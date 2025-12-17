from my_project.maintenance.controller.invoice_controller import invoice_bp

def register_invoice_routes(app):
    app.register_blueprint(invoice_bp)