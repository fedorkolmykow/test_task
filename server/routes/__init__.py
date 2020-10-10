from flask_restplus import Api

from .logical_route import api as dir_api

api = Api()
api.add_namespace(dir_api)
