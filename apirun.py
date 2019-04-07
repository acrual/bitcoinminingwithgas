from deletetweets import *
from flask import Flask, request
from flask_restful import Resource, Api
from flask import render_template
from panditas import mmbtu
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify 

db_connect = create_engine('postgresql://postgres:postgres@localhost:5432/Back y Front End Python')
app = Flask(__name__)
api = Api(app)

@app.route('/seguidores/<user>')
def seguidores_display(user):
    try:
        return render_template(
                "seguidores.html",  #name of template
                cuenta = user, # valor de usuario en el template
                seguidores = sacar(user)[0], # número de seguidores
                seguidos = sacar(user)[1], # número de seguidos
                amigos = amiguitos(user), # amiguitos que sigue
                tweets = ult_tweets(user), # lista de los últimos 20 tweets
        )
    except:
        return "Algo ha ido mal"

@app.route('/mmbtu/<int:num>')
def display_cifras(num):
        try:
                return render_template(
                        "mmbtu.html",  #name of template
                        cifras = mmbtu(num), # valor de usuario en el template
        )

        except:
                return "Algo ha salido mal"

class Mmbtu_api(Resource):
        def get(self):
                conn = db_connect.connect()
                query = conn.execute("SELECT * FROM cifras;")
                dias = query.cursor.fetchall()
                return {'mmbtus': [mmbtu for mmbtu in dias]}

api.add_resource(Mmbtu_api, '/mmbtus_api')

if __name__ == '__main__':
        app.run(host='127.0.0.1', port = 5002)