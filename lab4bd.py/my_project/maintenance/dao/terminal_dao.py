from my_project.utils.db_connection import get_db_connection
from my_project.maintenance.domain.terminal import Terminal

def get_all_terminals():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT t.terminal_id, t.inventory_number, l.city, l.address, 
               tm.model_name, m.name as manufacturer_name
        FROM terminals t
        JOIN locations l ON t.location_id = l.location_id
        JOIN terminal_models tm ON t.model_id = tm.model_id
        JOIN manufacturers m ON tm.manufacturer_id = m.manufacturer_id
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [Terminal(r['terminal_id'], r['inventory_number'], r['city'], r['address'], r['model_name'], r['manufacturer_name']) for r in rows]

def get_terminal_by_id(terminal_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT t.terminal_id, t.inventory_number, l.city, l.address, 
               tm.model_name, m.name as manufacturer_name
        FROM terminals t
        JOIN locations l ON t.location_id = l.location_id
        JOIN terminal_models tm ON t.model_id = tm.model_id
        JOIN manufacturers m ON tm.manufacturer_id = m.manufacturer_id
        WHERE t.terminal_id = %s
    """
    cursor.execute(query, (terminal_id,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    if row:
        return Terminal(row['terminal_id'], row['inventory_number'], row['city'], row['address'], row['model_name'], row['manufacturer_name'])
    return None

def create_terminal(location_id, model_id, inventory_number, commission_date):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO terminals (location_id, model_id, inventory_number, commission_date) VALUES (%s, %s, %s, %s)", 
                   (location_id, model_id, inventory_number, commission_date))
    conn.commit()
    new_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return new_id

def update_terminal(terminal_id, inventory_number, commission_date):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE terminals SET inventory_number=%s, commission_date=%s WHERE terminal_id=%s", 
                   (inventory_number, commission_date, terminal_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_terminal(terminal_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM terminals WHERE terminal_id=%s", (terminal_id,))
    conn.commit()
    cursor.close()
    conn.close()

def get_terminals_by_location_id(location_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT t.terminal_id, t.inventory_number, l.city, l.address, 
               tm.model_name, m.name as manufacturer_name
        FROM terminals t
        JOIN locations l ON t.location_id = l.location_id
        JOIN terminal_models tm ON t.model_id = tm.model_id
        JOIN manufacturers m ON tm.manufacturer_id = m.manufacturer_id
        WHERE t.location_id = %s
    """
    cursor.execute(query, (location_id,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [Terminal(r['terminal_id'], r['inventory_number'], r['city'], r['address'], r['model_name'], r['manufacturer_name']) for r in rows]