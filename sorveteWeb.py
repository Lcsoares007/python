from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def root():
    return  render_template('index.html')
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
            if lucro < 0:
               return "Prejuizo de: ", str(lucro)
            else:
            #    return "Lucro de: "
                return "Lucro de: ", str(lucro), "</br>Custo de produção: ", str(custoProducao),'</br>Custo carreteiro: ', str(carreteiros)
        except:
            return NameError


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)