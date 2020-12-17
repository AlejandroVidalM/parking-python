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
cliente1=Cliente("Luis Miguel", "Lopez")
vehiculo1=Motocicleta("1234ABC")

#listaParking=[parkingTurismo, parkingMoto, parkingMovReducida]
#filename = 'parkingDatabase'
#outfile = open(filename,'wb')
#pickle.dump(listaParking,outfile)
#outfile.close()

parkingMoto.ocuparPlaza(cliente1, vehiculo1, ticketRepository)
print(ticketRepository.listaTicket[0])

print(cliente1.nombre)
print(parkingMoto.listaPlazas[1].cliente)
