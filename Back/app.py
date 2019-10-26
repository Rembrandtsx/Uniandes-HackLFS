# app.py
from flask import Flask, request, jsonify
from firebase import firebase
import os
firebase = firebase.FirebaseApplication('https://hackandes-1816a.firebaseio.com/', None)
app = Flask(__name__)

@app.route('/data/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    name = request.args.get("name", None)
    

    response = {}


    result = firebase.get('/hackandes-1816a/Juegos/', '')
    print(result)


    response=result


    """"# Check if user sent a name at all
    if not name:
        response["ERROR"] = "no name found, please send a name."
    # Check if the user entered a number not a name
    elif str(name).isdigit():
        response["ERROR"] = "name can't be numeric."
    # Now the user entered a valid name
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"
"""

    # Return the response in json format
    return jsonify(response)

@app.route('/data/', methods=['POST'])
def post_something():
    usuario = request.form.get('usuario')
    print(usuario)
     print(request.json())
    atributo2 = request.form.get('atributo2')
    atributo3= request.form.get('atributo3')
    juego = request.form.get('juego')


    data =  { 'usuario':usuario,
        'atributo2': atributo2,
          'atributo3': atributo3,
          'juego': juego
          }
    result = firebase.post('/hackandes-1816a/Juegos/',data)
    resultget = firebase.get('/hackandes-1816a/Juegos/','')
    
    print(resultget)
    return jsonify(resultget)

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server!!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    port = int(os.environ.get("PORT", 5000))
    app.run(threaded=True, port=port)
