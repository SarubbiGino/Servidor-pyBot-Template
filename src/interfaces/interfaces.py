from abc import abstractmethod
from dataclasses import dataclass
import datetime

@dataclass
class Juego:
    nombre: str
    fecha_de_inicio: datetime
    fecha_de_publicacion: datetime
    fecha_de_vencimiento: datetime


class Repositorio:
    @abstractmethod
    def dameElJuego(self, id: int) -> Juego:
        pass



class RepositorioFake(Repositorio):
    def __init__(self):
        self.juegos = []

    def crearJuego(self, nombre, fecha_de_inicio, fecha_de_publicacion, fecha_de_vencimiento):
        juego = Juego(nombre, fecha_de_inicio,fecha_de_publicacion, fecha_de_vencimiento)
        return juego

    def almacenarJuego(self, juego):
        self.juegos.append(juego)
        return juego
