import tkinter as tk

class Calculadora:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora")

        # Configurar la interfaz
        self.crear_widgets()
    
    def iniciar(self):
        """ Mostrar la ventana """
        self.ventana.mainloop()

    def crear_widgets(self):
        """ Crear todo los elementos visuales"""

        # Pantalla de resultados
        self.pantalla = tk.Entry(
            self.ventana,
            font=("Arial", 20),
            justify="right"
        )

        self.pantalla.grid(
            row=0, 
            column=0, 
            columnspan=4, 
            padx=5, 
            pady=5
        )

        # Botones números
        numeros = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"]
        ]

        # Guardar la operación actual
        self.operacion = ""

        # Crear Botones
        for fila_idx, fila in enumerate(numeros, start=1):
            print(fila)
            for col_idx, numero in enumerate(fila):
                print(numero)
                boton = tk.Button(
                    self.ventana, 
                    text=numero, 
                    font=("Arial", 18), 
                    command=lambda n=numero: self.al_presionar_boton(n)
                )
                
                boton.grid(
                    row=fila_idx, 
                    column=col_idx, 
                    padx=2, 
                    pady=2
                )

        # Botón limpiar

        boton_limpiar = tk.Button(
            self.ventana,
            text="C",
            font=("Arial", 18),
            command=self.limpiar
        )
        
        boton_limpiar.grid(
            row=5,
            column=0,
            columnspan=4,
            padx="2",
            pady="2"
        )

    def al_presionar_boton(self, valor):
        """ Manejar presión de botones"""
        if valor == "=":
            """ Cuando valor sea = """
            resultado = eval(self.operacion)
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(0, resultado)
            self.operacion = ""
        else:
            """ Cuando la operación diferente de = """
            self.operacion += valor
            self.pantalla.delete(0, tk.END) # Limpiar lo que haya
            self.pantalla.insert(0, self.operacion) # Dibujamos

    def limpiar(self):
        """ Limpiar pantalla """
        self.pantalla.delete(0, tk.END)
        self.operacion = ""


# Crear y ejecutar
ventana = tk.Tk()
app = Calculadora(ventana)
app.iniciar()