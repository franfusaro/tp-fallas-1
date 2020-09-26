from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consulta', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        fever = request.form['fever']
        throat = request.form['sore_throat']
        breath = request.form['breath']
        fatigue = request.form['fatigue']
        smell = request.form['smell']
        taste = request.form['taste']
        cough = request.form['cough']
        headache = request.form['headache'] 
        mocus = request.form['mocus']
        risk = request.form['risk']
        contact = request.form['contact']
        zone =request.form['zone']

        #resultado = procesar_sintomas(fever, throat, breath, fatigue, smell, taste, cough, headache, mocus, risk, contact, zone)
        resultado = "Algún resultado"
        return render_template('resultados.html', resultado = resultado)
    return render_template('consulta.html')