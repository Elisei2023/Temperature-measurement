from Imports import *

from enum import Enum
class Judet(Enum):
    ALBA=1
    ARAD=2
    ARGES=3
    BACAU=4
    BIHOR=5
    BISTRITA=6
    BOTOSANI=7
    BRASOV=8
    BRAILA=9
    BUCURESTI=10
    BUZAU=11
    CARASSEVERIN=12
    CALARASI=13
    CLUJ=14
    CONSTANTA=15
    COVASNA=16
    DAMBOVITA=17
    DOLJ=18
    GALATI=19
    GIURGIU=20
    GORJ=21
    HARGHITA=22
    HUNEDOARA=23
    IALOMITA=24
    IASI=25
    ILFOV=26
    MARAMURES=27
    MEHEDINTI=28
    MURES=29
    NEAMT=30
    OLT=31
    PRAHOVA=32
    SATUMARE=33
    SALAJ=34
    SIBIU=38
    SUCEAVA=36
    TELEORMAN=37
    TIMIS=35
    TULCEA=39
    VASLUI=40
    VALCEA=41
    VRANCEA=42

    @staticmethod
    def stringToJudet(string):
        if string.upper()=="ARAD":
            return Judet.ARAD
        elif string.upper()=="ALBA":
            return Judet.ALBA
        elif string.upper() == "ARGES":
            return Judet.ARGES
        elif string.upper() == "BACAU":
            return Judet.BACAU
        elif string.upper() == "BIHOR":
            return Judet.BIHOR
        elif string.upper() == "BUZAU":
            return Judet.BUZAU
        elif string.upper() == "BRAILA":
            return Judet.BRAILA
        elif string.upper() == "BRASOV":
            return Judet.BRASOV
        elif string.upper() == "BISTRITA":
            return Judet.BISTRITA
        elif string.upper() == "BOTOSANI":
            return Judet.BOTOSANI
        elif string.upper() == "BUCURESTI":
            return Judet.BUCURESTI
        elif string.upper() == "CLUJ":
            return Judet.CLUJ
        elif string.upper() == "COVASNA":
            return Judet.COVASNA
        elif string.upper() == "CALARASI":
            return Judet.CALARASI
        elif string.upper() == "CONSTANTA":
            return Judet.CONSTANTA
        elif string.upper() == "CARASSEVERIN":
            return Judet.CARASSEVERIN
        elif string.upper() == "DOLJ":
            return Judet.DOLJ
        elif string.upper() == "DAMBOVITA":
            return Judet.DAMBOVITA
        elif string.upper() == "GORJ":
            return Judet.GORJ
        elif string.upper() == "GALATI":
            return Judet.GALATI
        elif string.upper() == "GIURGIU":
            return Judet.GIURGIU
        elif string.upper() == "HARGHITA":
            return Judet.HARGHITA
        elif string.upper() == "HUNEDOARA":
            return Judet.HUNEDOARA
        elif string.upper() == "IASI":
            return Judet.IASI
        elif string.upper() == "ILFOV":
            return Judet.ILFOV
        elif string.upper() == "IALOMITA":
            return Judet.IALOMITA
        elif string.upper() == "MURES":
            return Judet.MURES
        elif string.upper() == "MARAMURES":
            return Judet.MARAMURES
        elif string.upper() == "MEHEDINTI":
            return Judet.MEHEDINTI
        elif string.upper() == "NEAMT":
            return Judet.NEAMT
        elif string.upper() == "OLT":
            return Judet.OLT
        elif string.upper() == "PRAHOVA":
            return Judet.PRAHOVA
        elif string.upper() == "SALAJ":
            return Judet.SALAJ
        elif string.upper() == "SIBIU":
            return Judet.SIBIU
        elif string.upper() == "SUCEAVA":
            return Judet.SUCEAVA
        elif string.upper() == "SATUMARE":
            return Judet.SATUMARE
        elif string.upper() == "TIMIS":
            return Judet.TIMIS
        elif string.upper() == "TULCEA":
            return Judet.TULCEA
        elif string.upper() == "TELEORMAN":
            return Judet.TELEORMAN
        elif string.upper() == "VASLUI":
            return Judet.VASLUI
        elif string.upper() == "VALCEA":
            return Judet.VALCEA
        elif string.upper() == "VRANCEA":
            return Judet.VRANCEA

