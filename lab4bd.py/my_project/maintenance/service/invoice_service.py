from my_project.maintenance.dao import invoice_dao

def get_all_with_details():
    return invoice_dao.get_invoices_with_technicians()