import os
from datetime import datetime

from flask_restplus import Namespace, Resource

api = Namespace("api")


@api.route('/meta')
class GetDirectory(Resource):
    @api.response(200, "Success")
    def get(self):
        resp = {"data": []}
        directory = os.getenv("DIRECTORY", "./")
        if directory[-1] != "/":
            directory += "/"
        for f in os.listdir(directory):
            ts = int(os.path.getctime(directory + f))
            t = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            if os.path.isfile(directory + f):
                resp["data"].append({
                    "name": f,
                    "type": os.path.splitext(f)[1],
                    "time": t,
                })
        return resp, 200
