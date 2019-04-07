from deletetweets import *
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello '+ name + '!'

@app.route('/square/<int:num>')
def f(num):
    # No conversion of x needed.
    return str(num**2)

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
if __name__ == '__main__':
  app.run(host='0.0.0.0')