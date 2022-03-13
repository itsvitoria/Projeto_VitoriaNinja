<h1>
    Desafio cincluído - BackEnd KaBum - <strong>EntreGa</strong>
</h1>

<h2>Descrição:</h2>
<strong>API REST</strong> para cálculo e seleção de modalidades de frete através de informações de <strong>Dimensão e Peso</strong> dos produtos adquiridos pelo cliente.
</br>
</br>
</br>
<h3>Linguagem:</h3>

- [Python](https://www.python.org/)

<h3>Micro framework:</h3>

- [Flask](https://flask.palletsprojects.com/en/2.0.x/)

<h3>Libs:</h3>

- requeriments.txt

<h2>Exemplo:</h2>

- Input: Dimensões e peso do produto (centimentros e gramas).

```json
{
    "dimensao": {
                    "altura":102,
                    "largura":40
                },
    "peso":400
}
````
- Output: De acordo com as especificações de cada modalidade e as dimensões do produto, são apresentadas as modalidades de frete possíveis, sendo elas: Entrega Ninja, Entrega KaBum, ambas ou nenhuma.
</br>

```json
[
	{
        "nome":"Entrega Ninja",
    	  "valor_frete": 12.00,
    	  "prazo_dias": 6
	},
	{
    	  "nome":"Entrega KaBuM",
    	  "valor_frete": 8.00,
    	  "prazo_dias": 4
	}
]
````
<h2>Clone o Repositório:</h2>

````bash
$ git clone https://github.com/itsvitoria/Projeto_VitoriaNinja.git
````
<h3>Funcionamento:</h3> 

- URL: https://127.0.0.1:5000/ 
- Documentação: https://127.0.0.1:5000/docs 