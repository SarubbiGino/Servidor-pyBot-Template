import pymongo
from pymongo import MongoClient
from interfaces.interfaces import Juego, Repositorio
import datetime

#Crear base de datos
miCliente = pymongo.MongoClient("mongodb://localhost:27017/")
   
miDataBase = miCliente["BaseDeDatos"]

#Crear Coleccion de Participantes
Participantes = miDataBase["Participantes"]

#Crear Coleccion de Juegos
MisJuegos = miDataBase["Juegos"]
#Insertar registro en la coleccion
#Lista = { "id": 1,
 #           "nombreDeUsuario": "Suarezzz#7013",
  #          "ListaDeRegalo": "Remeras, Pantalones",
   #         "Compañero": 2,
    #        "Puntos acumulados por adivinar regalos": "192",
     #       "Puede ver la lista de su compañero": True}

#x = miColeccion.insert_one(Lista)

#Mostrar los Nombres de Usuarios
#for mostrar in miColeccion.find():
#    print(mostrar["nombreDeUsuario"])

#Mostrar todo
#resultados = miColeccion.find()
#for resultado in resultados:
#    print(resultado["nombreDeUsuario"]+" "+resultado["ListaDeRegalo"]+" "+str(resultado["Compañero"])+" "+resultado["Puntos acumulados por adivinar regalos"])

class DBMongo(Repositorio):
    def guardarUnParticipante(self, nombreDeUsuario: str, puntosAcumuladosParaAdivinarListaDeRegalos: int, puedeVerListaDeRegalos: bool):
        Lista = {
            "Nombre De Usuario": nombreDeUsuario,
            "Puntos acumulados por adivinar regalos": puntosAcumuladosParaAdivinarListaDeRegalos,
            "Puede ver la lista de su compañero": puedeVerListaDeRegalos}
        
        x = Participantes.insert_one(Lista)
    def almacenarJuego(self, juego: str, fecha_de_inicio: datetime, fecha_de_publicacion: datetime, fecha_de_vencimiento: datetime):
        Lista = {
            "Nombre Del Juego": juego,
            "Fecha de Inicio": fecha_de_inicio,
            "Fecha de Publicaciion": fecha_de_publicacion,
            "Fecha de Vencimiento": fecha_de_vencimiento}

        x = MisJuegos.insert_one(Lista)
  
    def dameElJuego(self, id: int) -> Juego:
        for mostrar in MisJuegos.find():
            print(mostrar["Nombre Del Juego"]+" "+mostrar["Fecha de Inicio"]+" "+mostrar["Fecha de Publicaciion"]+" "+mostrar["Fecha de Vencimiento"])
   
    
