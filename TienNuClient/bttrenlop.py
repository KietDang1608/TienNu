products = [
    {"id":1, "name":"Huu khung", "price": "3"},
    {"id":2, "name":"Hung khung", "price": "400"},
    {"id":3, "name":"Dat khung", "price": "500"},
    {"id":4, "name":"Khoi khung", "price": "600"},
]
def getPrice(product):
    return float(product["price"])

# print(sum(list(map(getPrice, products))))

expression = "2 + 3 * (5 - 2) / 4"

print(eval(expression))
