class Cliente():
    def __init__(self, nombre, apellidos, cliente, fecha):
        self.__nombre=nombre
        self.__apellidos=apellidos
        self.__cliente=cliente
        self.__fecha=fecha

    @property
    def numeroPlaza(self):
        return self.__numeroPlaza
    @numeroPlaza.setter
    def numeroPlaza(self, numeroPlaza):
        self.__numeroPlaza=numeroPlaza

# class Cliente{
#     constructor(nombre, apellidos, fechaDeNacimiento, email, matricula){
#         this.nombre=nombre;
#         this.apellidos=apellidos;
#         this.fechaDeNacimiento=fechaDeNacimiento;
#         this.email=email;
#         this.matricula=matricula;
#     }
