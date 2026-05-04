import tkinter as tk

ventana = tk.Tk()

ventana.title("Mi primera App")
ventana.geometry("800x600")

# Área de texto
texto = tk.Text(ventana, height=5, width=30)
texto.pack()

def obtener_todo():
    contenido = texto.get("1.0", tk.END) # Desde el inicio hasta fin 
    print(contenido)

boton = tk.Button(ventana, text="Ver texto", command=obtener_todo)
boton.pack()

ventana.mainloop()

# Gestión de Layout

# 1. pack(): Apilar widgets (arriba-abajo - izq-der)
# 2. grid(): Colocar en filas y columnas
# 3. place(): posición exacta (menos común)