class Terminal:
    def __init__(self, terminal_id, inventory_number, city, address, model, manufacturer):
        self.terminal_id = terminal_id
        self.inventory_number = inventory_number
        self.city = city
        self.address = address
        self.model = model
        self.manufacturer = manufacturer

    def to_dict(self):
        return {
            "terminal_id": self.terminal_id,
            "inventory_number": self.inventory_number,
            "location": f"{self.city}, {self.address}",
            "device": f"{self.manufacturer} {self.model}"
        }