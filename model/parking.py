from datetime import datetime

from model.plazaAparcamiento import PlazaAparcamiento
from model.ticket import Ticket


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

    def ocuparPlaza(self, cliente, vehiculo, ticketRepository):
        estado=False
        for i in self.listaPlazas:
            if i.estaLibre and estado!=True:
                i.ocupar(cliente, vehiculo)
                ticketRepository.listaTicket.append(Ticket(vehiculo, i))
                self.plazasLibres-=1
                estado=True
        return estado

    def calcularPrecio(self, fechaEntrada):
        fechaSalida=datetime.now()
        minutos = (fechaSalida - fechaEntrada).total_seconds() / 60.0
        



    def desocuparPlaza(self, matricula, numeroPlaza, pin, ticketRepository):
        for i in ticketRepository:
            if i.vehiculo.matricula==matricula and i.plazaAparcamiento.numeroPlaza==numeroPlaza and pin==i.pin:
                self.calcularPrecio(i.plazaAparcamiento.fecha)

    # def OcuparPlaza(self, cliente, vehiculo):
    #     estado=False
    #     i=0
    #     while i < self.plazasTotales or estado:
    #         if self.listaPlazas[i].estalibre:
    #             self.listaPlazas[i].ocupar(cliente, vehiculo)
    #             ticket=Ticket(vehiculo1,parkingMoto)
    #             self.plazasLibres-=1
    #             estado=True
    #     return estado

