# Thinker (es una libreria para crear intercaces graficas) GUI
# GUI -> Grpahical User Interface (interfaz gráfica)
# Es una libreria buildin (incorporada dentro del lenguaje)
# Set de componentes de interfaz gráfica (Ventanas, botones, campos de texto, etc...)

class Persona:
    """ Un molde para crear personas """

    def __init__(self, nombre, edad):
        """ El constructor: se usa cuando instancio una clase """
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        """ Un método: es una acción que la persona puede hacer """
        return f"Hola, soy {self.nombre} y tengo {self.edad} años"
    
# Creamos 2 instancias de persona a partir del molde
persona1 = Persona("Laura", 25)
persona2 = Persona("Eduymar", 20)

# Usar los objetos
print(persona1.presentarse()) # Hola soy Laura y tengo 25 años
print(persona2.presentarse()) # Hola soy Eduymar y tengo 20 años

