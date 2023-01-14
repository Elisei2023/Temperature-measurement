from Imports import *
from files import *
class Camera:
    def __init__(self,L,l,i,t,tP):
        self.__id=None
        self.__lungime=L
        self.__latime=l
        self.__inaltime=i
        self.__termoizolat=t
        self.__TipPerete=tP
        self.__listaPersoane=[]
    def __repr__(self):
        return  "id este" + str(self.__id) + " Camera are lungimea " + str(self.__lungime) + " metri, latimea " + str(self.__latime) + " metri, si inaltimea " + \
                str(self.__inaltime) +" metri " + str(self.__termoizolat) +" si are perete de " + self.__TipPerete +""
    def volum(self):
        volum= self.__lungime * self.__latime * self.__inaltime
        return volum
    def suprafata(self):
        suprafata= self.__lungime * self.__latime
        return suprafata
    def getInaltime(self):
        return self.__inaltime
    def getListaPersoane(self):
        return self.__listaPersoane
    def getid(self):
        return self.__id
    def setid(self,id):
        self.__id = id
    def adaugaPersoana(self,p):
        if self.suprafata()<=10:
            return False
        dif=self.volum()-12*len(self.__listaPersoane)
        if dif<12:
            return False
        else:
            self.__listaPersoane.append(p)
            return True
    def scoatePersoana(self,cnpPersoana):
        for persoana in self.__listaPersoane:
            if cnpPersoana==persoana.getCNP():
                self.__listaPersoane.remove(persoana)
                return True
        return False
    def coefCaloric(self):
        standard=14.5
        for persoana in self.__listaPersoane:
            standard=standard+persoana.consumCaloric()
        if self.__termoizolat==False:
            standard-=1
        if self.__TipPerete.upper()=="CIMENT":
            standard-=1
        return standard
    def adaugaPersoane(self,*p):
        for persoana in p:
            self.__listaPersoane.append(persoana)


    @staticmethod
    def getCamere():
        l = []
        file=open(CAMERE,'r')
        if file!=None:
            for linie in file:
                entitati = linie.split(";")
                id = entitati[0].strip()
                lungime = entitati[1].split(":")[1].strip()
                latime = entitati[2].split(":")[1].strip()
                inaltime = entitati[3].split(":")[1].strip()
                termoizolat = entitati[4].split(":")[1].strip()
                if termoizolat == "DA":
                    termoizolat = True
                else:
                    termoizolat = False
                tipperete = entitati[5].split(":")[1].strip()
                c1 = Camera(lungime,latime,inaltime,termoizolat,tipperete)
                c1.setid(id)

                l.append(c1)
            file.close()
            return l
        else:
            raise Exception("Fisierul nu a putut fi deschis!!!")

    def insertFisier(self):
        file=open(CAMERE,'a')
        if file!=None:
            if self.__id==None:
                id="Camera@"
                h=hash((self.__lungime,self.__inaltime,self.__latime,self.__termoizolat,self.__TipPerete))
                h=hex(h)
                h=h[2:]
                id=id+h+";"
            self.__id=id
            s0=id
            s1 = "lungime:"+str(self.__lungime)+";"
            s2 = "latime:" + str(self.__latime) + ";"
            s3 = "inaltime:" +str( self.__inaltime) + ";"
            if self.__termoizolat == True:
                s4 = "termoizolat:DA;"
            else:
                s4 = "termoizolat:NU;"
            s5 = "tipperete:"+str(self.__TipPerete)+";"

            file.write("\n"+s0+s1+s2+s3+s4+s5)
            file.close()
        else:
            raise Exception("Fisierul nu a putut fi deschis!!!")
