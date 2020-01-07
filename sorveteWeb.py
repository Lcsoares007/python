import os
import cherrypy
import urllib.request
class sorveteWeb():
    @cherrypy.expose
    def index(self):
        page = urllib.request.urlopen("http://127.0.0.1:8080/static/index.html")
        text = page.read().decode("utf8")
        return text
    @cherrypy.expose
    def buscar(self, pAgua, pLeite, pote2l, produzidosPa, produzidosPl, produzidosP):
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


#tutconf = os.path.join(os.path.dirname(__file__), 'tutorial.conf')
#tutconf = '/tutorial.confg'
if __name__=='__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    cherrypy.quickstart(sorveteWeb(), '/', conf)
