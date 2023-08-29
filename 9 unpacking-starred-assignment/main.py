# Assign single element to a named variables, store the rest in anoher

first, *remaining = [1, 2, 3, 4, 5]
print(first, remaining)

first, *remaining = [1] # only one * is allowed
print(first, remaining)

first, *rest, last = [1, 2, 3, 4, 5]
print(first, rest, last)