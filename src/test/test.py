import datetime
from interface import Repositorio, RepositorioFake
from app import App


repositorio = RepositorioFake()
nombre = 'Amigo Invisible'
fecha_de_inicio = datetime.datetime(2022, 1, 1)
fecha_de_publicacion = datetime.datetime(2022, 2, 1)
fecha_de_vencimiento = datetime.datetime(2022, 12, 31)

juego = App(repositorio).crearJuego(nombre, fecha_de_inicio,
                                    fecha_de_publicacion, fecha_de_vencimiento)
App(repositorio).almacenarJuego(juego)

print(repositorio.juegos[0].nombre)
print(repositorio.juegos[0].fecha_de_inicio)
print(repositorio.juegos[0].fecha_de_publicacion)
print(repositorio.juegos[0].fecha_de_vencimiento)
