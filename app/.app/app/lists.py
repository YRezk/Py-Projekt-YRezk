# app/lists.py

import uuid
from flask import jsonify, request, abort
from app import app

# GET /list/<list_id> – Ruft alle Todo-Einträge einer bestimmten Liste ab
# DELETE /list/<list_id> – Löscht eine Todo-Liste (und alle zugehörigen Einträge)
@app.route('/list/<list_id>', methods=['GET', 'DELETE'])
def handle_list(list_id):
    # Suche die Liste anhand der ID
    list_item = next((l for l in app.todo_lists if l['id'] == list_id), None)
    if not list_item:
        abort(404, description="Todo-Liste nicht gefunden.")
    
    if request.method == 'GET':
        # Rückgabe aller Einträge, die zu dieser Liste gehören
        entries = [todo for todo in app.todos if todo['list'] == list_id]
        return jsonify(entries), 200

    elif request.method == 'DELETE':
        # Entferne die Liste und lösche auch alle zugehörigen Einträge
        app.todo_lists.remove(list_item)
        app.todos = [todo for todo in app.todos if todo['list'] != list_id]
        return jsonify({'msg': 'Liste erfolgreich gelöscht'}), 200

# POST /list – Erstellt eine neue Todo-Liste
@app.route('/list', methods=['POST'])
def create_list():
    data = request.get_json(force=True)
    if 'name' not in data:
        abort(400, description="Feld 'name' fehlt im Request.")
    new_list = {
        'id': str(uuid.uuid4()),
        'name': data['name']
    }
    app.todo_lists.append(new_list)
    return jsonify(new_list), 200

# GET /lists – Ruft alle Todo-Listen ab
@app.route('/lists', methods=['GET'])
def get_all_lists():
    return jsonify(app.todo_lists), 200
