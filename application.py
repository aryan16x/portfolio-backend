from flask import Flask,request,jsonify
from flask_restx import Api,Resource
from config import Config
from flask_mail import Mail,Message
from flask_cors import CORS
import tensorflow as tf
import pandas as pd
import pickle

application = Flask(__name__)

application.config.from_object(Config)
application.config['MAIL_SERVER'] = "smtp.gmail.com"
application.config['MAIL_PORT'] = 587
application.config['MAIL_USE_TLS'] = True
application.config['MAIL_USE_SSL'] = False
application.config['MAIL_USERNAME'] = Config.MAIL_ID
application.config['MAIL_PASSWORD'] = Config.PASSWORD

CORS(application)


mail = Mail(application)

api = Api(application, doc='/docs')

# @api.route('/wineModel')
# class wine_model(Resource):
#     def post(self):
#         data = request.get_json()
#         wine_model = tf.keras.models.load_model("wine_model")
#         prediction = wine_model.predict([[int(data.get('fixed_acidity')),
#                                           int(data.get('volatile_acidity')),
#                                           int(data.get('citric_acid')),
#                                           int(data.get('residual_sugar')),
#                                           int(data.get('chlorides')),
#                                           int(data.get('free_sul_dio')),
#                                           int(data.get('total_sul_dio')),
#                                           int(data.get('density')),
#                                           int(data.get('pH')),
#                                           int(data.get('sulphates')),
#                                           int(data.get('alcohol'))]])
#         return str(int(prediction[0][0]))
    
@api.route('/blueberry')
class blueberry(Resource):
    def post(self):
        data = request.get_json()
        dx = {
            "clonesize" : data.get("clonesize"),
            "honeybee" : data.get("honeybee"), 
            "bumbles" : data.get("bumbles"),
            "andrena" : data.get("andrena"),
            "osmia" : data.get("osmia"),
            "MaxOfUpperTRange" : data.get("MaxOfUpperTRange"),
            "MinOfUpperTRange" : data.get("MinOfUpperTRange"),
            "AverageOfUpperTRange" : data.get("AverageOfUpperTRange"),
            "MaxOfLowerTRange" : data.get("MaxOfLowerTRange"),
            "MinOfLowerTRange" : data.get("MinOfLowerTRange"),
            "AverageOfLowerTRange" : data.get("AverageOfLowerTRange"),
            "RainingDays" : data.get("RainingDays"),
            "AverageRainingDays" : data.get("AverageRainingDays"),
            "fruitset" : data.get("fruitset"),
            "fruitmass" : data.get("fruitmass"),
            "seeds" : data.get("seeds")
        }
        df = pd.DataFrame(dx, index=[0])
        model = pickle.load(open("model.pkl", 'rb'))
        prediction = model.predict(df)
        return str(int(prediction[0]))
    
@api.route('/contact')
class contact(Resource):
    def post(Resource):
        data = request.get_json()
        mailId = data.get('email')
        message = data.get('message')
        msg = Message(subject="New Mail from website",body=f"E-mail: {mailId}\nMessage: {message}", sender=Config.MAIL_ID, recipients=['aryan.gadhiya2021@vitstudent.ac.in'])
        mail.send(msg)
        return "Sent message"
    

if __name__ == '__applicationlication__':
    application.run()
