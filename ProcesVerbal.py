from Imports import *
class ProcesVerbal:
    def __init__(self,locuinta,mt,agent):
        self.__locuinta=locuinta
        self.__masuratoareTemperatura=mt
        self.__locuinta.addMasuratoare(mt)
        self.__agent=agent

    def __repr__(self):
        a="Locuinta: "+str(self.__locuinta)+"\n\n"
        b="Masuratoare temperatura: "+str(self.__masuratoareTemperatura)+"\n\n"
        c="Agent :"+str(self.__agent)+"\n\n"
        return a+b+c

    def toFile(self):
        titular=self.__locuinta.getListaCamere()[0].getListaPersoane()[0]
        numeTitular=titular.getNume()+" "+titular.getPrenume()
        data=self.__masuratoareTemperatura.getData()
        timp=self.__masuratoareTemperatura.getTimp()
        adresa=self.__locuinta.getAdresa()
        strada=adresa.getStrada()
        nr=str(adresa.getNr())
        oras=adresa.getOras()
        judet=str(adresa.getJudet())
        tempRef=self.__locuinta.temperaturaReferinta()
        temperaturi=self.__masuratoareTemperatura.getTemperaturiCamere()
        suma=0
        for t in self.__masuratoareTemperatura.getTemperaturiCamere():
            suma=suma+t
        temperaturaMedieLocuinta=suma/len(self.__masuratoareTemperatura.getTemperaturiCamere())
        numeFisier="Amenda "+numeTitular+" .html"
        file=open(numeFisier,"w")
        file.write("<html>")
        file.write("<head>")
        file.write("<title> Amenda "+numeTitular+" </title>")
        file.write("</head>")
        file.write("<body>")
        file.write("<h1> Proces Verbal </h1>")
        file.write("<p> Pentru "+numeTitular+" </p>")
        file.write("<p> Pentru locuinta situata pe strada "+strada+ "," + " nr. " +nr+ "," + " ora&#351 "+oras+"," + " jude&#355 "+judet+"." + " </p>")
        file.write("<p> Temperatura de referin&#355&#259 a locuin&#355ei: "+str(self.__locuinta.temperaturaReferinta()))
        file.write("<table border=\"1\">")
        file.write("<tr>")
        for i in range(len(self.__masuratoareTemperatura.getTemperaturiCamere())):
            s="<td> Camera "+str(i+1)+"</td>"
            file.write(s)
        file.write("</tr>")
        file.write("<tr>")
        for temperatura in self.__masuratoareTemperatura.getTemperaturiCamere():
            s = "<td> " + str(temperatura) + "</td>"
            file.write(s)
        file.write("</tr>")
        file.write("</table>")
        file.write("<p> Temperatura medie a locuin&#355ei: </p>"+str(temperaturaMedieLocuinta))
        file.write("<p> Tip amend&#259: AVERTISMENT </p>")
        file.write("<p> Semn&#259turi: </p>")
        file.write("<p> Agent: "+str(self.__agent.getNume())+" "+str(self.__agent.getPrenume())+"</p>")
        file.write("<p>  </p>"+self.__locuinta.getListaCamere()[0].getListaPersoane()[0].getNume()+" "+self.__locuinta.getListaCamere()[0].getListaPersoane()[0].getPrenume())
        file.write("</body>")
        file.write("</html>")
        file.write("</html>")
        file.close()

    def tipAmenda(self):
        d = 0
        sum = 0
        for t in self.__masuratoareTemperatura.getTemperaturiCamere():
            sum = sum + t
        temperaturaMedie = sum / len(self.__masuratoareTemperatura.getTemperaturiCamere())
        d = temperaturaMedie - self.__locuinta.temperaturaReferinta()
        q = 0
        if d <= 0.5:
            q = 0
        elif d > 0.5 and d <= 1:
            q = 100
        elif d > 1 and d <= 1.5:
            q = 200
        elif d > 1.5 and d <= 2:
            q = 300
        elif d > 2 and d <= 3:
            q = 400
        elif d > 3:
            q = 1000

        x = len(self.__locuinta.getTemperaturiEfective()) - 1   #coeficient de ignoranta
        coef = 1
        if x == 1:
            coef = 1.5
        elif x >= 2 and x <= 4:
            coef = 2
        elif x >= 5:
            coef = 10

        if q == 0 and x < 1:
            return -1
        elif q == 0 and x >= 1:
            return 100
        return q * coef