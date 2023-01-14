from Imports import *
from Judet import *
from files import *
class Adresa:
    def __init__(self,str,nr,bl,ap,sc,et,oras,judet,cp):
        self.__id = None
        self.__strada=str
        self.__nr=nr
        self.__bloc=bl
        self.__apartament=ap
        self.__scara=sc
        self.__etaj=et
        self.__oras=oras
        self.__judet=judet
        self.__codPostal=cp

    def __repr__(self):
        s1="\n****************************"
        s2="\n*"+"Strada:"+self.__strada+"      *"
        s3="\n*"+"Nr:"+self.__nr+"                    *"
        s4="\n*"+"Bloc:"+str(self.__bloc)+"                    *"
        s5="\n*"+"Apartament:"+str(self.__apartament)+"              *"
        s6="\n*"+"Scara:"+str(self.__scara)+"                   *"
        s7="\n*"+"Etaj:"+str(self.__etaj)+"                    *"
        s8="\n*"+""+str(self.__oras)+","+str(self.__codPostal)+"          *"
        s9="\n*"+""+str(self.__judet)+"                     *"
        s10="\n****************************"
        return s1+s2+s3+s4+s5+s6+s7+s8+s9+s10

    def getStrada(self):
        return self.__strada
    def getid(self):
        return self.__id
    def setid(self,id):
        self.__id = id

    def setStrada(self,s):
        self.__strada=s

    def getNr(self):
        return self.__nr

    def getBloc(self):
        return self.__bloc


    def getApartament(self):
        return self.__apartament

    def getScara(self):
        return self.__scara

    def getEtaj(self):
        return self.__etaj

    def getOras(self):
        return self.__oras

    def setOras(self,o):
        self.__oras=o

    def getJudet(self):
        return self.__judet

    def setJudet(self,jud):
        self.__judet=jud

    def getcodPostal(self):
        return self.__codPostal

    @staticmethod
    def getAdrese():
        l= []
        file=open(ADRESE,'r')
        if file!=None:
            for linie in file:
                entitati = linie.split(";")

                entitati = linie.split(";")
                id = entitati[0].strip()
                strada = entitati[1].split(":")[1].strip()
                nr = entitati[2].split(":")[1].strip()
                bloc = entitati[3].split(":")[1].strip()
                apartament = int(entitati[4].split(":")[1].strip())
                scara = entitati[5].split(":")[1].strip()
                etaj = int(entitati[6].split(":")[1].strip())
                oras = entitati[7].split(":")[1].strip()
                judet = Judet.stringToJudet(entitati[8].split(":")[1].strip())
                codPostal = int(entitati[9].split(":")[1].strip())

                b1=Adresa(strada,nr,bloc,apartament,scara,etaj,oras,judet,codPostal)
                l.append(b1)
            file.close()
            return l
        else:
            raise Exception("Fisierul nu a putut fi deschis!!!")

    def insertFisier(self):
        file=open("Adrese.txt",'a')
        if file!=None:
            s1 = "strada:"+self.__strada+";"
            s2 = "numar:" + self.__nr + ";"
            s3 = "bloc:" + self.__bloc + ";"
            s4 = "apartament:" +self.__apartament+";"
            s5 = "scara:"+self.__scara+";"
            s6 = "etaj:"+self.__etaj+";"
            s7 = "oras:"+self.__oras+";"
            s8 = "judet:"+self.__judet+";"
            s9 = "codPostal:"+self.__codPostal+";"
            s1+s2+s3+s4+s5+s6+s7+s8+s9
            file.write(s1+s2+s3+s4+s5+s6+s7+s8+s9)
            file.close()
        else:
            raise Exception("Fisierul nu a putut fi deschis!!!")