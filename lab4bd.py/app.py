from flask import Flask, jsonify
from my_project.maintenance.route.terminal_route import register_terminal_routes
from my_project.maintenance.route.invoice_route import register_invoice_routes

app = Flask(__name__)

register_terminal_routes(app)
register_invoice_routes(app)

@app.route('/')
def index():
    return jsonify({
        "status": "API is running",
        "endpoints": {
            "terminals_crud": "/api/terminals",
            "terminals_by_location_1_M": "/api/locations/<id>/terminals",
            "invoices_with_techs_M_M": "/api/invoices"
        }
    })

if __name__ == '__main__':
    app.run(debug=True, port=5001)