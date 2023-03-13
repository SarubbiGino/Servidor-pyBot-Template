from interfaces import Repositorio
from dataclasses import dataclass
from datetime import date
from datetime import datetime, timedelta
from interfaces import Participante


def sumar_cinco_dias():
    fecha_actual = datetime.today()
    fecha_futura = fecha_actual + timedelta(days=5)
    return fecha_futura


def sumar_diez_dias():
    fecha_actual = datetime.today()
    fecha_futura = fecha_actual + timedelta(days=10)
    return fecha_futura


DIAS_PARA_COMPRAR_REGALO = 5
PUNTOS_POR_ACERTAR = 40
PUNTOS_POR_ERRAR = - 20
PUNTOS_PARA_DESBLOQUEAR_DESEOS = 100

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

    def consultar_regalo_en_lista_deseos(self, id_juego: str, id_participante: str, regalo_por_consultar: str):
        # Obtener información del participante
        participante: Participante = self.repo.obtener_participante(
            id_juego, id_participante)
        if participante is None:
            return {"resultado": "Participante no encontrado"}

        # Obtener información del destinatario
        id_destinatario = participante.id_amigo_asignado
        destinatario = self.repo.obtener_participante(
            id_juego, id_destinatario)
        if destinatario is None:
            return {"resultado": "Destinatario no encontrado"}

        # Obtener lista de deseos del destinatario
        lista_deseos = destinatario.lista_deseos
        if not lista_deseos:
            return {"resultado": "El destinatario no ha agregado ningún elemento a su lista de deseos"}

        # Mostrar lista de deseos como respuesta
        # return {"resultado": f"Los posibles regalos para {destinatario['nombre']} son: {', '.join(lista_deseos)}"}
        if regalo_por_consultar in lista_deseos:
            puntos_acumulados = participante.puntos_acumulados + PUNTOS_POR_ACERTAR
            self.repo.actualizar_puntos_acumulados(
                id_participante=id_participante,
                puntos_acumulados=puntos_acumulados)
            return ResConsultaRegalo(
                puntos_obtenidos=PUNTOS_POR_ACERTAR,
                puntos_acumulados=puntos_acumulados,
                acertado=True
            )

    def consultar_lista_deseos(self, id_juego: str, id_participante: str, pregunta: str):
        lista_deseos = self.repo.obtener_deseos(id_juego, id_participante)

        # Palabras clave que otorgan puntos
        palabras_clave = ['zapatillas', 'taza', 'playstation']
        puntuacion = {'zapatillas': 80, 'taza': 50,
                      'playstation': 70}  # Puntos por palabra clave

        puntos_obtenidos = 0
        for palabra in palabras_clave:
            if palabra in pregunta.lower() and palabra in lista_deseos:
                puntos_obtenidos += puntuacion[palabra]

        return {'puntos_obtenidos': puntos_obtenidos}


# esto va en interfaces
@dataclass
class ResConsultaRegalo:
    participante_encontrado: bool = True
    amigo_asignado_encontrado: bool = True
    lista_vacia: bool = False
    puntos_obtenidos: int = 0
    puntos_acumulados: int = 0
    acertado: bool = False
