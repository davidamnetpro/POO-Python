"""
Permite modelar una jerarquia de clases

permite compartir comportamiento comun entre jerarquia

Al padre se le conoce como super clase y al hijo como sub clase

Creamos nuevas clases a partir de otras para reutilizar código

"""

#Super clase
class Rectangulo:
    #Se inicializa con el constructor
    #Dando variables de instancia de base y altura
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    #Metodo que calcula el area
    def area(self):
        return self.base * self.altura
#Herencia del rectangulo
class Cuadrado(Rectangulo):

    def __init__(self, lado):
        #Obtiene una referencia directa de la super clase
        #Hereda la operacion * para calcular su area
        super().__init__(lado, lado)


if __name__ == '__main__':
    rectangulo = Rectangulo(base=3, altura=4)
    print(rectangulo.area())
    #Ejecuta el metodo area dentro de la clase cuadrado
    #Ya que heredo los atributos de la clase rectangulo
    cuadrado = Cuadrado(lado=5)
    print(cuadrado.area())