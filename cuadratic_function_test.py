from customtkinter import *
import math


#  Definimos la clase:
class FuncionCuadratica():
    __coeficientes = []
    __discriminante = 0
    __valores_calculados = []
    
#  Definimos los métodos:
    
    def ingreso_dato(self, a, b, c):
        self.__coeficientes.append(a)
        self.__coeficientes.append(b)
        self.__coeficientes.append(c)
        return        
    
    def calcular_discriminante(self):
        self.__discriminante = self.__coeficientes[1]**2 - 4 * self.__coeficientes[0] * self.__coeficientes[2]
        return
    
    def evaluar_discriminante(self):
        if self.__discriminante == 0:
            self.__valores_calculados.append(-self.__coeficientes[1] / (2 * self.__coeficientes[0]))
        elif self.__discriminante > 0:
            self.__valores_calculados.append((-self.__coeficientes[1] + math.sqrt(self.__discriminante)) / (2 * self.__coeficientes[0]))
            self.__valores_calculados.append((-self.__coeficientes[1] - math.sqrt(self.__discriminante)) / (2 * self.__coeficientes[0]))
        else:
            pass
        return
    
    def mostrar_resultado(self):
        if len(self.__valores_calculados) == 0:
            label_resultado.configure(text='La ecuación no tiene solución real')
        elif len(self.__valores_calculados) == 1:
            label_resultado.configure(text=f'Valor de la raíz 1: {self.__valores_calculados[0]}')
        else: 
            label_resultado.configure(text=f'Valor de la raíz 1: {self.__valores_calculados[0]}\n Valor de la raíz 2: {self.__valores_calculados[1]}')
        return




# Definimos la ventana
app = CTk()
app.geometry("500x500")
app.title("Funcion Cuadratica")


# funciones
def calcular():
    try:
        a = float(textbox_A.get())
        b = float(textbox_B.get())
        c = float(textbox_C.get())
        
        if a != 0:
            ecuacion = FuncionCuadratica()
            ecuacion.ingreso_dato(a, b, c)
            ecuacion.calcular_discriminante()
            ecuacion.evaluar_discriminante()
            ecuacion.mostrar_resultado()
        else:
            raise ValueError("El coeficiente A no puede ser igual a 0")         
    except ValueError as e:
        label_resultado.configure(text=str(e))
   
def cancelar():
    label_resultado.configure(text='')
    textbox_A.delete(0, END)    
    textbox_B.delete(0, END)
    textbox_C.delete(0, END)
    



# label de la funcion cuadratica
label_funcion = CTkLabel(master=app, text='f(x) = ax² + bx + c', font=("arial", 30))
label_funcion.place(relx=0.5, rely=0.05, anchor="center")


# textboxes y sus respectivos labels
label_A = CTkLabel(app, text='Coeficiente A:')
label_A.place(relx=0.05, rely=0.15)
textbox_A = CTkEntry(master=app, placeholder_text='Introduzca el coeficiente A...', width=250)
textbox_A.place(relx=0.05, rely=0.2)

label_B = CTkLabel(app, text='Coeficiente B:')
label_B.place(relx=0.05, rely=0.3)
textbox_B = CTkEntry(master=app, placeholder_text='Introduzca el coeficiente B...',  width=250)
textbox_B.place(relx=0.05, rely=0.35)

label_C = CTkLabel(app, text='Coeficiente C:')
label_C.place(relx=0.05, rely=0.45)
textbox_C = CTkEntry(master=app, placeholder_text='Introduzca el coeficiente C...',  width=250)
textbox_C.place(relx=0.05, rely=0.5)


# label resultado
label_resultado = CTkLabel(master=app, text='', font=("arial", 18))
label_resultado.place(relx=0.5, rely=0.7, anchor="center")


# buttons
button_calcular = CTkButton(master=app, text='Calcular', command=calcular)
button_calcular.place(relx=0.3, rely=0.9, anchor="center")

button_cancelar = CTkButton(master=app, text='Cancelar', command=cancelar)
button_cancelar.place(relx=0.7, rely=0.9, anchor="center")


app.mainloop()
