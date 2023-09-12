"""
La clase define el molde, es una forma en la que nosotros podemos definir
cuales son las caracteristicas que esta clase va a tener y estas caracteristicas 
las van a poder utilizar todas las instacias de clase

"""

#Definicion
class Persona:
    #Definicion de funciones y caracteristicas
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saluda(self, otra_persona):
        return print(f"Hola {otra_persona.nombre}, me llamo {self.nombre}")

#Uso
david = Persona("David",30)
erika = Persona("Erika", 25)

#Utiliza el modelo para generar la informacion
# Y utiliza la informacion de la instacias para los metodos
david.saluda(erika)