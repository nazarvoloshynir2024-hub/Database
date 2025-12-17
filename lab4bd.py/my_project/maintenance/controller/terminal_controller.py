from flask import Blueprint, jsonify, request
from my_project.maintenance.service import terminal_service

terminal_bp = Blueprint('terminal_bp', __name__)

@terminal_bp.route('/api/terminals', methods=['GET'])
def get_terminals():
    terminals = terminal_service.get_all()
    return jsonify([t.to_dict() for t in terminals])

@terminal_bp.route('/api/terminals/<int:term_id>', methods=['GET'])
def get_terminal(term_id):
    terminal = terminal_service.get_one(term_id)
    if terminal:
        return jsonify(terminal.to_dict())
    return jsonify({"error": "Not found"}), 404

@terminal_bp.route('/api/terminals', methods=['POST'])
def create_terminal():
    data = request.get_json()
    new_id = terminal_service.create(data)
    return jsonify({"message": "Created", "id": new_id}), 201

@terminal_bp.route('/api/terminals/<int:term_id>', methods=['PUT'])
def update_terminal(term_id):
    data = request.get_json()
    terminal_service.update(term_id, data)
    return jsonify({"message": "Updated"})

@terminal_bp.route('/api/terminals/<int:term_id>', methods=['DELETE'])
def delete_terminal(term_id):
    terminal_service.delete(term_id)
    return jsonify({"message": "Deleted"})

@terminal_bp.route('/api/locations/<int:loc_id>/terminals', methods=['GET'])
def get_terminals_by_location(loc_id):
    terminals = terminal_service.get_by_location(loc_id)
    return jsonify([t.to_dict() for t in terminals])