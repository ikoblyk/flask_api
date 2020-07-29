import random
import string

def get_random_string(length):
    key = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(key) for i in range(length))
    return result_str

class Config(object):
    DEBUG = False
    UPLOAD_FOLDER= 'images'
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_DEFAULT_SENDER= 'scalettavito285@gmail.com'
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT= 465
    MAIL_USERNAME= 'scalettavito285@gmail.com'
    MAIL_PASSWORD= 'lucescu2020'
    MAIL_USE_TLS= False
    MAIL_USE_SSL= True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://ivan:cherikcr7@127.0.0.1:3306/prod'
    SECRET_KEY= get_random_string(10)
    SECURITY_PASSWORD_SALT= get_random_string(16)

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://ivan:cherikcr7@127.0.0.1:3306/dev'
    SQLALCHEMY_ECHO = False
    SECRET_KEY= get_random_string(10)
    SECURITY_PASSWORD_SALT= get_random_string(16)
    MAIL_DEFAULT_SENDER= 'scalettavito285@gmail.com'
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT= 465
    MAIL_USERNAME= 'scalettavito285@gmail.com'
    MAIL_PASSWORD= 'lucescu2020'
    MAIL_USE_TLS= False
    MAIL_USE_SSL= True
    SWAGGER_URL='https://inspector.swagger.io/builder'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://ivan:cherikcr7@127.0.0.1:3306/test'
    SQLALCHEMY_ECHO = False
    SECRET_KEY= get_random_string(10)
    SECURITY_PASSWORD_SALT= get_random_string(16)
    MAIL_DEFAULT_SENDER= 'scalettavito285@gmail.com'
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT= 465
    MAIL_USERNAME= 'scalettavito285@gmail.com'
    MAIL_PASSWORD= 'lucescu2020'
    MAIL_USE_TLS= False
    MAIL_USE_SSL= True
    JWT_SECRET_KEY = 'JWT-SECRET'
    UPLOAD_FOLDER= 'images'
