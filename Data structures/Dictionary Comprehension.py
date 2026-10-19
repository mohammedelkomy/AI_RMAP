
# new_dict = {key_expression: value_expression for item in iterable} القاعده العامه 

# new_dict = {
#     key: value
#     for item in iterable        
#     if condition                   >> مع شرط 
# }




# 1. Create a Dictionary from a Loop

squares = {}

for i in range(1, 6):
    squares[i] = i ** 2

print(squares)


# 2. Dictionary Comprehension

squares = {i: i ** 2 for i in range(1, 6)}

print(squares)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# 3. Convert List to Dictionary

names = ["Ali", "Mohamed", "Omar"]

name_lengths = {name: len(name) for name in names}

print(name_lengths)


# 4. Add a Condition

numbers = range(1, 11)

even_squares = {
    i: i ** 2
    for i in numbers
    if i % 2 == 0
}

print(even_squares)


# 5. Use Existing Dictionary

prices = {
    "Laptop": 20000,
    "Phone": 10000,
    "Mouse": 500
}

discounted_prices = {
    item: price * 0.9
    for item, price in prices.items()
}

print(discounted_prices)


# 6. Filter a Dictionary

prices = {
    "Laptop": 20000,
    "Phone": 10000,
    "Mouse": 500
}

expensive_items = {
    item: price
    for item, price in prices.items()
    if price > 1000
}

print(expensive_items)
