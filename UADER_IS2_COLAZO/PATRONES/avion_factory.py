#implemente el patrón Abstract Factory, que se utiliza cuando se necesita crear 
#familias de objetos relacionados sin especificar sus clases concretas. Para eso, 
#creé una fábrica abstracta que genera distintos tipos de aviones con sus componentes, 
#como el cuerpo, las turbinas, las alas y el tren de aterrizaje.

import os

from taller_avion import Avion
class Motor:
    def crear_body(self):
        pass

    def crear_turbinas(self):
        pass

    def crear_alas(self):
        pass

    def crear_tren_aterrizaje(self):
        pass


class BoeingFactory:
    def crear_body(self):
        return "Cuerpo Boeing"

    def crear_turbinas(self):
        return ["Turbina Boeing 1", "Turbina Boeing 2"]

    def crear_alas(self):
        return ["Ala Boeing izquierda", "Ala Boeing derecha"]

    def crear_tren_aterrizaje(self):
        return "Tren de aterrizaje Boeing"


class AirbusFactory:
    def crear_body(self):
        return "Cuerpo Airbus"

    def crear_turbinas(self):
        return ["Turbina Airbus 1", "Turbina Airbus 2"]

    def crear_alas(self):
        return ["Ala Airbus izquierda", "Ala Airbus derecha"]

    def crear_tren_aterrizaje(self):
        return "Tren de aterrizaje Airbus"


class EnsambladorAvion:
    def __init__(self, factory):
        self.factory = factory

    def ensamblar_avion(self):
        avion = Avion()
        avion.body = self.factory.crear_body()
        avion.turbinas = self.factory.crear_turbinas()
        avion.alas = self.factory.crear_alas()
        avion.tren_aterrizaje = self.factory.crear_tren_aterrizaje()
        return avion
    
print("\n--- Usando Abstract Factory ---")
ensamblador_boeing = EnsambladorAvion(BoeingFactory())
avion_boeing = ensamblador_boeing.ensamblar_avion()
avion_boeing.especificaciones()

ensamblador_airbus = EnsambladorAvion(AirbusFactory())
avion_airbus = ensamblador_airbus.ensamblar_avion()
avion_airbus.especificaciones()
