class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

    def __repr__(self):
        return f"Магазин: {self.name}, Адрес: {self.address}, Ассортимент: {self.items}"

# Создание объектов класса Store
store1 = Store("Магазин у дома", "ул. Ленина, 1")
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)

store2 = Store("Супермаркет", "ул. Гагарина, 10")
store2.add_item("milk", 1.5)
store2.add_item("bread", 1.0)

store3 = Store("Эко-магазин", "ул. Пушкина, 5")
store3.add_item("tofu", 2.5)
store3.add_item("soy milk", 3.0)

# Тестирование методов для одного из магазинов
print(store1)
store1.add_item("oranges", 0.8)
print("Добавлен товар:", store1)

store1.update_price("apples", 0.6)
print("Обновлена цена:", store1)

store1.remove_item("bananas")
print("Удален товар:", store1)

print("Цена на apples:", store1.get_price("apples"))
print("Цена на bananas:", store1.get_price("bananas"))