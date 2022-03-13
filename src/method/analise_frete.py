#Libs =================================================
from flask_restx import fields

#Server ===============================================
from src.server.instance import server

#Data descriptions ====================================
dimensao = server.api.model('dimensao_produto',{
    'altura': fields.Integer(description='Altura: '),
    'largura': fields.Integer(description='Largura: ')
})
requisicao = server.api.model('Requisicao', {
    'dimensao_produto': fields.Nested(dimensao),
    'peso' : fields.Integer(description='Peso: ')
})
retorno = server.api.model('Retorno', {
    'Tipo': fields.String(description='Modalidade de entrega: '),
    'Frete': fields.String(description='Frete: '),
    'Prazo': fields.Integer(description='Prazo: ')
})  
        
   