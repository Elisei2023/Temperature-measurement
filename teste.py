from Imports import *
from Adresa import *
from Camera import *
from Judet import *
from Locuinta import *
from MasuratoareTemperatura import *
from Persoana import *
from ProcesVerbal import *
from Sex import Sex
from TipActivitate import *

c1=Camera(3,3,2.6,True,"Caramida")
c2=Camera(3,3,2.8,True,"Caramida")
c3=Camera(4,3,3,True,"Caramida")
c4=Camera(3,4,2,True,"Caramida")

p1=Persoana(1930348235476,"Ion","Ionel",30,Sex.MALE,TipActivitate.HEAVY)
p2=Persoana(1990205366944,"Ilie","Danut",35,Sex.MALE,TipActivitate.HEAVY)
p3=Persoana(1910605366912,"Dana","Budeanu",40,Sex.FEMALE,TipActivitate.HEAVY)
p4=Persoana(2205062565986,"Ana","Karenina",78,Sex.FEMALE,TipActivitate.HEAVY)
p5=Persoana(4508967656574,"Ion","Iliescu",99,Sex.MALE,TipActivitate.HEAVY)
p6=Persoana(1930342345476,"Coco","Cristi",30,Sex.MALE,TipActivitate.SEDENTARY)
p7=Persoana(1992328956944,"Moco","Danut",35,Sex.MALE,TipActivitate.SEDENTARY)
p8=Persoana(1915455366912,"Daiel","Mihaita",80,Sex.FEMALE,TipActivitate.MODERATE)
p9=Persoana(2206756256986,"Ani","Ioana",58,Sex.FEMALE,TipActivitate.MODERATE)
p10=Persoana(4506766765674,"Maia","Iova",49,Sex.MALE,TipActivitate.SEDENTARY)
c1.adaugaPersoana(p6)
c1.adaugaPersoane(p1,p2,p3)
c2.adaugaPersoana(p6)
c3.adaugaPersoana(p8)
c4.adaugaPersoana(p10)

a1=Adresa("Budai Deleanu","13A",7,3,1,4,"Sibiu","Sibiu",400400)
mtCristi=MasuratoareTemperatura(a1,24.5,22.5,19.5,19)
print(mtCristi)
l=Locuinta(a1,c1,c2,c3,c4)
print(l)
print(l.temperaturaReferinta())
politai=Persoana(1930348235476,"Garcea","Dorin",30,Sex.MALE,TipActivitate.HEAVY)
pv=ProcesVerbal(l,mtCristi,politai)
print(pv)
pv.toFile()
print(Adresa.getAdrese())
print(Camera.getCamera())
c1.insertFisier()