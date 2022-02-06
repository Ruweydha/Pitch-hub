from distutils.command import config
from distutils.debug import DEBUG
import os


class Config:
    '''
    General configuration parent class
    '''   

class ProdConfig(Config):
    '''
    Production Configuration class

    Args:
      Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development configuration child class 

    Args:
      Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:R0707318659@localhost/pitch'
    DEBUG = True

config_options = {
  'development': DevConfig,
  'production': ProdConfig,
}    