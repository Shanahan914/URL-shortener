import os

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', )
SQLALCHEMY_TRACK_MODIFICATIONS = False 