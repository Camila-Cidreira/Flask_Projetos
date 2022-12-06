

from flask_restful import Resource, reqparse


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
        return {"Restaurantes" : restaurantes}
        

class Restaurante(Resource):
    
    def find_restaurante(restaurante_id):
        for restaurante in restaurantes:
            if restaurante.get('restaurante_id') == restaurante_id :
                return restaurante
        return {'message': 'Restaurante not found.'}, 404
        

    def get(self, restaurante_id):

        restaurante = Restaurante.find_restaurante(restaurante_id)
        
        if restaurante:
            return restaurante
        return {'message': 'Restaurante not found.'}, 404

    def post(self, restaurante_id):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('nome')
        argumentos.add_argument('estrelas')
        argumentos.add_argument('valor médio')
        argumentos.add_argument('cidade')

        dados = argumentos.parse_args()

        novo_restaurante = {
            'restaurante_id': restaurante_id,
            'nome': dados['nome'],
            'estrelas': dados['estrelas'],
            'valor médio': dados['valor médio'],
            'cidade': dados['cidade']
        }

        restaurantes.append(novo_restaurante)
        return novo_restaurante, 200



        

    def put(self, restaurante_id):

        pass

    def delete(self, restaurante_id):

        pass


