def main():
    #create somme items
    item1 = Item("Apple", 0.5, 10)
    item2 = Item("Banana", 0.3, 5)
    item3 = Item("Orange", 0.8, 8)

    #create a cart
    my_cart = Cart()

    #add items to the cart
    my_cart.add_items(item1)
    my_cart.add_items(item2)
    my_cart.add_items(item3)

    #print total price
    print(my_cart)
    print(f"Total price: ${my_cart.total_price():.2f}")
    
    




class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


    @property
    def name(self):
        return self.__name 
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) <1:
            raise ValueError("Name must be at least 1 character long")
        self.__name = name

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number")
        if price < 0 :
            raise ValueError("Price must be greater than or equal to 0")
        self.__price = price

   
    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity):
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer")
        if quantity < 0:
            raise ValueError("Quantity must be greater than or equal to 0")
        self.__quantity = quantity


class Cart:
    def __init__(self):
        self.items = []

    def add_items(self, item):
        for i in self.items:
            if i.name == item.name:
                i.quantity += item.quantity
                return
        self.items.append(item)

    def remove_items(self, item_name):
        for i in self.items:
            if i.name == item_name:
                self.items.remove(i)
                return
        raise ValueError(f"Item '{item_name}' not found in cart")

    def total_price(self):
        total = 0
        for i in self.items:
            total += i.price * i.quantity
        return total
    def __str__(self):
        if not self.items:
            return "Cart is empty"
        items_str = [f"{i.name}: {i.quantity} @ ${i.price:.2f} {i.quantity*i.price}" for i in self.items]
        return "\n".join(items_str)



if __name__ == "__main__":
    main()