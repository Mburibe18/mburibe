from flask import Flask, request, make_response, redirect, render_template, url_for
import utilidades as helper

#Se crea un objeto del tipo app
app = Flask (__name__)

fileNameCredential = 'usuarios.csv'
data = helper.leerArchivo(fileNameCredential)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')
    
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
    helper.leerArchivo('usuarios.csv')
    return redirect(url_for('login'))

@app.route('/home')
def home():
   return render_template('home.html')

@app.route('/login', methods = ['POST','GET'])
def login():
    data = helper.leerArchivo(fileNameCredential)
    if request.method == 'POST':
        nameUser = request.form['name']
        passUser = request.form ['pass']
        output= helper.validatePassword (data, nameUser, passUser)
        if (output == True):
            return  redirect(url_for('home'))
        elif (output == 'Usuario no registrado'):
            return  redirect(url_for('singin'))
        else:
            return 'Falló proceso de autenticación'
    else: 
        return render_template('login.html')

        




@app.route('/signin', methods = ['POST','GET'])
def singin():

    if request.method == 'POST':
        helper.saveUser (data,fileNameCredential,request.form['name'],request.form ['pass'] )
        return redirect(url_for('success'))
    else: 
        return render_template('signIn.html')

@app.route('/success', methods= ['GET'])
def success():
    return render_template('success.html')


    
if __name__ == '__main__':
    app.run()