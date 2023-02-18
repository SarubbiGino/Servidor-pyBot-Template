import datetime
from interface import Repositorio, RepositorioJuego
from app import App


repositorio = RepositorioJuego()
nombre = 'Amigo Invisible'
fecha_de_inicio = datetime.datetime(2022, 1, 1)
fecha_de_publicacion = datetime.datetime(2022, 2, 1)
fecha_de_vencimiento = datetime.datetime(2022, 12, 31)

juego = App(repositorio).crearJuego(nombre, fecha_de_inicio, fecha_de_publicacion, fecha_de_vencimiento)
App(repositorio).almacenarJuego(juego)

print(juego.nombre)
print(juego.fecha_de_inicio)
print(juego.fecha_de_publicacion)
print(juego.fecha_de_vencimiento)
