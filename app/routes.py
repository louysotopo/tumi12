from flask_restful import Api
from app.resources.index import Index

from app import app
#Api
api = Api(app)
#Routes
api.add_resource(Index, '/', '/<string:id>')