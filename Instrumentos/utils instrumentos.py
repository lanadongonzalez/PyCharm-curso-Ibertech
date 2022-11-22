#un módulo para pedir que el usuario meta info
from abc import  ABC


class Pregunta_instrumentos(ABC):
    def pide_nombre(self):
        pass

    def pide_tipo(self):
        pass

    def pide_num_cuerdas(self):
        pass

    def pide_potencia(self):
        pass

    def pide_num_teclas(self):
        pass

    def pide_diametro(self):
        pass