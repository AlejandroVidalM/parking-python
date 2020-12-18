from model.parking import *
from model.cliente import *
from model.vehiculo import *
from model.motocicleta import *
from model.ticket import *
from repository.ticketRepository import *
import pickle

parkingTurismo=Parking(14)
parkingMoto=Parking(3)
parkingMovReducida=Parking(3)
ticketRepository=TicketRepository([])
vehiculo1=Motocicleta("1234ABC")
cliente1=Cliente("Luis Miguel", "Lopez", "dni", vehiculo1)

#listaParking=[parkingTurismo, parkingMoto, parkingMovReducida]
#filename = 'parkingDatabase'
#outfile = open(filename,'wb')
#pickle.dump(listaParking,outfile)
#outfile.close()

parkingMoto.ocuparPlaza(vehiculo1, ticketRepository)
print(ticketRepository.listaTicket[0])
input("Espera")
print(parkingMoto.listaPlazas[0].estaLibre)
parkingMoto.desocuparPlaza("1234ABC", 1, "pin", ticketRepository)

print(parkingMoto.listaPlazas[0].estaLibre)

print(parkingMoto.listaPlazas[0].vehiculo)
