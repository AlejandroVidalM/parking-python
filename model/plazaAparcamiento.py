from datetime import date
from datetime import datetime
class PlazaAparcamiento():
    def __init__(self, numeroPlaza, estaLibre, fecha, vehiculo, estaAbonado):
        self.__numeroPlaza=numeroPlaza
        self.__estaLibre=estaLibre
        self.__fecha=fecha
        self.__vehiculo = vehiculo
        self.__estaAbonado=estaAbonado
    def __init__(self, numeroPlaza):
        self.__numeroPlaza=numeroPlaza
        self.__estaLibre=True
        self.__cliente=None
        self.__fecha=datetime.now()
        self.__vehiculo = None
        self.__estaAbonado=False

    @property
    def numeroPlaza(self):
        return self.__numeroPlaza
    @numeroPlaza.setter
    def numeroPlaza(self, numeroPlaza):
        self.__numeroPlaza=numeroPlaza

    @property
    def estaLibre(self):
        return self.__estaLibre
    @estaLibre.setter
    def estaLibre(self, estaLibre):
        self.__estaLibre=estaLibre

    @property
    def fecha(self):
        return self.__fecha
    @fecha.setter
    def fecha(self, fecha):
        self.__fecha=fecha

    @property
    def vehiculo(self):
        return self.__vehiculo
    @vehiculo.setter
    def vehiculo(self, vehiculo):
        self.__vehiculo=vehiculo

    @property
    def estaAbonado(self):
        return self.__estaAbonado
    @estaAbonado.setter
    def estaAbonado(self, estaAbonado):
        self.__estaAbonado=estaAbonado


    def __str__(self):
        return "numeroPlaza: "+ str(self.numeroPlaza)+", estaLibre: "+self.estaLibre+", fecha: "+self.fecha

    def ocupar(self, vehiculo):
        if self.estaLibre:
            self.vehiculo=vehiculo
            self.fecha=datetime.now()
            self.estaLibre=False
            return True
        else:
            return False


    def liberar(self):
        vehiculo=None
        if self.estaLibre:
            return False
        else:
            self.vehiculo=vehiculo
            self.fecha=datetime.now()
            self.estaLibre=True
            return True






