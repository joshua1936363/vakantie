import os
from flask import Flask, render_template, request, redirect, url_for
import json
import streamlit as st

app = Flask(__name__)
app.run(port=5234)

def load_vragen():
    if os.path.exists('vragen.json'):
        with open('vragen.json', 'r') as f:
            return json.load(f)
    return []

def save_vragen(vragen):
    with open('vragen.json', 'w') as f:
        json.dump(vragen, f)

vragen = load_vragen()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/vragen', methods=['GET', 'POST'])
def vragen_page():
    if request.method == 'POST':
        vraag = request.form['vraag']
        foto = request.files['foto']
        if foto:
            foto.save(os.path.join('static', foto.filename))
        vragen.append({'vraag': vraag, 'foto': foto.filename if foto else None, 'reacties': []})
        save_vragen(vragen)
        return redirect(url_for('vragen_page'))
    return render_template('vragen.html', vragen=vragen, enumerate=enumerate)

@app.route('/reactie/<int:vraag_id>', methods=['POST'])
def reactie(vraag_id):
    reactie = request.form['reactie']
    vragen[vraag_id]['reacties'].append(reactie)
    save_vragen(vragen)
    return redirect(url_for('vragen_page'))

@app.route('/verwijder_vraag/<int:vraag_id>', methods=['POST'])
def verwijder_vraag(vraag_id):
    vragen.pop(vraag_id)
    save_vragen(vragen)
    return redirect(url_for('vragen_page'))

@app.route('/verwijder_reactie/<int:vraag_id>/<int:reactie_id>', methods=['POST'])
def verwijder_reactie(vraag_id, reactie_id):
    vragen[vraag_id]['reacties'].pop(reactie_id)
    save_vragen(vragen)
    return redirect(url_for('vragen_page'))

@app.route('/route')
def route():
    return render_template('route.html')

def run_flask():
    app.run()

if __name__ == '__main__':
    run_flask()
