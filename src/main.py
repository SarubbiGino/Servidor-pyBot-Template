from flask import Flask, jsonify, request, abort
from app.app import App
from db.bdd import DBMongo

app = Flask(__name__)
server = App(repo=DBMongo())

# Ruta de bienvenida
@app.route('/')
def hello():
    return 'bienvenido al juego del amigo invisible'


# Ruta para crear un juego
@app.route('/api/v1/juegos', methods=['POST'])
def post_juego():
    if request.method == 'POST':
        fecha_de_celebracion = request.args['fecha_celebracion']
        server.crear_juego(
            fecha_de_celebracion_del_juego=fecha_de_celebracion)
    else:
        abort(502)


# Ruta para obtener un juego por ID
@app.route('/api/v1/juegos/<id_juego>', methods=['GET'])
def obtener_juego(id_juego):
    if request.method == 'GET':
        juego = server.obtener_juego(id_juego)
        if juego:
            return jsonify(juego), 200
        else:
            abort(404)
    else:
        abort(400)


# Ruta para agregar un participante a un juego
@app.route('/api/v1/juegos/<id_juego>/participantes', methods=['POST'])
def agregar_participante(id_juego):
    if request.method == 'POST':
        nombre = request.json['nombre']
        nuevo_participante = server.agregar_participante(
            id_juego=id_juego, nombre=nombre)
        return jsonify(nuevo_participante), 201
    else:
        abort(400)


# Ruta para obtener una lista de todos los participantes de un juego
@app.route('/api/v1/juegos/<id_juego>/participantes', methods=['GET'])
def obtener_participantes(id_juego):
    if request.method == 'GET':
        participantes = server.obtener_participantes(id_juego=id_juego)
        return jsonify(participantes), 200
    else:
        abort(400)


# Ruta para obtener información sobre un participante en particular
@app.route('/api/v1/juegos/<id_juego>/participantes/<id_participante>', methods=['GET'])
def obtener_participante(id_juego, id_participante):
    if request.method == 'GET':
        participante = server.obtener_participante(
            id_juego=id_juego, id_participante=id_participante)
        if participante:
            return jsonify(participante), 200
        else:
            abort(404)
    else:
        abort(400)


# Ruta para agregar lista de deseo a un participante
@app.route('/api/v1/juegos/<id_juego>/participantes/<id_participante>/deseos', methods=['PUT'])
def agregar_lista_deseos(id_juego, id_participante):
    if request.method == 'PUT':
        lista_deseos = request.json['lista_deseos']
        server.agregar_lista_deseos(
            id_juego=id_juego, id_participante=id_participante, lista_deseos=lista_deseos)
        return '', 204
    else:
        abort(400)


# Ruta para agregar un producto a la lista de deseos de un participante
@app.route('/api/v1/juegos/<id_juego>/participantes/<id_participante>/deseos', methods=['POST'])
def agregar_deseo(id_juego, id_participante):
    if request.method == 'POST':
        item = request.json['item']
        server.agregar_deseo(
            id_juego=id_juego, id_participante=id_participante, item=item)
        return '', 204
    else:
        abort(400)

# Ruta para consultar si un producto está en la lista de deseos de un participante
# si está, se le suman 80 puntos al participante que hizo la consulta y si no está, se le restan 30 puntos.
@app.route('/api/v1/juegos/<id_juego>/participantes/<id_participante>/consultas', methods=['POST'])
def consultar_regalo_en_lista_deseos(id_juego, id_participante):
    if request.method == 'POST':
        consulta = request.json['consulta']
        lista_deseos = server.obtener_deseos(
            id_juego=id_juego, id_participante=id_participante)
        if consulta in lista_deseos:
            puntos = server.sumar_puntos(id_participante, 80)
            mensaje = f"Tienes {puntos} puntos por encontrar '{consulta}' en la lista de deseos de tu amigo."
        else:
            puntos = server.sumar_puntos(id_participante, -30)
            mensaje = f"No encontramos '{consulta}' en la lista de deseos de tu amigo. Pierdes 30 puntos. Tienes {puntos} puntos ahora."
        return jsonify(mensaje), 200
    else:
        abort(400)

# Ruta para obtener la lista de deseos de un participante [solo si el participante que consulta la Lista tiene más de 160 puntos]
@app.route('/api/v1/juegos/<id_juego>/participantes/<id_participante>/deseos', methods=['GET'])
def obtener_deseos(id_juego, id_participante):
    if request.method == 'GET':
        puntaje = server.obtener_puntaje(id_participante)
        if puntaje >= 100:
            deseo = server.obtener_deseos(id_juego=id_juego, id_participante=id_participante)
            return jsonify(deseo), 200
        else:
            return "No tienes suficiente puntaje para acceder a la lista de deseos", 403
    else:
        abort(400)




if __name__ == '__main__':
    app.run()
