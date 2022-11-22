import random
import logging as log
from abc import ABC


class Instrumento(ABC):
    def __init__(self, nombre,tipo, afinado = False):
        self._nombre = nombre
        self._tipo = tipo
        self.afinido = afinado

    @property
    def nombre(self):
        return self._nombre

    @property
    def tipo(self):
        return self._tipo

    def afinar(self):
        self.afinado = random.choice([True, False])

    def tocar(self):
        try:
            if self.afinado == True:
                log.debug('El instrumento {} está tocando afinado'.format(self.nombre))
            else:
                raise Exception
        except Exception as e:
            log.info('El instrumento {} no está afinado. Así no se puede tocar'.format(self.nombre))
            self.afinar()
            self.tocar()

class Guitarra(Instrumento):
    def __init__(self,nombre, tipo, num_cuerdas):
        self._nombre = nombre
        self._tipo = nombre
        self.num_cuerdas = num_cuerdas # la dejo pública por si quiero cambiar el número de cuerdas (se pueden romper
        # y que siga tocando)


class Guitarra_electrica(Guitarra):
    def __init__(self,nombre, tipo, num_cuerdas, potencia):
        self._nombre = nombre
        self._tipo = nombre
        self.num_cuerdas = num_cuerdas
        self.potencia = potencia # la dejo pública porque depende del ampli

class Piano(Instrumento):
    def __init__(self,nombre, tipo, num_teclas):
        self._nombre = nombre
        self._tipo = nombre
        self._num_teclas = num_teclas

class Tambor(Instrumento):
    def __init__(self,nombre, tipo, diametro):
        self._nombre = nombre
        self._tipo = tipo
        self._diametro = diametro

    def aporrear(self):
        pass

class Banda:
    #ya pondremos un __init__ si queremos (o no)
    def crear_banda(self):
        guitarra = Guitarra('nombre_guitarra', 'tipo_cuerda', '6')
        guitarra_electrica = Guitarra_electrica('nombre_guitarra', 'tipo_eletrófono', '6', '100')
        tambor = Tambor('nombre_tambor', 'Percusión', '40')
        piano = Piano('nombre_piano', 'tipo_cuerda', '88')
        lista_banda = [guitarra, guitarra_electrica, tambor, piano]
        return lista_banda

    def iniciar_concierto(self, lista_instrumento):
        for instrumento in lista_instrumento:
            instrumento.afinar()
        for instrumento in lista_instrumento:
            instrumento.tocar()

mi_banda = Banda()
mi_banda.iniciar_concierto(mi_banda.crear_banda())
print('termina el concierto')