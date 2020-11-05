from flask import Flask, request, make_response, redirect, render_template
#Se crea un objeto del tipo app
app = Flask (__name__)

@app.route('/')
def home():
    user_ip = request.remote_addr
    response = make_response(redirect("Suanfonson"))
    response.set_cookie("ip",user_ip)
    response.set_cookie('persona','Marco')
    return response

@app.route('/Suanfonson')
def SuanfonsonRoute():
    persona = request.cookies.get('persona')
    ip = request.cookies.get('ip')
    return render_template('Suanfonson.html', tipo = persona, userIp = ip)
if __name__ == '__main__':
    app.run()