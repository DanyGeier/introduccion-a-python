import tkinter as tk

ventana = tk.Tk()

ventana.title("Mi primera App")
ventana.geometry(("800x600"))

# Creamos la etiqueta
etiqueta = tk.Label(ventana, text="Hola mundo")
etiqueta.pack() # Mostrar la etiqueta en la interfaz

ventana.mainloop()