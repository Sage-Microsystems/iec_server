import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY", "50m3h@rd2gu3555tr1ng0rp@55w0rd")
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_PATH = os.path.join(basedir, "data-dev.sqlite")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + SQLALCHEMY_DATABASE_PATH

class TestingConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_PATH = os.path.join(basedir, "data-test.sqlite")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + SQLALCHEMY_DATABASE_PATH

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_PATH = os.path.join(basedir, "data-prod.sqlite")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + SQLALCHEMY_DATABASE_PATH

config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "test": TestingConfig,
    "default": DevelopmentConfig,
}
