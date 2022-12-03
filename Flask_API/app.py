from flask import Flask
from flask_restful import Api
from resources.restaurantes import (Restaurantes, Restaurante)

app = Flask(__name__)
api = Api(app)



api.add_resource(Restaurantes, '/restaurantes')
api.add_resource(Restaurante, '/restaurantes/<string:restaurante_id>')


if __name__ == '__main__':
    app.run(debug=True)

#http://127.0.0.1:5000/restaurantes