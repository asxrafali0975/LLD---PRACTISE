from typing_extensions import Self

from threading import Lock


class Product:
    def __init__(
        self, product_id: str, price_per_item: int, product_quantity: int
    ) -> None:
        self.product_id = product_id
        self.price_per_item = price_per_item
        self.product_quantity = product_quantity


class Inventory:
    _instance = None
    _lock = Lock()

    def __new__(cls) -> Self:

        if cls._instance == None:
            with cls._lock:
                if cls._instance == None:
                    cls._instance = super().__new__(cls)
                    cls._instance.items_list = {}
                    cls._instance.initialized = False
        return cls._instance

    def __init__(self) -> None:
        if self._instance.initialized == False:
            self.items_list = dict({})
            self._instance.initialized = True

    def add_to_inventory(self, prod: Product):
        # if already exists do nothing
        with self._lock:
            if not self.items_list.get(prod.product_id):
                self.items_list[prod.product_id] = prod

    def update_price(self, prod: Product, new_price: int):
        if new_price <= 0:
            print("error : price cannot be 0 or less")
            return
        with self._lock:
            self.items_list[prod.product_id].price_per_item = new_price
        print("updated")

    def update_quantity(self, prod: Product, new_quantity: int):
        if new_quantity < 0:
            print("quantity cannot be in negative")
            return
        with self._lock:
            self.items_list[prod.product_id].product_quantity = new_quantity
        print("updated")

    def remove_product(self, product_id: str):
        if self.items_list.get(product_id):
            del self.items_list[product_id]
        pass

    def view_inventory(self):
        if not len(self.items_list):
            print("Inventory is empty")
            return

        for key in self.items_list:
            print(
                f"product_id = {key} , price_per_item = {self.items_list[key].price_per_item } , quantity = {self.items_list[key].product_quantity} "
            )


class CustomerCart:

    def __init__(self) -> None:
        self.cart = {}
        self.inventory = Inventory()
        self.lock = Lock()

    def add_item(self, product_id: str, quantity: int):
        if self.inventory.items_list.get(product_id):
            with self.lock:
                if (
                    self.inventory.items_list.get(product_id).product_quantity
                    >= quantity
                ):
                    self.cart[product_id] = self.cart.get(product_id, 0) + quantity
                    print(f" {product_id} added to cart !!")
                else:
                    print("item quanity not available right now")

        else:
            print("item not found")

    def remove_item(self, product_id: str):
        if self.cart.get(product_id):
            with self.lock:
                del self.cart[product_id]
                print(f"item with id : {product_id} removed from cart")
        else:
            print("item not found in cart !!")

    def update_quanity(self, product_id: str, new_quantity: int):
        if self.cart.get(product_id):
            with self.lock:
                if (
                    self.inventory.items_list.get(product_id).product_quantity
                    >= new_quantity
                ):
                    self.cart[product_id] = new_quantity
                    print("quantity upgraded !!")
                else:
                    print("item quanity not available right now")
        else:
            print("item not found")

        pass

    def view_cart(self):
        if len(self.cart):
            for keys in self.cart:
                print(f"[product_id = {keys} , quanitity = {self.cart[keys]}  ]")
        else:
            print("your cart is empty !!")
        pass


class CheckOut:
    def __init__(self) -> None:
        self.inventory = Inventory()

    def checkout(self, costumer_cart: CustomerCart):

        gross_total = 0
        items_to_remove = []

        with self.inventory._lock:
            for product_id in costumer_cart.cart:
                product = self.inventory.items_list.get(product_id)
                price_per_itm = product.price_per_item
                inventory_quantity = product.product_quantity
                cart_quantity = costumer_cart.cart.get(product_id)
                if cart_quantity > inventory_quantity:
                    print(
                        f"Sorry product : {product_id} stocks are limited , deleting that product from your account"
                    )
                    items_to_remove.append(product_id)

            for product_id in items_to_remove:
                del costumer_cart.cart[product_id]

            for product_id in costumer_cart.cart:
                product = self.inventory.items_list.get(product_id)
                price_per_itm = product.price_per_item
                inventory_quantity = product.product_quantity
                cart_quantity = costumer_cart.cart.get(product_id)

                total_price = price_per_itm * cart_quantity
                gross_total += total_price

                self.inventory.items_list[product_id].product_quantity -= cart_quantity

        print("your items are : ")

        costumer_cart.view_cart()

        costumer_cart.cart.clear()

        print(f"total amount is  : {gross_total}")

    pass


"""
items_list = 

items_name    price per item        total quantity

onion          50                    10
tomato         30                    20
iphone         70                    50,000

i better create object 

"""

if __name__ == "__main__":
    inventory = Inventory()

    onion = Product("onion", 50, 10)
    potato = Product("potato", 20, 10)
    iphone_17 = Product("iphone 17", 50000, 10)
    iphone_case = Product("iphone case transparent", 300, 50)

    inventory.add_to_inventory(onion)
    inventory.add_to_inventory(potato)
    inventory.add_to_inventory(iphone_17)
    inventory.add_to_inventory(iphone_case)

    ashcart = CustomerCart()
    ashcart.add_item(onion.product_id, 2)
    ashcart.add_item(potato.product_id, 1)
    ashcart.add_item(iphone_17.product_id, 1)

    ashcart.view_cart()
