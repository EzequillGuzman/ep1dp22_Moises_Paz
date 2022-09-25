from Privado import Privado
class SociedadAnonima(Privado):
    
    #Atributos:
    
    nombreSa= "Javier Muñoz"
    representante = "Manuel López"
    representanteCorreo= "manuelgomenz@gmail.com"
    
    #Métodos:
    
    def asignarDatosSociedad(self):
      return  "Nombre SA: ", self.nombreSa, ", Representante: ", self.representante, ",Representante Correo: ", self.representanteCorreo
        
         