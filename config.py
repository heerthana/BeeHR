# config.py

DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
SECRET_KEY = "BSVIiuYZcTAzHRe07NzEgYqveb6mFkdj"
JWT_ALGORITHM = "HS256"
JWT_TOKEN_TIME_OUT_IN_MINUTES = 600

EMAIL = 'darsanameenakshi.1605014@srec.ac.in'
PASSWORD = ''
APP_BASE_URL = 'http://localhost:5000'

ENABLE_AUTH = False


class Config(object):
    CSRF_ENABLED = True
    """
    Common configurations
    """
    FIXED_RATE = 000
    URL_PREFIX = 'api'


class DevelopmentConfig(Config):
    # pymysql - for pip install pymysql || mysql-python not needed
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:iphone21@127.0.0.1:5432/beehr'
    SECRET_KEY = 'Your_secret_string_dev'
    SQLALCHEMY_ECHO = True
    DEVELOPMENT = True
    DEBUG = True
    FIXED_RATE = 200


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:iphone21@localhost/hoi'
    SECRET_KEY = 'Your_secret_string_prod'
    DEBUG = True
    FIXED_RATE = 300


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
