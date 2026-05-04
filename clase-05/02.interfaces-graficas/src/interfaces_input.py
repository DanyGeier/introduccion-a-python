import tkinter as tk

ventana = tk.Tk()

ventana.title("Mi primera App")
ventana.geometry("800x600")

entrada = tk.Entry(ventana)
entrada.pack()


def obtener_texto():
    texto = entrada.get() # Obtengo lo ingresado en el input
    print(f"Escribiste: {texto}")

boton = tk.Button(ventana, text="Enviar", command=obtener_texto)
boton.pack()

ventana.mainloop()