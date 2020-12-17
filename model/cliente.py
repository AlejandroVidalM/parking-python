class Cliente():
    def __init__(self, nombre, apellidos):
        self.__nombre=nombre
        self.__apellidos=apellidos

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre=nombre

    @property
    def apellidos(self):
        return self.__apellidos
    @apellidos.setter
    def apellidos(self, apellidos):
        self.__apellidos=apellidos


