from datetime import datetime

from flask import Flask, render_template, request
from google.cloud import datastore
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def root():
    if request.method == 'POST':
        #return "retorno: "+request.form['pAgua']
        return buscar(request.form['pAgua'], request.form['pLeite'], request.form['pote2l'], request.form['produzidosPa'], request.form['produzidosPl'], request.form['produzidosP'])
    else:
        return render_template('index.html')

@app.route('/buscar')
def buscar(pAgua, pLeite, pote2l, produzidosPa, produzidosPl, produzidosP):
        try:
            produzidosPl = int(produzidosPl)
            produzidosP = int(produzidosP)
            produzidosPa = int(produzidosPa)
            pAgua=int(pAgua)
            pLeite = int(pLeite)
            pote2l = int(pote2l)
            custoPicoleLeite = float(0.25)
            custoPicoleAgua = float(0.15)
            custoPote2l = float(2.50)
            custoProducao = (custoPicoleAgua * produzidosPa) + (custoPote2l * produzidosP) + (custoPicoleLeite * produzidosPl)
            totalVendido = (pAgua * float(1.50)) + (pote2l * float(18.0)) + (pLeite * float(2.00))
            carreteiros = float(0.4) * (pAgua * float(1.50)) + float(0.4) * (pLeite * float(2.00))
            lucro = float(totalVendido - carreteiros - custoProducao)

            #grava resulado no bd
            datastore_client = datastore.Client()
            entity = datastore.Entity(key=datastore_client.key('results'))
            entity.update({
                'timestamp': datetime.datetime.now(),
                'lucro': lucro,
                'custoProducao' : custoProducao,
                'custoCarreteiros' : carreteiros
            })

            if lucro < 0:
               return "Prejuizo de: ", str(lucro)
            else:
                #return str(lucro)
                tupla =("Lucro de: "+ str(lucro), "Custo de produção: "+ str(custoProducao),'Custo carreteiro: '+ str(carreteiros))
                return render_template('resultados.html', tupla=tupla)
        except:
            return NameError


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)