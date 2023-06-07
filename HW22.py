class Item:

    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f"Item: name = {self.name} price={self.price}"

lemon = Item('lemon', 10, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
cherry= Item('cherry', 4, "red", "big")

class User:

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"name = {self.name} surname = {self.surname}, numberphone = {self.numberphone}"

buyer1 = User("Ivan", "Ivanov", "02628162")
buyer2 = User("Anna", "Litvin", "06723456")
buyer3 = User("Mykola", "Chub", "063245567")
print(buyer1)

class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item_to_basket(self, item, cnt):
        self.products[item] = cnt
        self.products[item]=cnt

    def remove_from_basket(selfself, item):
        cnt = self.products.pop(item, None)

        return cnt

    def get_item(self, item):
        return self.products.get(item)

    def get_total_value(self):
       total = 0
       for key, cnt in self.products.items():
           total+=key.price * cnt

       return total
    def __str__(self):
        tmp = ''
        for item, cnt in self.products.items():
            tmp +=f"{str(item)}:{cnt} pcs.\n"

        return f"Basket contains: \n{tmp}"
cart = Purchase(buyer1)
cart.add_item_to_basket(lemon, 4)
cart.add_item_to_basket(apple, 20)
print(cart)

# new_basket = Purchase(buyer1)
# print(new_basket.get_total_value())
#
# new_basket.add_item_to_basket(lemon, 10)
# new_basket.add_item_to_basket(cherry, 20)
# print(new_basket.get_total_value())
# print(new_basket.get_item(lemon), "lemons in the basket")











