from customtkinter import *

# instancia del objeto
app = CTk()
app.geometry("500x500")
app.title("Funcion Cuadratica")

# funciones
def calcular(a, b, c):
    label_resultado.config(text='¡Nuevo texto!')
    return

def cancelar():
    label_resultado.config(text='')
    return


# label de la funcion cuadratica
label_funcion = CTkLabel(master=app, text='f(x) = ax² + bx + c', font=("arial", 30))
label_funcion.place(relx=0.5, rely=0.045, anchor="center")


# textboxes y sus respectivos labels
label_A = CTkLabel(app, text="Coeficiente A:")
label_A.place(relx=0.05, rely=0.15)
textbox_A = CTkEntry(master=app, placeholder_text='Introduzca el coficiente A...', width=250)
textbox_A.place(relx=0.05, rely=0.2)

label_B = CTkLabel(app, text="Coeficiente B:")
label_B.place(relx=0.05, rely=0.3)
textbox_B = CTkEntry(master=app, placeholder_text='Introduzca el coficiente B...',  width=250)
textbox_B.place(relx=0.05, rely=0.35)

label_C = CTkLabel(app, text="Coeficiente C:")
label_C.place(relx=0.05, rely=0.45)
textbox_C = CTkEntry(master=app, placeholder_text='Introduzca el coficiente C...',  width=250)
textbox_C.place(relx=0.05, rely=0.5)


# label resultado
label_resultado = CTkLabel(master=app, text='')
label_resultado.place(relx=0.5, rely=0.7, anchor="center")

# buttons
button_calcular = CTkButton(master=app, text='Calcular', command=lambda: calcular(textbox_A, textbox_B, textbox_C))
button_calcular.place(relx=0.3, rely=0.9, anchor="center")

button_cancelar = CTkButton(master=app, text='Cancelar', command=lambda: cancelar)
button_cancelar.place(relx=0.7, rely=0.9, anchor="center")




app.mainloop()