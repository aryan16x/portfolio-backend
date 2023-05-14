from decouple import config

class Config:
    SECRET_KEY = config("SECRET_KEY")
    MAIL_ID = config("MAIL_ID")
    PASSWORD = config("PASSWORD")
    

