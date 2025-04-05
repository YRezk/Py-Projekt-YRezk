# app/__init__.py

from flask import Flask

# Erstelle die Flask-App
app = Flask(__name__)

# Lade die Konfiguration aus dem Modul config.py
app.config.from_object('app.config')

# Globale, in-Memory-Datenstrukturen zur Speicherung von Todo-Listen und -Einträgen
app.todo_lists = [
    {'id': '1318d3d1-d979-47e1-a225-dab1751dbe75', 'name': 'Einkaufsliste'},
    {'id': '3062dc25-6b80-4315-bb1d-a7c86b014c65', 'name': 'Arbeit'},
    {'id': '44b02e00-03bc-451d-8d01-0c67ea866fee', 'name': 'Privat'},
]

app.todos = [
    {'id': 'dummy-uuid-1', 'name': 'Milch', 'description': '', 'list': '1318d3d1-d979-47e1-a225-dab1751dbe75'},
    {'id': 'dummy-uuid-2', 'name': 'Arbeitsblätter ausdrucken', 'description': '', 'list': '3062dc25-6b80-4315-bb1d-a7c86b014c65'},
    {'id': 'dummy-uuid-3', 'name': 'Kinokarten kaufen', 'description': '', 'list': '44b02e00-03bc-451d-8d01-0c67ea866fee'},
    {'id': 'dummy-uuid-4', 'name': 'Eier', 'description': '', 'list': '1318d3d1-d979-47e1-a225-dab1751dbe75'},
]

# Globale CORS-Konfiguration: Erlaubt den Zugriff von allen Domains
@app.after_request
def apply_cors(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

# Importiere die Endpunkt-Module (Listen und Todos)
from app import lists
from app import todos
