class ClienteRepository:
    def __init__(self, listaCliente):
        self.__listaCliente=listaCliente

    @property
    def listaCliente(self):
        return self.__listaCliente
    @listaCliente.setter
    def listaCliente(self, listaCliente):
        self.__listaCliente=listaCliente
