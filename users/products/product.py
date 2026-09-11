products = []

def add_product(name, price):
    product = {
        "name": name,
        "price": price
    }
    products.append(product)

def display_products():
    for product in products:
        print(product)
