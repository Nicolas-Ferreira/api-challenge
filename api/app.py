from flask import Flask
from flask_restful import Api

from resources.indicator import IndicatorFilter
from db import db
from db_setup import load_dataset

# App & app config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def create_tables():
    # Create tables
    db.create_all()
    # Load data from Challenge File
    load_dataset()

# Resources
api.add_resource(IndicatorFilter, '/filter_country_by_indicator')

if __name__ == '__main__':
    db.init_app(app)
    app.run(host="0.0.0.0")
