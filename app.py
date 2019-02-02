from flask import Flask
from flask_restful import Api, Resource, reqparse

from globalterrorism import GTData

#import parser
#from csvtojson import convertCSVtoJSON

#convertCSVtoJSON()

app = Flask(__name__)
api = Api(app)

api.add_resource(GTData, "/gt/<string:eventid>")
app.run(debug=True)