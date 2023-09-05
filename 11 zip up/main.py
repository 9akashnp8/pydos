# zip() is a built-in function that allows traversing multiple
# iterators together. 

firsts = ["Anna", "Bob", "Charles"]
lasts = ["Smith", "Doe", "Evans"]
for first, last in zip(firsts, lasts):
    print(f"{first} {last}")

# Output:
# Anna Smith
# Bob Doe
# Charles Evans

# Internally, zip creates a tuple containing the items of the
# iterators each iteration.
firsts = ["Anna", "Bob", "Charles"]
lasts = ["Smith", "Doe", "Evans"]
for z in zip(firsts, lasts):
    print(z)

# Output:
# ('Anna', 'Smith')
# ('Bob', 'Doe')
# ('Charles', 'Evans')

# Because it's a tuple, we can unpack the tuple into
# it's respective variables (see first example)

# Zip is lazy, it is computed only when asked.
# Eg: when you iterate over them in a for loop
# or convert the zip into a list.

# Zip can take an arbitrary number of iterators and will produce a tuple of
# the appropriate size.

# >>> firsts = ["Anna", "Bob", "Charles"]
# >>> middles = ["Z.", "A.", "G."]
# >>> lasts = ["Smith", "Doe", "Evans"]
# >>> for z in zip(firsts, middles, lasts):
# ... print(z)
# ...
# ('Anna', 'Z.', 'Smith')
# ('Bob', 'A.', 'Doe')
# ('Charles', 'G.', 'Evans')

# Zip will create tuples as long as there are appropriate
# number of matching items in the iterator. If matching
# item is not found, zip stops safely. We can configure
# zip to raise error (>=3.10) by using strict=True.
# If you expect the iterators to be same length, then it is a
# good idea to use strict=True to catch bugs easily.

# If you have tuple in which first item is key and second item is value,
# then you can create a dictionary by passing the tuple to dict function.
# which means the zip() method can be used to convert two iterators
# which contain keys and values respectively, into a dict.
firsts = ["Anna", "Bob", "Charles"]
lasts = ["Smith", "Doe", "Evans"]
dict(zip(firsts, lasts))
# {'Anna': 'Smith', 'Bob': 'Doe', 'Charles': 'Evans'}


