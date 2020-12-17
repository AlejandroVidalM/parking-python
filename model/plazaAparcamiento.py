from datetime import date
from datetime import datetime
class PlazaAparcamiento():
    def __init__(self, numeroPlaza, estaLibre, cliente, fecha, vehiculo):
        self.__numeroPlaza=numeroPlaza
        self.__estaLibre=estaLibre
        self.__cliente=cliente
        self.__fecha=fecha
        self.__vehiculo = vehiculo
    def __init__(self, numeroPlaza, estaLibre):
        self.__numeroPlaza=numeroPlaza
        self.__estaLibre=estaLibre
        self.__cliente=None
        self.__fecha=datetime.now()
        self.__vehiculo = None

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
    def cliente(self):
        return self.__cliente
    @cliente.setter
    def cliente(self, cliente):
        self.__cliente=cliente

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


    def __str__(self):
        return "numeroPlaza: "+ str(self.numeroPlaza)+", estaLibre: "+self.estaLibre+", cliente: "+self.cliente+", fecha: "+self.fecha

    def ocupar(self, cliente, vehiculo):
        if self.estaLibre:
            self.cliente=cliente
            self.vehiculo=vehiculo
            self.fecha=datetime.now()
            return True
        else:
            return False


    def liberar(self, ):
        if self.estaLibre:
            return False
        else:
            self.cliente=None
            self.vehiculo=None
            self.fecha=datetime.now()
            return True






