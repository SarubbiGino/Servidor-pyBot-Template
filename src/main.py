from flask import Flask, request, abort
from app.app import App
from db.bdd import DBMongo

app = Flask(__name__)
server = App(repo=DBMongo())


@app.route('/')
def hello():
    return 'bienvenido al juego del amigo invisible'


@app.route('/api/v1/juegos', methods=['POST'])
def post_juego():
    if request.method == 'POST':
        fecha_de_celebracion = request.args['fecha_celebracion']
        server.crear_juego(
            fecha_de_celebracion_del_juego=fecha_de_celebracion)
    else:
        abort(502)


if __name__ == '__main__':
    app.run()
