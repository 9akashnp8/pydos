# the built in enumerate function can be useful when
# you need the index as well as the item being loop.
words = ["Hey", "there"]
for i, word in enumerate(words):
    print(i, word)
# 0 Hey
# 1 there

# You can also do this with zip
for i, word in zip(range(len(words)), words):
    print(i, word)
# here range(len(word)) gives us an iterator
# that iterats from 0 to the length of the words list (2)

# The start argument
# It allows you to specify the first index i.e., start from what number
for i, word in enumerate(words, start=1):
    print(i, word)
# 1 Hey
# 2 there

# start has to be an integer but it can be negative
for i, word in enumerate(words, start=-3500):
    print(i, word)
# -3500 Hey
# -3499 there

# When iterating, enumerates gives us a 2-item tuple
# (x, y) where x is the index and y the value/item
# that is why we can unpack in the loop statement itself.
for tup in enumerate(words):
    print(tup)
# (0, Hey)
# (1, there)

# We can also deep unpack the 2nd item in the tuple depending
# on what it's structure is. For eg:
pages = [5, 17, 41, 50]
for i, (start, end) in enumerate(zip(pages, pages[1:]), start=1):
    print(f"#{i}: {end-start} pages long")
# 1: 12 pages long
# 2: 24 pages long
# 3: 9 pages long
