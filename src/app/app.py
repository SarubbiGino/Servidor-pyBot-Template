from interfaces import Repositorio
from dataclasses import dataclass
from datetime import date
from datetime import datetime, timedelta


def sumar_cinco_dias():
    fecha_actual = datetime.today()
    fecha_futura = fecha_actual + timedelta(days=5)
    return fecha_futura


def sumar_diez_dias():
    fecha_actual = datetime.today()
    fecha_futura = fecha_actual + timedelta(days=10)
    return fecha_futura


DIAS_PARA_COMPRAR_REGALO = 5


@dataclass
class App:
    repo: Repositorio

    def crear_juego(self, fecha_de_celebracion_del_juego: date):
        fecha_de_inicio_juego = date.today()
        fecha_limite_para_admitir_participantes = fecha_de_celebracion_del_juego - \
            timedelta(days=DIAS_PARA_COMPRAR_REGALO)
        self.repo.guardar_juego(
            fecha_de_inicio_juego=fecha_de_inicio_juego,
            fecha_limite_para_admitir_participantes=fecha_limite_para_admitir_participantes,
            fecha_de_celebracion_del_juego=fecha_de_celebracion_del_juego)
        return self

    def agregar_jugador(self, id_juego: str, nombre_usuario: str):
        self.repo.guardar_participante(
            id_juego=id_juego, nombre_usuario=nombre_usuario)
        return self
