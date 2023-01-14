from Imports import *

class MasuratoareTemperatura:
    def __init__(self,pAdresa,*temperaturi):     #functie cu numar variabil de parametrii
        oras=pAdresa.getOras()
        self.__temperaturiCamere=[]
        for t in temperaturi:
            self.__temperaturiCamere.append(t)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                          '58.0.3029.110 Safari/537.3'}
        city = oras.replace(" ", "+")
        city = city + " weather"
        res = requests.get(
            f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome'
            f'&ie=UTF-8',headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        wind = re.search("Vânt:\\s\\d*\\s*km/h", soup.getText()).group().strip()
        self.__vitezaVant = int(re.search("\\d+", wind).group())
        self.__stareMeteo = soup.select('#wob_dc')[0].getText().strip()
        self.__temperaturaExterna = soup.select('#wob_tm')[0].getText().strip()
        self.__umiditate = int(soup.select('#wob_hm')[0].getText().strip().removesuffix("%").strip())
        self.__dataCurenta=date.today()
        self.__time=datetime.now()

    def __repr__(self):
        a="Data: {} \n".format(self.__dataCurenta)
        b="Time: {} \n".format(self.__time.strftime("%H:%M:%S"))
        c="Temperatura externa este {}°C\n".format(self.__temperaturaExterna)
        d="Vantul bate cu {} km/h\n".format((self.__vitezaVant))
        e="Este {}\n".format(self.__stareMeteo)
        f="Umiditatea este de {}%\n".format(self.__umiditate)
        return a+b+c+d+e+f

    def getTemperaturiCamere(self):
        return self.__temperaturiCamere

    def getTemperaturaExterna(self):
        return self.__temperaturaExterna

    def getUmiditate(self):
        return self.__umiditate

    def getVitezaVant(self):
        return self.__vitezaVant

    def getData(self):
        return self.__dataCurenta

    def getTimp(self):
        return self.__time