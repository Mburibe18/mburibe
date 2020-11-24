from flask import Flask, request, make_response, redirect, render_template, url_for
#Se crea un objeto del tipo app
app = Flask (__name__)

@app.route('/')
def beginRoute():
    return render_template("begin.html")




@app.route('/pacientes')
def pacientessRoute():
    return render_template('pacientes.html')

@app.route('/doctores')
def doctoresRoute():
    return render_template('doctores.html')


@app.route('/conocenos')
def conocenosRoute():

    return render_template('conocenos.html')

@app.route('/contactanos')
def contactanosRoute():
    return render_template('contactanos.html')


@app.route('/curioso')
def curiosoRoute():
    return render_template('curioso.html')


if __name__=='__main__':
    app.run()