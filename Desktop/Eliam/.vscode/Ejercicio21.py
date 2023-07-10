import tkinter as tk

class AdministradorAlumnosGUI:
    def __init__(self):
        self.nombres = []
        self.notas = []

        self.root = tk.Tk()
        self.root.title("Administrador de Alumnos")

        self.button_cargar = tk.Button(self.root, text="Cargar Alumno", command=self.mostrar_ventana_carga)
        self.button_cargar.pack()

        self.button_listar = tk.Button(self.root, text="Listar Alumnos", command=self.listar_alumnos)
        self.button_listar.pack()

        self.button_aprobados = tk.Button(self.root, text="Mostrar Aprobados", command=self.mostrar_alumnos_aprobados)
        self.button_aprobados.pack()

        self.button_salir = tk.Button(self.root, text="Salir", command=self.root.quit)
        self.button_salir.pack()

    def mostrar_ventana_carga(self):
        ventana_carga = tk.Toplevel(self.root)
        ventana_carga.title("Carga de Alumno")

        label_nombre = tk.Label(ventana_carga, text="Nombre:")
        label_nombre.pack()
        entry_nombre = tk.Entry(ventana_carga)
        entry_nombre.pack()

        label_nota = tk.Label(ventana_carga, text="Nota:")
        label_nota.pack()
        entry_nota = tk.Entry(ventana_carga)
        entry_nota.pack()

        button_guardar = tk.Button(ventana_carga, text="Guardar", command=lambda: self.cargar_alumno(entry_nombre.get(), entry_nota.get(), ventana_carga))
        button_guardar.pack()

    def cargar_alumno(self, nombre, nota, ventana_carga):
        if nombre and nota:
            self.nombres.append(nombre)
            self.notas.append(float(nota))
            ventana_carga.destroy()
            self.mostrar_mensaje("Carga exitosa", "Alumno cargado exitosamente.")
        else:
            self.mostrar_mensaje("Error", "Debes ingresar un nombre y una nota.")

    def mostrar_mensaje(self, titulo, mensaje):
        ventana_mensaje = tk.Toplevel(self.root)
        ventana_mensaje.title(titulo)

        label_mensaje = tk.Label(ventana_mensaje, text=mensaje)
        label_mensaje.pack()

        button_cerrar = tk.Button(ventana_mensaje, text="Cerrar", command=ventana_mensaje.destroy)
        button_cerrar.pack()

    def listar_alumnos(self):
        lista_alumnos = ""
        for i in range(len(self.nombres)):
            lista_alumnos += f"Alumno: {self.nombres[i]}, Nota: {self.notas[i]}\n"
        self.mostrar_mensaje("Listado de Alumnos", lista_alumnos)

    def mostrar_alumnos_aprobados(self):
        alumnos_aprobados = ""
        for i in range(len(self.nombres)):
            if self.notas[i] >= 7:
                alumnos_aprobados += f"Alumno: {self.nombres[i]}, Nota: {self.notas[i]}\n"
        if alumnos_aprobados == "":
            alumnos_aprobados = "No hay alumnos con notas mayores o iguales a 7."
        self.mostrar_mensaje("Alumnos Aprobados", alumnos_aprobados)

    def run(self):
        self.root.mainloop()

# Crear instancia de la clase AdministradorAlumnosGUI
admin_alumnos_gui = AdministradorAlumnosGUI()

# Iniciar la aplicación
admin_alumnos_gui.run()
