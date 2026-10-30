from model.productmodel import Product

products = {}

def create_product(product: Product):
    if product.id in products:
        return None
    products[product.id] = product
    return product

def get_all_products():
    return list(products.values())

def get_product(product_id: int):
    return products.get(product_id)

def update_product(product_id: int, product: Product):
    if product_id not in products:
        return None
    products[product_id] = product
    return product

def delete_product(product_id: int):
    if product_id not in products:
        return False
    del products[product_id]
    return True