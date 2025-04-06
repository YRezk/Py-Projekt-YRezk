# app/todos.py

import uuid
from flask import jsonify, request, abort
from app import app

# POST /todo-list/<list_id>/entry – Fügt einen neuen Todo-Eintrag zu einer Liste hinzu
@app.route('/todo-list/<list_id>/entry', methods=['POST'])
def add_todo_entry(list_id):
    # Prüfe, ob die Liste existiert
    list_item = next((l for l in app.todo_lists if l['id'] == list_id), None)
    if not list_item:
        abort(404, description="Todo-Liste nicht gefunden.")
    
    data = request.get_json(force=True)
    if 'name' not in data or 'description' not in data:
        abort(400, description="Felder 'name' und 'description' müssen im Request vorhanden sein.")
    
    new_entry = {
        'id': str(uuid.uuid4()),
        'name': data['name'],
        'description': data['description'],
        'list': list_id  # intern gespeichert, aber nicht im Response
    }
    app.todos.append(new_entry)
    response_data = {
        'id': new_entry['id'],
        'name': new_entry['name'],
        'description': new_entry['description']
    }
    return jsonify(response_data), 200

# PUT /todo-list/<list_id>/entry/<entry_id> – Aktualisiert einen bestehenden Todo-Eintrag
@app.route('/todo-list/<list_id>/entry/<entry_id>', methods=['PUT'])
def update_todo_entry(list_id, entry_id):
    # Prüfe, ob die Liste existiert
    list_item = next((l for l in app.todo_lists if l['id'] == list_id), None)
    if not list_item:
        abort(404, description="Todo-Liste nicht gefunden.")
    
    entry = next((e for e in app.todos if e['id'] == entry_id and e['list'] == list_id), None)
    if not entry:
        abort(404, description="Todo-Eintrag nicht gefunden.")
    
    data = request.get_json(force=True)
    if 'name' not in data or 'description' not in data:
        abort(400, description="Felder 'name' und 'description' müssen im Request vorhanden sein.")
    
    entry['name'] = data['name']
    entry['description'] = data['description']
    return jsonify(entry), 200

# DELETE /todo-list/<list_id>/entry/<entry_id> – Löscht einen bestehenden Todo-Eintrag
@app.route('/todo-list/<list_id>/entry/<entry_id>', methods=['DELETE'])
def delete_todo_entry(list_id, entry_id):
    # Prüfe, ob die Liste existiert
    list_item = next((l for l in app.todo_lists if l['id'] == list_id), None)
    if not list_item:
        abort(404, description="Todo-Liste nicht gefunden.")
    
    entry = next((e for e in app.todos if e['id'] == entry_id and e['list'] == list_id), None)
    if not entry:
        abort(404, description="Todo-Eintrag nicht gefunden.")
    
    app.todos.remove(entry)
    return jsonify({'msg': 'success'}), 200
