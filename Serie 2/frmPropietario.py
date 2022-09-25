import tkinter
from tkinter import *
from tkinter import ttk
from Propietario import Propietario


#crear ventana 
ventana = Tk()
ventana.title = "Ejemplo tablas y objetos"
ventana.geometry("500x500")

tabla = ttk.Treeview(ventana, columns=("col1","col2"))

#instanciar la clase para asignar valores a los atributos y utilizar los métodos

listaPropietario = []  
    
def guardaDatos():
    propietario = Propietario()
    #asignar los valores a los atributos
    propietario.propietarioId = int(txt_propietarioId.get())
    propietario.propietarioNombre = txt_propietarioNombre.get()
    propietario.propietarioTelefono = txt_propietarioTelefono.get()
    
    
    
    #agregando el estudiante a la lista
    listaPropietario.append(propietario)
    generarTabla()
    limpiarCajasTexto() 
    
    
    

def generarTabla():
    #limpiar o borrar las filas antes de cargar de nuevo
    for fila in tabla.get_children():
        tabla.delete(fila)
        
    #establecer el tamaño de las columnas
    tabla.column("#0", width=125)
    tabla.column("col1", width=125)
    tabla.column("col2", width=125)
   
   
    
    tabla.heading("#0", text="Propietario Id", anchor=CENTER)
    tabla.heading("col1", text="Propietario Nombre", anchor=CENTER)
    tabla.heading("col2", text="Propietario Teléfono", anchor=CENTER)
    
    
    
    #ciclo para pasar los elementos de lista de estudiantes
    for registro in listaPropietario:
        tabla.insert("",END, text=registro.propietarioId, values=(registro.propietarioNombre, registro.propietarioTelefono))
    
    tabla.pack(fill= tkinter.X)
    
def limpiarCajasTexto():
    #borrar el contenido de los controles Entry
    txt_propietarioId.delete(0,"end")
    txt_propietarioNombre.delete(0,"end")
    txt_propietarioTelefono.delete(0,"end")
    
    #pone el foco a este elemento
    txt_propietarioId.focus_set()
    
fuente = ("Arial", 16)

    #Nombres que se le darán a los label y cajas de texto:
lbl_titulo = Label(ventana, text="Clase Propietario", font=("Arial","20"))

lbl_propietarioId = Label(ventana, text="Propietario Id:", font = fuente)
txt_propietarioId = Entry(ventana, font= fuente)

lbl_propietarioNombre = Label(ventana, text="Propietario Nombre:", font = fuente)
txt_propietarioNombre = Entry(ventana, font= fuente)

lbl_propietarioTelefono = Label(ventana, text="Propietario Teléfono:", font = fuente)
txt_propietarioTelefono = Entry(ventana, font= fuente)




btn_guardar = Button(ventana, text="Guardar datos", command=guardaDatos, font=fuente)



lbl_titulo.pack()
lbl_propietarioId.pack(anchor = tkinter.W)
txt_propietarioId.pack(fill = tkinter.X)

lbl_propietarioNombre.pack(anchor = tkinter.W)
txt_propietarioNombre.pack(fill = tkinter.X)

lbl_propietarioTelefono.pack(anchor = tkinter.W)
txt_propietarioTelefono.pack(fill = tkinter.X)




btn_guardar.pack(fill = tkinter.X)




ventana.mainloop()

 


        
