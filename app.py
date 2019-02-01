from flask import Flask
from flask_restful import Api, Resource, reqparse

import parser
from csvtojson import convertCSVtoJSON

convertCSVtoJSON()

app = Flask(__name__)
api = Api(app)