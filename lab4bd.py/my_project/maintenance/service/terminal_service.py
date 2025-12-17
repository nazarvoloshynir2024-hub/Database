from my_project.maintenance.dao import terminal_dao

def get_all():
    return terminal_dao.get_all_terminals()

def get_one(terminal_id):
    return terminal_dao.get_terminal_by_id(terminal_id)

def create(data):
    return terminal_dao.create_terminal(data['location_id'], data['model_id'], data['inventory_number'], data['commission_date'])

def update(terminal_id, data):
    terminal_dao.update_terminal(terminal_id, data['inventory_number'], data['commission_date'])

def delete(terminal_id):
    terminal_dao.delete_terminal(terminal_id)

def get_by_location(location_id):
    return terminal_dao.get_terminals_by_location_id(location_id)