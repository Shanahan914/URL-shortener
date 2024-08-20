import os

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'postgresql://username:password@localhost/dbname')
SQLALCHEMY_TRACK_MODIFICATIONS = False 