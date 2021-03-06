import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Base configuration"""


class ProductionConfig(Config):
    """Production configuration"""


class DevelopmentConfig(Config):
    """Development configuration"""

    JSONIFY_PRETTYPRINT_REGULAR = True
    ENV = "development"
    DEBUG = True


class TestingConfig(Config):
    """Testing configuration"""

    TESTING = True
