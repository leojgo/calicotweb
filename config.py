import os
import urllib

basedir = os.path.abspath(os.path.dirname(__file__))
database_url = os.environ.get('DATABASE_URL')

class Config(object):
    """ Base configuration """
    # Database configuration
    SQLALCHEMY_DATABASE_URI = database_url or \
        'postgresql:///calicotdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Cryptographic key
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'voce-nunca-vai-adivinhar-esta-senha'

class ProductionConfig(Config):
    if database_url:
        params = urllib.parse.quote_plus(database_url)
        SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc:///?odbc_connect={params}"
    else:
        if os.environ.get('FLASK_ENV') == 'production':
            raise ValueError("Environment variable not set: DATABASE_URL")