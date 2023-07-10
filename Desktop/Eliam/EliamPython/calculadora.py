from tkinter import Tk, Button, Text

class Interfaz():

    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora")
        
        self.pantalla=Text(ventana, state="disabled", width=40, height=3, background="orchid", foreground="white")
        self.pantalla.grid(column=0, row=0, columnspan=4)

        boton1 = Button(self.ventana, text=1, width=9, height=1, font=("Helvetica",15))
        boton1.grid(column=0, row=1)
        boton2 = Button(self.ventana, text=1, width=9, height=1, font=("Helvetica",15))
        boton2.grid(column=1, row=1)
        boton3 = Button(self.ventana, text=1, width=9, height=1, font=("Helvetica",15))
        boton3.grid(column=2, row=1)
        boton4 = Button(self.ventana, text=1, width=9, height=1, font=("Helvetica",15))
        boton4.grid(column=3, row=1)
        boton5 = Button(self.ventana, text=1, width=9, height=1, font=("Helvetica",15))
        boton5.grid(column=0, row=2)
        boton6 = Button(self.ventana, text=1, width=9, height=1, font=("Helvetica",15))
        boton6.grid(column=1, row=2)
        boton7 = Button(self.ventana, text=1, width=9, height=1, font=("Helvetica",15))
        boton7.grid(column=2, row=2)
        boton8 = Button(self.ventana, text=1, width=9, height=1, font=("Helvetica",15))
        boton8.grid(column=3, row=2)
        boton9 = Button(self.ventana, text=1, width=9, height=1, font=("Helvetica",15))
        boton9.grid(column=0, row=3)
        boton10 = Button(self.ventana, text=1, width=9, height=1, font=("Helvetica",15))
        boton10.grid(column=1, row=3)
        boton11 = Button(self.ventana, text=1, width=9, height=1, font=("Helvetica",15))
        boton11.grid(column=2, row=3)
        boton12 = Button(self.ventana, text=1, width=9, height=1, font=("Helvetica",15))
        boton12.grid(column=3, row=3)
        boton13 = Button(self.ventana, text=1, width=9, height=1, font=("Helvetica",15))
        boton13.grid(column=0, row=4)
        boton14 = Button(self.ventana, text=1, width=9, height=1, font=("Helvetica",15))
        boton14.grid(column=1, row=4)
        boton15 = Button(self.ventana, text=1, width=9, height=1, font=("Helvetica",15))
        boton15.grid(column=2, row=4)
        boton16 = Button(self.ventana, text=1, width=9, height=1, font=("Helvetica",15))
        boton16.grid(column=3, row=4)
        boton17 = Button(self.ventana, text=1, width=19, height=1, font=("Helvetica",15))
        boton17.grid(column=0, row=5, columnspan=4)




ventana_principal = Tk()
aplicacion = Interfaz(ventana_principal)
ventana_principal.mainloop()
