from dotenv  import load_dotenv
from datetime import date
import logging
load_dotenv()
import os
from flask_sqlalchemy import SQLAlchemy
import logging
from sqlalchemy import create_engine



class Config:
    DEBUG = bool(os.getenv('DEBUG',False))
    DEVELOPMENT = bool(os.getenv('DEVELOPMENT',False))
    CSRF_ENABLED = True
    URL_PREFIX = 'api'
    SECRET_KEY = 'Your_secret_string_dev'
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    # SQLALCHEMY_READ_DATABASE_URI = os.getenv('SQLALCHEMY_READ_DATABASE_URI')
    SQLALCHEMY_ECHO = False
    FIXED_RATE = 200
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 30
    SQLALCHEMY_MAX_OVERFLOW = 20
    SQLALCHEMY_POOL_PRE_PING = True
    SQLALCHEMY_POOL_RECYCLE = 300
    # READ_REPLICA_ENGINE = create_engine(SQLALCHEMY_READ_DATABASE_URI, pool_pre_ping=True, pool_size=20, max_overflow=20)
    PORT = os.getenv('PORT') 
    DATETIME_FORMAT =  os.getenv('DATETIME_FORMAT')
    SECRET_KEY =  os.getenv('SECRET_KEY')
    JWT_ALGORITHM  = os.getenv('JWT_ALGORITHM')
    JWT_TOKEN_TIME_OUT_IN_MINUTES = int(os.getenv('JWT_TOKEN_TIME_OUT_IN_MINUTES',5))
    # JWT_TOKEN_TIME_OUT_IN_MINUTES = 2
    JWT_REFRESH_TOKEN_TIME_OUT_IN_MINUTES = int(os.getenv('JWT_REFRESH_TOKEN_TIME_OUT_IN_MINUTES',525600))
   



db = SQLAlchemy()


# FORMAT = ('%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] '
#           '[dd.service=%(dd.service)s dd.env=%(dd.env)s dd.version=%(dd.version)s dd.trace_id=%(dd.trace_id)s dd.span_id=%(dd.span_id)s] '
#           '- %(message)s')

# logging.basicConfig(format=FORMAT)
# log = logging.getLogger('gunicorn.error')
# log.level = logging.INFO
