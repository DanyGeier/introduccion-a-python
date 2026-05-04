import tkinter as tk

ventana = tk.Tk()

ventana.title("Mi primera App")
ventana.geometry("800x600")

def al_presionar():
    print("Presionaste el botón!")

boton = tk.Button(ventana, text="Presione aquí", command=al_presionar)
boton.pack()

ventana.mainloop()