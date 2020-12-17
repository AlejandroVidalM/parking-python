import random


class Ticket():
    def __init__(self, vehiculo, plazaAparcamiento):
        self.__vehiculo=vehiculo
        self.__plazaAparcamiento=plazaAparcamiento
        self.__pin=str(random.randrange(1000000)).zfill(6)

    @property
    def vehiculo(self):
        return self.__vehiculo
    @vehiculo.setter
    def vehiculo(self, vehiculo):
        self.__vehiculo=vehiculo

    @property
    def plazaAparcamiento(self):
        return self.__plazaAparcamiento
    @plazaAparcamiento.setter
    def cliente(self, plazaAparcamiento):
        self.__plazaAparcamiento=plazaAparcamiento

    @property
    def pin(self):
        return self.__pin
    @pin.setter
    def cliente(self, pin):
        self.__pin=pin

    def __str__(self):
        fechaformateada=f"{self.plazaAparcamiento.fecha.day}/{self.plazaAparcamiento.fecha.month}/{self.plazaAparcamiento.fecha.year} {self.plazaAparcamiento.fecha.hour}:{self.plazaAparcamiento.fecha.minute}:{self.plazaAparcamiento.fecha.second}"
        return f"matricula: {self.vehiculo.matricula} - fecha: {fechaformateada} - numero de la plaza: {self.plazaAparcamiento.numeroPlaza}\nPIN: {self.pin}"
