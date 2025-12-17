from my_project.maintenance.controller.terminal_controller import terminal_bp

def register_terminal_routes(app):
    app.register_blueprint(terminal_bp)