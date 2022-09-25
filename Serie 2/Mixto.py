from Publico import Publico
class Mixto(Publico):
    
    #Atributos:
    
    cantidadHombres= 300
    cantidadMujeres= 700
    
    #Métodos:
    
    def asignarDatosMixto(self):
        return  "Cantidad de Hombres: ", self.cantidadHombres, ", Cantidad de Mujeres: ", self.cantidadMujeres