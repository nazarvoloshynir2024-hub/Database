from my_project.utils.db_connection import get_db_connection
from my_project.maintenance.domain.invoice import Invoice

def get_invoices_with_technicians():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    sql = """
        SELECT i.invoice_id, t.inventory_number, st.name as service_name, 
               i.event_date, i.total_amount, i.status
        FROM invoices i
        JOIN terminals t ON i.terminal_id = t.terminal_id
        JOIN service_types st ON i.service_type_id = st.service_type_id
    """
    cursor.execute(sql)
    invoice_rows = cursor.fetchall()
    
    invoices = []
    for row in invoice_rows:
        inv = Invoice(row['invoice_id'], row['inventory_number'], row['service_name'],
                      row['event_date'], row['total_amount'], row['status'])
        
        cursor.execute("""
            SELECT tech.full_name, it.hours_worked, it.rate_per_hour
            FROM invoice_technicians it
            JOIN technicians tech ON it.technician_id = tech.technician_id
            WHERE it.invoice_id = %s
        """, (row['invoice_id'],))
        
        inv.technicians = cursor.fetchall()
        invoices.append(inv)
        
    cursor.close()
    conn.close()
    return invoices