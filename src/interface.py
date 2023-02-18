class Juego:
    def __init__(self, nombre, fecha_de_inicio, fecha_de_publicacion, fecha_de_vencimiento):
        self.nombre = nombre
        self.fecha_de_inicio = fecha_de_inicio
        self.fecha_de_publicacion = fecha_de_publicacion
        self.fecha_de_vencimiento = fecha_de_vencimiento


class Repositorio:
    pass


class RepositorioJuego(Repositorio):
    def __init__(self):
        self.juegos = []

    def crearJuego(self, nombre, fecha_de_inicio, fecha_de_publicacion, fecha_de_vencimiento):
        juego = Juego(nombre, fecha_de_inicio, fecha_de_publicacion, fecha_de_vencimiento)
        return juego

    def almacenarJuego(self, juego):
        self.juegos.append(juego)
        return juego
    
    def agregarJugador(self, juego, jugador):
        juego.agregarJugador(jugador)
        return juego
