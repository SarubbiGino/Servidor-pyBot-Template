from abc import abstractmethod
from dataclasses import dataclass
from datetime import date




@dataclass
class Participante:
    id_participante: str
    nombre_usuario: str
    puntos_acumulados: int
    puede_ver_deseos_amigo: bool
    id_amigo: str
    lista_deseos: list[str]

@dataclass
class Juego:
    id_juego: str
    fecha_limite_para_admitir_participantes: date
    fecha_de_inicio_del_juego: date
    fecha_de_celebracion_del_juego: date
    participantes: list[Participante]

class Repositorio:
    @abstractmethod
    def guardar_juego(
            self,
            fecha_limite_para_admitir_participantes: date,
            fecha_de_inicio_del_juego: date,
            fecha_de_celebracion_del_juego: date):
        raise NotImplementedError

    @abstractmethod
    def agregar_participante(
            self,
            id_juego: str,
            nombre_usuario: str,
            puntos_acumulados: int = 0,
            puede_ver_deseos_amigo: bool = False,
            id_amigo: str = '',
            lista_deseos: list[str] = []):
        raise NotImplementedError
