from pymongo import MongoClient
from interfaces.interfaces import Juego, Repositorio
from datetime import date


class DBMongo(Repositorio):
    def __init__(self) -> None:
        self.client_mongo = MongoClient("mongodb://localhost:27017/")
        self.db = self.client_mongo["BaseDeDatos"]

    def guardar_juego(
            self,
            fecha_limite_para_admitir_participantes: date,
            fecha_de_inicio_del_juego: date,
            fecha_de_celebracion_del_juego: date):
        juegos = self.db['MisJuegos']
        juegos.insert_one(document={
            "fechaLimiteParaAdmitirParticipantes": fecha_limite_para_admitir_participantes,
            "fechaDeInicioDelJuego": fecha_de_inicio_del_juego,
            "fechaDeCelebracionDelJuego": fecha_de_celebracion_del_juego,
            'listaDeParticipantes': []
        })
        return self

    def agregar_participante(
            self,
            id_juego: str,
            nombre_usuario: str,
            puntos_acumulados: int = 0,
            puede_ver_deseos_amigo: bool = False,
            id_amigo: str = '',
            lista_deseos: list[str] = []):
        participantes = self.db['Participantes']
        res = participantes.insert_one(document={
            "nombreDeUsuario": nombre_usuario,
            "puntosAcumulados": puntos_acumulados,
            "puedeVerDeseosDeAmigos": puede_ver_deseos_amigo,
            "listaDeDeseos": lista_deseos,
            'id_amigo': id_amigo
        })
        juegos = self.db['MisJuegos']
        juego = juegos.find_one(filter={
            '_id': id_juego
        })
        lista_participantes = juego['listaDeParticipantes']
        lista_participantes.append(res.inserted_id)
        juegos.update_one(
            filter={
                '_id': id_juego
            },
            update={
                'listaDeParticipantes': lista_participantes
            }
        )
        return self
