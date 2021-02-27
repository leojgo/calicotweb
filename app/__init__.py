import os
from flask import Flask
from config import Config, ProductionConfig
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
if os.environ.get('FLASK_ENV') == 'production':
    app.config.from_object(ProductionConfig)
else:
    app.config.from_object(Config)

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

from app import routes, models