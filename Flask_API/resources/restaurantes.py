''' MÓDULO DE RESTAURANTES '''

from flask_restful import Resource


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
    def get(self, restaurante_id):

        for restaurante in restaurantes:
            if restaurante('restaurante_id') == restaurante_id :
                return restaurante
        return {'message': 'Restaurante not found.'}, 404

    def post(self, restaurante_id):

        pass

    def put(self, restaurante_id):

        pass

    def delete(self, restaurante_id):

        pass


if __name__ == "__main__":
    print(__doc__)