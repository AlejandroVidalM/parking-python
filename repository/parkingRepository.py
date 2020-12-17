class ParkingRepository:
    def __init__(self, listaParking):
        self.__listaParking=listaParking


    @property
    def listaParking(self):
        return self.__listaParking
    @listaParking.setter
    def listaParking(self, listaParking):
        self.__listaParking=listaParking
