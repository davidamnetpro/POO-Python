"""
La habilidad de tomar varias formas

Nos permiten cambiar el comportamiento de una super 
clase para adaptarlo a la subclase

"""

class Persona:

    def __init__(self, nombre):
        self.nombre = nombre
    #No recibe parametros
    #Forma en la que avanza una persona
    def avanza(self):
        print('Ando caminando')

#Hereda de la clase persona
class Ciclista(Persona):

    def __init__(self, nombre):
        #Inicializa a la super clase 
        super().__init__(nombre)
    #Forma en la que avanza una persona en bicicleta
    def avanza(self):
        print('Ando moviendome en mi bicicleta')

#Funcion que contiene todo el comportamiento
def main():
    persona = Persona('David')
    persona.avanza()

    ciclista = Ciclista('Daniel')
    ciclista.avanza()


if __name__ == '__main__':
    main()