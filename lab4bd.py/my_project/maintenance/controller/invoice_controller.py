from flask import Blueprint, jsonify
from my_project.maintenance.service import invoice_service

invoice_bp = Blueprint('invoice_bp', __name__)

@invoice_bp.route('/api/invoices', methods=['GET'])
def get_invoices_with_techs():
    invoices = invoice_service.get_all_with_details()
    return jsonify([i.to_dict() for i in invoices])