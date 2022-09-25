from CentroEducativo import CentroEducativo

class Publico(CentroEducativo):
    
     #Atributos:
     
    fechaCreacion= "12 de septiembre 2022"
    tipo="Tipo federación"
    descripcion= "Infraestructura de calidad"
    
    #Métodos:
    
    def asignarDatosPublico(self):
     return  "Fecha de Creación: ", self.fechaCreacion, ", Tipo: ", self.tipo, ",Descripción: ", self.descripcion
