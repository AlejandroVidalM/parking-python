class Vehiculo():
    def __init__(self, matricula):
        self.__matricula=matricula

    @property
    def matricula(self):
        return self.__matricula
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula=matricula

    def calcularPrecio(self, minutos):
        return minutos
