
# ----------------------------------------------------------------------------------------------------------- 
# --------------- new_list = [expression for item in iterable] ---------------------------------------------- الشكل الاساسي
# --------------- new_list = [expression for item in iterable if condition] --------------------------------- مع شرط التصفية 
# --------------- new_list = [value_if_true if condition else value_if_false for item in iterable] ---------- لو عايز تختار قمية حسب شرط



# 1. Normal For Loop

numbers = []

for i in range(1, 6):
    numbers.append(i)

print(numbers)


# 2. List Comprehension

numbers = [i for i in range(1, 6)]

print(numbers)
# [1, 2, 3, 4, 5]


# 3. Apply an Operation

squares = [i ** 2 for i in range(1, 6)]

print(squares)
# [1, 4, 9, 16, 25]


# 4. Add a Condition

even_numbers = [i for i in range(1, 11) if i % 2 == 0]

print(even_numbers)
# [2, 4, 6, 8, 10]


# 5. If / Else in Comprehension

results = [
    "Even" if i % 2 == 0 else "Odd"
    for i in range(1, 6)
]

print(results)
# ['Odd', 'Even', 'Odd', 'Even', 'Odd']


# 6. Convert Strings

names = ["ali", "mohamed", "omar"]

capitalized_names = [name.capitalize() for name in names]

print(capitalized_names)


# 7. Filter Strings

long_names = [name for name in names if len(name) > 3]

print(long_names)


# 8. Work with Existing Lists

numbers = [2, 4, 6, 8]

doubled = [number * 2 for number in numbers]

print(doubled)
# [4, 8, 12, 16]




