class PlazaAparcamiento():
    def __init__(self, numeroPlaza, estaLibre, cliente, fecha):
        self.__numeroPlaza=numeroPlaza
        self.__estaLibre=estaLibre
        self.__cliente=cliente
        self.__fecha=fecha
    def __init__(self, numeroPlaza, estaLibre):
        self.__numeroPlaza=numeroPlaza
        self.__estaLibre=estaLibre

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


    def __str__(self):
        return "numeroPlaza: "+ str(self.numeroPlaza)+", estaLibre: "+self.estaLibre+", cliente: "+self.cliente+", fecha: "+self.fecha

    def ocupar(self, cliente):
        if self.estaLibre:
            self.cliente=cliente
            return True
        else:
            return False


    def liberar(self, ):
        if self.estaLibre:
            return False
        else:
        #    self.cliente=Null
            return True






