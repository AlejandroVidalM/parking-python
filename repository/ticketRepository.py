class TicketRepository:
    def __init__(self, listaTicket):
        self.__listaTicket=listaTicket

    @property
    def listaTicket(self):
        return self.__listaTicket
    @listaTicket.setter
    def listaTicket(self, listaTicket):
        self.__listaTicket=listaTicket
