from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from engine.inference_engine import InferenceEngine

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
        zone = request.form['zone']

        engine = InferenceEngine()
        paciente_sintomas = {'fiebre_mayor_37': (fever == "Si"),
                             'dolor_garganta': throat,
                             'dif_respirar': breath,
                             'cansancio': fatigue,
                             'anosmia': smell,
                             'ageusia': taste,
                             'tos_seca': cough,
                             'cefalea': (headache == "Si"),
                             'secrecion_nasal': (mocus == "Si"),
                             'grupo_riesgo': (risk == "Si"),
                             'contacto_estrecho': contact,
                             'cant_contagios_zona': zone
                            }

        resultado = engine.startEngine(paciente_sintomas)
        return render_template('resultados.html', resultado=resultado)
    return render_template('consulta.html')
