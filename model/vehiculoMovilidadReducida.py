from model.vehiculo import Vehiculo


class VehiculoMovilidadReducida(Vehiculo):
    def __init__(self, matricula):
        super().__init__(matricula)
        self.__matricula=matricula

    @property
    def matricula(self):
        return self.__matricula
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula=matricula

    def calcularPrecio(self, minutos):
        precioPorMinuto=0.1
        return super().calcularPrecio()*precioPorMinuto
