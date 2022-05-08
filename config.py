import os

class Config:
    # SECRET_KEY='ercfgvbniojnngfdfgssdfghjsdfghdfg'
    SECRET_KEY='secret key'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://abrighthuman:bright@localhost/pitch'
    UPLOADED_PHOTOS_DEST='app/static/photos'
    # email configurations
    MAIL_SERVER = 'stmp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')


    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://abrighthuman:bright@localhost/pitch'
DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}