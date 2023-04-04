books = [
    {"title" : "good",
    "price" : 3200},
    {"title" : "hello",
    "price" : 2000},
    {"title" : "bye",
    "price" : 4500},
]

def get_price(book):
    return book["price"]
print(min(books, key=get_price)) # {'title': 'hello', 'price': 2000}

print(min(books, key=lambda book: book["price"])) # {'title': 'hello', 'price': 2000}

from operator import itemgetter
print(min(books, key=itemgetter("price"))) # {'title': 'hello', 'price': 2000}