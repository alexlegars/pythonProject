from flask_restful import Resource
import ijson

class GTData(Resource):
    def get(self, eventid):
        with open('data/globalterrorism.json') as gtdb_raw:
            gtdb = ijson.items(gtdb_raw, 'item')
            for gt in gtdb:
                if(eventid == gt["eventid"]):
                    return gt, 200
        return "Terrorist attack not found", 404