class Invoice:
    def __init__(self, invoice_id, terminal_inv, service_name, date, amount, status):
        self.invoice_id = invoice_id
        self.terminal_inventory = terminal_inv
        self.service_name = service_name
        self.date = str(date)
        self.amount = float(amount)
        self.status = status
        self.technicians = []

    def to_dict(self):
        return {
            "invoice_id": self.invoice_id,
            "terminal": self.terminal_inventory,
            "service": self.service_name,
            "date": self.date,
            "amount": self.amount,
            "status": self.status,
            "technicians": self.technicians
        }