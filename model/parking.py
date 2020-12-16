from model.plazaAparcamiento import PlazaAparcamiento


class Parking():
    def __init__(self, plazasTotales):
        self.__plazasTotales=plazasTotales
        self.__listaPlazas=[]
        self.__plazasLibres=plazasTotales
        self.crearListaPlazas()

    def crearListaPlazas(self):
        for i in range(self.plazasTotales):
            self.listaPlazas.append(PlazaAparcamiento(i+1,True))
    @property
    def listaPlazas(self):
        return self.__listaPlazas
    @listaPlazas.setter
    def listaPlazas(self, listaPlazas):
        self.__listaPlazas=listaPlazas

    @property
    def plazasTotales(self):
        return self.__plazasTotales
    @plazasTotales.setter
    def plazasTotales(self, plazasTotales):
        self.__plazasTotales=plazasTotales

    @property
    def plazasLibres(self):
        return self.__plazasLibres
    @plazasLibres.setter
    def plazasLibres(self, plazasLibres):
        self.__plazasLibres=plazasLibres
