from flask import Flask, request, make_response, redirect, render_template, url_for
#Se crea un objeto del tipo app
app = Flask (__name__)



@app.route('/hello')
def helloRoute():
    gato = request.cookies.get('gato')
    ip = request.cookies.get('ip')
    return render_template('hello.html', mascota = gato, userIp = ip)


@app.route('/Suanfonson')
def SuanfonsonRoute():
    persona = request.cookies.get('persona')
    ip = request.cookies.get('ip')
    return render_template('Suanfonson.html', tipo = persona, userIp = ip)

@app.route('/lugares')
def lugaresRoute():
    lugares = request.cookies.get('lugares')
    ip = request.cookies.get('ip')
    return render_template('lugares.html', tipo = lugares, userIp = ip)


@app.route('/personajes')
def personajesRoute():
    personajes = request.cookies.get('personajes')
    ip = request.cookies.get('ip')
    return render_template('personajes.html', tipo = personajes, userIp = ip)

@app.route('/')
def baseRoute():
    return redirect(url_for('login'))

@app.route('/home')
def home():
   return render_template('home.html')

@app.route('/login', methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        nameUser = request.form['name']
        passUser = request.form ['pass']
        if (passUser == 'hola1234'):
            return  redirect(url_for('home'))
        else:
            return 'Falló proceso de autenticación'
    else: 
        return render_template('login.html')


    
if __name__ == '__main__':
    app.run()