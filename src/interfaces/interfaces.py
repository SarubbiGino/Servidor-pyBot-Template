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

    @abstractmethod
    def guardarUnParticipante(self, nombreDeUsuario: str, puntosAcumuladosParaAdivinarListaDeRegalos: int, puedeVerListaDeRegalos: bool):
        
    
    @abstractmethod
    def almacenarJuego(self, juego: str, fecha_de_inicio: datetime, fecha_de_publicacion: datetime, fecha_de_vencimiento: datetime):
     
    
  