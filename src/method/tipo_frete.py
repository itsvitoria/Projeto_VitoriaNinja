# Class ==========================================================================
from controller.analise_frete import *

# Ninja - Conditions =============================================================


def metodo_ninja(altura, largura, peso):
    especificacao = 10 <= altura <= 200 and 6 <= largura <= 140 and peso > 0
    if especificacao:
        c_ninja = 0.3
        prazo = 6
        frete = (peso*c_ninja)/10
        metodo = {'Tipo': 'Entrega Ninja',
                  'Frete': f'{frete:.2f}', 'Prazo': prazo}
        return metodo
    else:
        None

# KaBum - Conditions =============================================================


def metodo_kabum(altura, largura, peso):
    especificacao = 5 <= altura <= 140 and 13 <= largura <= 125 and peso > 0
    if especificacao:
        c_kabum = 0.2
        prazo = 4
        frete = (peso*c_kabum)/10
        metodo = {'Tipo': 'Entrega KaBuM',
                  'Frete': f'{frete:.2f}', 'Prazo': prazo}
        return metodo
    else:
        None
