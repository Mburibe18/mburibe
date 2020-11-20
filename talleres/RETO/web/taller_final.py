from flask import Flask, request, make_response, redirect, render_template, url_for
#Se crea un objeto del tipo app
app = Flask (__name__)

@app.route('/')
def inicioRoute():
    return render_template("inicio.html")




@app.route('/doctors')
def doctorsRoute():
    return render_template('doctors.html')

@app.route('/services')
def servicesRoute():
    return render_template('services.html')


@app.route('/about')
def aboutRoute():

    return render_template('about.html')

@app.route('/contact')
def contactRoute():
    return render_template('contact.html')


if __name__=='__main__':
    app.run()