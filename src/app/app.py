from interfaces import Repositorio
class App:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def crearJuego(self, nombre, fecha_de_inicio, fecha_de_publicacion, fecha_de_vencimiento):
        juego = self.repositorio.crearJuego(nombre, fecha_de_inicio, fecha_de_publicacion, fecha_de_vencimiento)
        return juego

    def almacenarJuego(self, juego):
        self.repositorio.almacenarJuego(juego)
        return juego
    
    def agregarJugador(self, juego, jugador):
        juego.agregarJugador(jugador)
        return juego

