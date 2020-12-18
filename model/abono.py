from datetime import datetime


class Abono():
    def __init__(self, numeroPlaza, pin, fecha, precio, tiempoCobro):
        self.__numeroPlaza=numeroPlaza
        #self.__pin=str(random.randrange(1000000)).zfill(6)
        self.__pin=pin
        self.__fecha=fecha
        self.__precio=precio
        self.__tiempoCobro=tiempoCobro

    def __init__(self, numeroPlaza, precio, tiempoCobro):
        self.__numeroPlaza=numeroPlaza
        #self.__pin=str(random.randrange(1000000)).zfill(6)
        self.__pin="pin"
        self.__fecha=datetime.now()
        self.__precio=precio
        self.__tiempoCobro=tiempoCobro

    @property
    def numeroPlaza(self):
        return self.__numeroPlaza
    @numeroPlaza.setter
    def numeroPlaza(self, numeroPlaza):
        self.__numeroPlaza=numeroPlaza

    @property
    def pin(self):
        return self.__pin
    @pin.setter
    def pin(self, pin):
        self.__pin=pin

    @property
    def fecha(self):
        return self.__fecha
    @fecha.setter
    def fecha(self, fecha):
        self.__fecha=fecha

    @property
    def tiempoCobro(self):
        return self.__tiempoCobro
    @tiempoCobro.setter
    def tiempoCobro(self, tiempoCobro):
        self.__tiempoCobroa=tiempoCobro

    @property
    def precio(self):
        return self.__precio
    @precio.setter
    def precio(self, precio):
        self.__precio=precio
