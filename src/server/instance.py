#Libs ===========================================================
from flask import Flask
from flask_restx import Api

#Server definitions =============================================
class Server():
    def __init__(self, ):
        self.app = Flask(__name__)
        self.api = Api(self.app,
        version='7.7',
        title='Projeto EntreGa - KaBum!',
        description='API para cálculo e seleção de modalidades de frete',
        doc='/docs')

#Debug for test =================================================
    def run(self,):
        self.app.run(
            
            debug=True
            
        )

server = Server()