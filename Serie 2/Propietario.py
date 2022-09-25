from Privado import Privado
class Propietario(Privado):
    #Atributos:
    
    propietarioId= 0
    propietarioNombre= ""
    propietarioTelefono= ""
    
    
    
    #Métodos: 
    
    def asignarDatosPropietario(self):
        print("Propietario ID: ", self.propietarioId, ", Propietario Nombre: ", self.propietarioNombre, ", Propietario Telefono: ", self.propietarioTelefono)


    
        