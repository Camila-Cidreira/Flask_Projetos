from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

restaurantes = [
    
    {'restaurante_id': 'Amado',
    'nome': 'Restaurante Amado',
    'estrelas': '4.9',
    'valor médio': '500',
    'cidade':'Salvador'
    },

    {'restaurante_id': 'Ki-mukeka',
    'nome': 'Restaurante Ki-mukeka',
    'estrelas': '4.6',
    'valor médio': '250',
    'cidade':'Lauro de Freitas'
    },

    {'restaurante_id': 'Bom Paladar',
    'nome': 'Restaurante Bom Paladar',
    'estrelas': '4.5',
    'valor médio': '100',
    'cidade':'Camaçari'
    }
]

class Restaurantes(Resource):
    def get(self):
        return {'restaurantes' : 'restaurantes'}
        

api.add_resource(Restaurantes, '/restaurantes')


if __name__ == '__main__':
    app.run(debug=True)

#http://127.0.0.1:5000/restaurantes