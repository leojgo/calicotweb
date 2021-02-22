import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Database configuration
    #  TODO: later to change to a file => 'sqlite:///' + os.path.join(basedir, 'calicotdb.db')+"?mode=memory&cache=shared"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql:///calicotdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Cryptographic key
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'voce-nunca-vai-adivinhar-esta-senha'