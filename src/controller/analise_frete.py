#Libs ==============================================================
from flask import Flask, request
from flask_restx import Api, Resource
from method.tipo_frete import metodo_kabum

#Server ============================================================
from src.server.instance import server

#Classes and functions =============================================
from method.analise_frete import requisicao, retorno
from method.tipo_frete import *

app = server.app
api = server.api

#POST request definition ===========================================
@api.route('/cotacao')
class resposta_frete(Resource):
    @api.expect(requisicao, validate=True)
    @api.marshal_with(retorno)
    def post(self, ):
        
#Input (JSON) ======================================================
        payload = api.payload

#Product dimensions request ========================================
        altura = payload["dimensao"]["altura"]
        largura = payload["dimensao"]["largura"]
        peso = payload["peso"]
            
#Calculation =======================================================
        ninja = metodo_ninja(altura, largura, peso)
        kabum = metodo_kabum(altura, largura, peso)

#Analysis and definition of modalities =============================
        if ninja == None and kabum == None:
            return []
        elif ninja == None:
            return [kabum]
        elif kabum == None:
            return [ninja]
        else:
            return [ninja, kabum]
