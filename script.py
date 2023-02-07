class Transaction:
    def __init__(self):
        self.transaction_id = "trnsct_123"
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def update_item_name(self, name, update_name):
        for item in self.items:
            if item[0] == name:
                item[0] = update_name

    def update_item_qty(self, name, update_qty):
        for item in self.items:
            if item[0] == name:
                item[1] = update_qty

    def update_item_price(self, name, update_price):
        for item in self.items:
            if item[0] == name:
                item[2] = update_price

    def delete_item(self, name):
        for item in self.items:
            if item[0] == name:
                self.items.remove(item)

    def reset_transaction(self):
        self.items.clear()

    def check_order(self):
        for item in self.items:
            if None in item:
                return "Terdapat kesalahan input data"
        return "Pemesanan sudah benar"

    def total_price(self):
        total_price = 0
        for item in self.items:
            total_price += item[1] * item[2]
        if total_price >= 500000:
            discount = total_price * 0.1
        elif total_price >= 300000:
            discount = total_price * 0.08
        elif total_price >= 200000:
