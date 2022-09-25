from CentroEducativo import CentroEducativo
class Privado(CentroEducativo):
    
    #Atributos:
    
    cantidadHombres= 0
    cantidadMujeres=0 
    
    
    #Métodos:
    
    def asignarDatosPrivado(self):
        return  "Cantidad de Hombres: ", self.cantidadHombres, ", Cantidad de Mujeres: ", self.cantidadMujeres