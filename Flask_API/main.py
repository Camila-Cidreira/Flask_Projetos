from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Restaurantes(Resource):
    def get(self):
        return {'restaurantes' : 'meus restaurantes'}
        

api.add_resource(Restaurantes, '/restaurantes')


if __name__ == '__main__':
    app.run(debug=True)