import flask
#para autenticação
import flask_basicauth
#from flask.wrappers import Response
from textblob import TextBlob
import pandas as pd
from sklearn.linear_model import LinearRegression
#para exportar e importar o arquivos .sav de serialização
import pickle
#os Para fazer uso do terminal 
import os


columns = ["tamanho","ano","garagem", "Preco"]

#--------Modelo com 1 'feature'---SERIALIZED-------

#cada '../' desce 1 diretório, uma vez que estamos em  mlops_first_prediction\src\app\main.py
model = pickle.load(open('../../models/model.sav','rb'))

#--------Modelo com 3 'features'---SERIALIZED------

model_3f = pickle.load(open('../../models/model_3f.sav','rb'))


#-------Iniciando a aplicação com flask ---------
app = flask.Flask('__name__')

#-------------Autenticação-----------------------

#app.config['BASIC_AUTH_USERNAME'] = 'usuário'
app.config['BASIC_AUTH_USERNAME'] = os.environ.get('BASIC_AUTH_USERNAME')
#app.config['BASIC_AUTH_PASSWORD'] = 'senha'
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get('BASIC_AUTH_PASSWORD')

basic_auth = flask_basicauth.BasicAuth(app)


#rota 'home'
@app.route('/')
def home():
    return 'Minha primeira API para Python ML.'

@app.route('/sentimento/<frase>')
@basic_auth.required
def sentimento(frase):
    text_Blob_Test = TextBlob(frase)
    text_Blob_Test_ING = text_Blob_Test.translate(to='en')
    polaridade = text_Blob_Test_ING.sentiment.polarity
    return f'A polaridade da frase é: {polaridade}'


@app.route('/cotacao/<int:tamanho>', methods=['GET'])
@basic_auth.required
def cotacao(tamanho):
    preco = model.predict([[tamanho]])
    return str(preco) # Forçando cast pra string por causa da resposta


@app.route('/cotacao3f/', methods=['POST'])
@basic_auth.required
def cotacao3f():
    data_json = flask.request.get_json()
    data_input = [data_json[col] for col in columns]
    preco = model_3f.predict([data_input])
    #return str(preco)
    data_output = flask.jsonify(
        {"preco": str(preco[0])}
    )
    #response = flask.make_response(data_output, 401,)
    #response.headers["Content-Type"] = "application/json"
    return data_output
    #return response

app.run(debug=True, host='0.0.0.0', port=5009) #0.0.0.0 resolve em todos os ambientes
# Rodando debug mode True o flask identifica sozinho 
# alterações no código e 'restarta' a aplicação

#ALTERAÇÂO
