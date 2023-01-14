from Imports import *
from files import *
from Adresa import *

class Locuinta:
    def __init__(self,adr,*camere):
        self.__adresa=adr
        self.__listaCamere=[]
        for c in camere:
            self.__listaCamere.append(c)
        self.__suprafataTotala=0
        for c in camere:
            self.__suprafataTotala+=c.suprafata()
        self.__regimInaltime=[]
        for c in camere:
            self.__regimInaltime.append(c.getInaltime())
        self.__temperaturiEfective=[]

    def __repr__(self):
        return "Adresa locuintei este {}\n,camerele sunt {}\n,suprafata este {}\n,regimul de inaltime este"\
        " {}\n {}\n".format(str(self.__adresa),self.__listaCamere,self.__suprafataTotala,self.__regimInaltime,
        self.__temperaturiEfective)

    def addMasuratoare(self,mt):
        if len(self.__listaCamere)!=len(mt.getTemperaturiCamere()):
            raise Exception("Numarul este invalid!")
        for temp in mt.getTemperaturiCamere():
            if temp<5 or temp>30:
                raise Exception("Masuratoare invalida!")
        self.__temperaturiEfective.append(mt)

    def temperaturaReferinta(self):
        temp=0
        for camera in self.__listaCamere:
            temp+=camera.coefCaloric()
        temp=temp/len(self.__listaCamere)
        print("Temperatura referinta canonica: {}\n".format(temp))
        h=0
        for hh in self.__regimInaltime:
            h+=hh
        h=h/len(self.__regimInaltime)
        print("Inaltimea este: ",h)
        if h>2.6:
            h+=0.1
            x=(h-2.6)//0.1
            temp=temp-x*0.02*temp
        elif h<2.6:
            h += 0.1
            x = (2.6-h) // 0.1
            temp = temp + x * 0.02 * temp
        print("Temperatura referinta adaptata la regimul de inaltime: {}\n".format(temp))
        if self.__adresa.getOras() in zoneClimatice[2]:
            temp-=1
        elif self.__adresa.getOras() in zoneClimatice[3]:
            temp-=2
        elif self.__adresa.getOras() in zoneClimatice[4]:
            temp -= 3.5
        elif self.__adresa.getOras() in zoneClimatice[5]:
            temp -= 4.5
        print("Temperatura referinta adaptata la zona geografica: {}\n".format(temp))
        return temp

    def getListaCamere(self):
        return self.__listaCamere

    def getAdresa(self):
        return self.__adresa

    @staticmethod
    def getLocuinte():
        l = []
        file=open(APARTAMENTE,'r')
        if file!=None:
            for linie in file:
                entitati = linie.split(";")
                id = entitati[0].strip()
                adresa = entitati[1].split(":")[1].strip()
                camere = entitati[2].split(":")[1].strip()
                listaAdrese=Adresa.getAdrese()
                for a in listaAdrese:
                    if adresa == a.getid():
                        adresa=a
                for s in entitati [2:]:
                    if camere == s.getid():
                        camere=s


