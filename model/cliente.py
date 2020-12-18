class Cliente():
    def __init__(self, nombre, apellidos, dni, vehiculo, nTarjeta, abono, email):
        self.__nombre=nombre
        self.__apellidos=apellidos
        self.__dni=dni
        self.__vehiculo=vehiculo
        self.__nTarjeta=nTarjeta
        self.__abono=abono
        self.__email=email

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

    @property
    def dni(self):
        return self.__dni
    @dni.setter
    def dni(self, dni):
        self.__dni=dni

    @property
    def vehiculo(self):
        return self.__vehiculo
    @vehiculo.setter
    def vehiculo(self, vehiculo):
        self.__vehiculo=vehiculo

    @property
    def nTarjeta(self):
        return self.__nTarjeta
    @nTarjeta.setter
    def nTarjeta(self, nTarjeta):
        self.__nTarjeta=nTarjeta

    @property
    def abono(self):
        return self.__abono
    @abono.setter
    def abono(self, abono):
        self.__abono=abono

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email):
        self.__email=email



