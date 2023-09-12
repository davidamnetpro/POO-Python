"""
Permite agrupar datos y su comportamiento

Controla acceso a dichos datos

Previene modificaciones no autorizadas

"""
# Estructura de la clase
class CasillaDeVotacion:

    def __init__(self, identificador, pais):
        self.__identificador = identificador
        self.__pais = pais
        self.__region = None
    #Acceder al valor a travez de decoradores getter
    @property
    def region(self):
        return print(self.__region)
    #Permite modificar la informacion a travez de decoradores setter
    @region.setter
    def region(self, region):
        if region in self.__pais:
            self.__region = region
        else:
            raise ValueError(print(f"la region {region} no es valida en {self.__pais}"))

#Uso
#Definicion de informacion a travez de un diccionario
#Se estipula el codigo, pais, y la region que se encuentra dentro de ese pais.
#Si se quiere acceder a la region tiene que pertenecer al pais de lo contraio
#Nos arroja error
casilla = CasillaDeVotacion(123, ["Ciudad de Mexico", "Morelos"])

casilla.region = "Ciudad de Mexico"
casilla.region
