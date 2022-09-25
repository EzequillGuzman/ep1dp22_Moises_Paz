from Publico import Publico
class Ungenero(Publico):
    
    #Atributos:
    
    genero= ""
    cantidadEstudiantes= 0
    
    #Métodos:
    
    def asignarDatosUngenero(self):
       return  "Genero: ", self.genero, ", Cantidad de Estudiantes: ", self.cantidadEstudiantes