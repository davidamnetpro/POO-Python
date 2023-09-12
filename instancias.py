"""
Las instancias son los objetos que producen las clases,
la maquina que crea las botellas es la clase y cada una de las botellas
son la instancia de esa clase osea cada botella.

Cuando se crea una instancia, se ejecuta el metodo __init__

Todos los metodos de una clase reciben implicitamente
como primer parametro self

Los atributos de la clase permiten:

1. Representar datos
2. Procedimientos para interactuar con los mismos metodos
3. Mecanismos para esconder la representacion interna

Se accede a los atributos con la notacion de punto

Puede tener atributos privados. Por convencion se comienza con _
"""
#Ejemplo calculo de distancia entre coordenadas x,y
class Coordenada:
    #Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otra_coordendada):
        x_diff = (self.x - otra_coordendada.x)**2
        y_diff = (self.y - otra_coordendada.y)**2

        return (x_diff + y_diff)**0.5


if __name__ == '__main__':
    coord_1 = Coordenada(3, 30)
    coord_2 = Coordenada(4, 8)

    #print(coord_1.distancia(coord_2))
    print(isinstance(3, Coordenada))#Verifica si la instancia existe