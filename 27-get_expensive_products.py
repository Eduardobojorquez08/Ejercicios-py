products = {
    "laptop": 15000,
    "mouse": 350,
    "keyboard": 800,
    "monitor": 8500,
    "headphones": 1200,
    "webcam": 950
}

def get_expensive(products, n):
    expensive_products = {}
    for key, value in products.items():
        if value >= n:
            expensive_products[key] = value
    return expensive_products
print(get_expensive(products, 800))
