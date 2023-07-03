class StockItem:
    def __init__(self, item_name, quantity, supplier, category):
        self.item_name = item_name
        self.quantity = quantity
        self.supplier = supplier
        self.category = category

class StockManagementSystem:
    def __init__(self):
        self.stock_items = []
        self.suppliers = []
        self.categories = []

    def retrieve_stock_list(self):
        return self.stock_items

    def search_item(self, item_name):
        for item in self.stock_items:
            if item.item_name == item_name:
                return item.quantity
        return 0

    def add_item(self, item_name, quantity, supplier, category):
        new_item = StockItem(item_name, quantity, supplier, category)
        self.stock_items.append(new_item)

    def update_item_quantity(self, item_name, new_quantity):
        for item in self.stock_items:
            if item.item_name == item_name:
                item.quantity = new_quantity
                break

    def remove_item(self, item_name):
        for item in self.stock_items:
            if item.item_name == item_name:
                self.stock_items.remove(item)
                break

    def retrieve_supplier_list(self):
        return self.suppliers

    def retrieve_category_list(self):
        return self.categories

    def record_transaction(self, transaction_type, date, quantity, item_name, customer_info):
        # Code to record the transaction in your desired format or database
        # You can define a Transaction class and store the transaction details
        pass


# Usage example:

stock_system = StockManagementSystem()

# Add some stock items
stock_system.add_item("Item 1", 10, "Supplier A", "Category X")
stock_system.add_item("Item 2", 5, "Supplier B", "Category Y")

# Retrieve stock list
stock_list = stock_system.retrieve_stock_list()
for item in stock_list:
    print(item.item_name, item.quantity)

# Search for an item and view its quantity
item_quantity = stock_system.search_item("Item 1")
print("Item 1 quantity:", item_quantity)

# Update item quantity
stock_system.update_item_quantity("Item 1", 20)

# Remove an item
stock_system.remove_item("Item 2")

# Retrieve supplier list
supplier_list = stock_system.retrieve_supplier_list()
for supplier in supplier_list:
    print(supplier)

# Retrieve category list
category_list = stock_system.retrieve_category_list()
for category in category_list:
    print(category)

# Record a stock transaction
stock_system.record_transaction("Purchase", "2023-06-30", 5, "Item 1", "Customer X")
