import string
from tkinter import Tk,Label,Button,Entry, Frame

class Textos(Frame):

    def __init__(self, master=None):
        super().__init__(master,width=520, height=320)
        self.master = master
        self.pack()
        self.create_widgets()

    def fSuma(self):
        self.n1=self.txtTexto1.get()
        self.n2=self.txtTexto2.get()
        self.n3=self.txtTexto3.get()
        self.n4=self.txtTexto4.get()
        r=(self.n1)+(self.n2)+(self.n3)+(self.n4)
        self.longa= len(r)

        self.txtNum3.delete(0,'end')
        self.txtNum3.insert(0,self.longa)
        
        dato=(self.n3) + (self.n4)
        self.result = len(dato)
        
    def calcularMenor(self):
        if (self.n1 < self.n2) and (self.n1 < self.n3) and (self.n1 < self.n4):
            self.txtNum4.delete(0,'end')
            self.txtNum4.insert(0,self.n1)
        elif (self.n2 < self.n1) and (self.n2 < self.n3) and (self.n2 < self.n4):
            self.txtNum4.delete(0,'end')
            self.txtNum4.insert(0,self.n2)
        elif (self.n3 < self.n1) and (self.n3 < self.n2) and (self.n3 < self.n4):
            self.txtNum4.delete(0,'end')
            self.txtNum4.insert(0,self.n3)
        else:
            self.txtNum4.delete(0,'end')
            self.txtNum4.insert(0,self.n4)   
            
            
    def calcularMayorMenor(self):
        if (self.longa > self.result):
            self.txtNum5.delete(0,'end')
            self.txtNum5.insert(0,self.result)
        elif (self.longa < self.result):
            self.txtNum5.delete(0,'end')
            self.txtNum5.insert(0,self.result)
        else:
            self.txtNum5.delete(0,'end')
            self.txtNum5.insert(0,self.result)
        
             
    def create_widgets(self):
        self.lblTexto1 = Label(self,text="Primer Texto: ",bg="yellow")
        self.txtTexto1=Entry(self,bg="pink")
        self.lblTexto2 = Label(self,text="Segundo Texto: ",bg="yellow")
        self.txtTexto2=Entry(self,bg="pink")
        self.lblTexto3 = Label(self,text="Tercer Texto: ",bg="yellow")
        self.txtTexto3=Entry(self,bg="pink")
        self.lblTexto4 = Label(self,text="Cuarto Texto: ",bg="yellow")
        self.txtTexto4=Entry(self,bg="pink")
        
        #Colores y diseños de los botones y cajas de rsultado
        self.btn1=Button(self,text="Sumar", command=self.fSuma)
        self.lblNum3 = Label(self,text="Suma_Longitudes: ",bg="yellow")
        self.txtNum3=Entry(self,bg="cyan")
        self.btn2=Button(self,text="Menor", command=self.calcularMenor)
        self.lblNum4 = Label(self,text="Menor_Caracteres: ",bg="yellow")
        self.txtNum4=Entry(self,bg="cyan")
        self.btn3=Button(self,text="Mayor,Menor,Igual", command=self.calcularMayorMenor)
        self.lblNum5 = Label(self,text="Mayor,Menor,Igual:",bg="yellow")
        self.txtNum5=Entry(self,bg="cyan")
        
        #Tamaños y dimensiones de las cajas de textos
        self.lblTexto1.place(x=10,y=10,width=100, height=30)
        self.txtTexto1.place(x=120,y=10,width=100, height=30)
        self.lblTexto2.place(x=10,y=50,width=100, height=30)
        self.txtTexto2.place(x=120,y=50,width=100, height=30)
        self.lblTexto3.place(x=10, y=90,width=100,height=30) 
        self.txtTexto3.place(x=120,y=90,width=100, height=30)
        self.lblTexto4.place(x=10,y=130,width=100, height=30)
        self.txtTexto4.place(x=120,y=130,width=100, height=30)
        
        #Tamaños y dimensiones de los resultados
        self.btn1.place(x=230,y=50,width=80, height=30)
        self.lblNum3.place(x=10,y=170,width=100, height=30)
        self.txtNum3.place(x=120,y=170,width=100, height=30)
        self.btn2.place(x=230,y=90,width=80, height=30)
        self.lblNum4.place(x=10,y=210,width=100, height=30)
        self.txtNum4.place(x=120,y=210,width=100, height=30)
        self.btn3.place(x=230,y=130,width=110, height=30)
        self.lblNum5.place(x=10,y=250,width=105, height=30)
        self.txtNum5.place(x=120,y=250,width=100, height=30)


problema1 = Tk()
problema1.wm_title("Suma_Long")
app = Textos(problema1) 
app.mainloop()