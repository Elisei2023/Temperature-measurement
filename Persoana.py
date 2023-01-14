from Imports import *
from Sex import *
from TipActivitate import *
class Persoana:
    def __init__(self,c,n,p,v,s,t):
        self.__cnp=c
        self.__nume=n
        self.__prenume=p
        self.__varsta=v
        self.__sex=s
        self.__TipActivitate=t


    def __repr__(self):
        return "Persoana cu numele "+ self.__nume +", prenumele "+self.__prenume+", CNP "+str(self.__cnp)+", varsta "+\
               str(self.__varsta)+", sex "+str(self.__sex)+", si tipul de activitate "+str(self.__TipActivitate)+"."

    def getCNP(self):
        return self.__cnp
    def getNume(self):
        return self.__nume
    def getPrenume(self):
        return self.__prenume
    def getVarsta(self):
        return self.__varsta
    def getSex(self):
        return self.__sex
    def getTipActivitate(self):
        return self.__TipActivitate
    def setNume(self,n):
        self.__nume=n
    def setPrenume(self,p):
        self.__prenume=p
    def setVarsta(self,v):
        self.__varsta=v
    def setTipActivitate(self,t):
        self.__TipActivitate=t
    def consumCaloric(self):
        if self.__varsta<3:
            return 0.4
        elif self.__varsta<6:
            return 0.5
        elif self.__varsta<8:
            return 0.6
        elif self.__varsta<10:
            return 0.7
        elif self.__varsta<13:
            return 0.8
        elif self.__varsta<22:
            return 1.0
        elif self.__sex==Sex.FEMALE and self.__TipActivitate==TipActivitate.HEAVY:
            return 1.2
        elif self.__sex==Sex.FEMALE and self.__TipActivitate==TipActivitate.MODERATE:
            return 0.9
        elif self.__sex==Sex.FEMALE and self.__TipActivitate==TipActivitate.SEDENTARY:
            return 0.8
        elif self.__sex==Sex.MALE and self.__TipActivitate==TipActivitate.HEAVY:
            return 1.6
        elif self.__sex==Sex.MALE and self.__TipActivitate==TipActivitate.MODERATE:
            return 1.2
        elif self.__sex==Sex.MALE and self.__TipActivitate==TipActivitate.SEDENTARY:
            return 1.0

    @staticmethod
    def __cnp2Lista(n):
        lista = []
        while n != 0:
            u = n % 10
            n = n // 10
            lista.append(u)
        lista.reverse()
        return lista

    @staticmethod
    def __validareSex(lista):
        digit = lista[0]
        if digit == 1:
            return ("M", 1900)
        elif digit == 2:
            return ("F", 1900)
        elif digit == 3:
            return ("M", 1800)
        elif digit == 4:
            return ("F", 1800)
        elif digit == 5:
            return ("M", 2000)
        elif digit == 6:
            return ("F", 2000)
        elif digit == 7:
            return ("M")
        elif digit == 8:
            return ("F")
        else:
            return None

    @staticmethod
    def __validareDataNasterii(lista):
        an = lista[1] * 10 + lista[2]
        x = Persoana.__validareSex(lista)
        if x != None:
            if len(x) == 2:
                an = an + x[1]
        else:
            raise Exception("Anul nasterii nu poate fi calculat")
        luna = lista[3] * 10 + lista[4]
        zi = lista[5] * 10 + lista[6]
        if luna < 1 or luna > 12:
            return None
        if luna in [1, 3, 5, 7, 8, 10, 12]:
            if zi > 31:
                return None
        if luna in [4, 6, 9, 11]:
            if zi > 30:
                return None
        if an % 4 == 0 and luna == 2:
            if zi > 29:
                return None
        if an % 4 != 0 and luna == 2:
            if zi > 28:
                return None
        data = datetime.date(an, luna, zi)
        return data

    @staticmethod
    def __validareJudet(lista):
        l = [i for i in range(1, 49)]
        l.append(51)
        l.append(52)
        judet = lista[7] * 10 + lista[8]
        if judet in l:
            return True
        else:
            return False

    @staticmethod
    def __validareCifraControl(lista):
        control = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
        suma = 0
        for i in range(0, 12):
            suma = suma + control[i] * lista[i]
        rest = suma % 11
        if rest == 10:
            rest = 1
        if rest == lista[-1]:
            return True
        else:
            return False

    @staticmethod
    def validareCNP(n):
        lista = Persoana.__cnp2Lista(n)
        c1 = (Persoana.__validareSex(lista) != None)
        c2 = (Persoana.__validareDataNasterii(lista) != None)
        c3 = Persoana.__validareJudet(lista)
        c4 = Persoana.__validareCifraControl(lista)
        conditie = c1 and c2 and c3 and c4
        return conditie