# Sequence Indexing

"Sequences" in python are Strings, Lists and Tuples. All three support indexing wherein you can access a specific item from the sequence by providing the index (position) of the item in the sequence.

To index a sequence,
- refer the variable and use square brackets along with the integer that corresponds to the required characted
- Python is 0-indexed i.e., it starts counting from 0 i.e., the index of the very first element will be 0, the second will be 1 and so on.

```py
s = "Indexing is easy"
s[0]
>>> "I"
```

## Maximum Legal Index and Index Errors
Since sequences are finite, there is a "maximum legal index" that exists i.e., the highest index you can specify i.e., the last most character. Now since Python is 0-indexed, this limit is: **Length of the sequence, _minus one_**

```py
>>> s = "Indexing is easy!"
>>> len(s)
17
>>> s[16]
'!'
>>> s[17]
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
IndexError: string index out of range
```

## Negative Indices
We've seen above, to access the last element we can use `len(s)-1` but Python providers another method: "Negative indexing" to access elements in reverse. Using this, the last element can be accessed via `s[-1]`, the second last `s[-2]` so on and so forth.

NOTE: When negative indexing, the last element from reverse can be accessed via s[-<len of s>] i.e., `s[-17]` (as opposed to s[len(s) - 1] when positive indexing)

## Best Practices in Code

### A Looping pattern with range
We know that characters can be accessed via the index of the character in the sequence. This, coupled with our knowledge or range() means we can loop through items in a sequence by `for chat in range(len(s))` where s is a sequence.

But with Python, you can directly access items in a sequence. `for letter in word` where word is a string sequence.

### Large expressions as indices
When attempting to access an item from sequence, we might need to perform some calculation. Instead of using the calculation in the index sytax `s = seq[len(s)/2]`, move the calculation to another variable with meaningful name.

This will ensure that the code is readable and no unwanted comments is required for further clarification.

### Unpacking with indexing
When accessing a well know sequence, it might be more better to unpack the items instead of indexing it

```py
names = ["First", "Last"]
if condition:
    return name[0]
else:
    return name[1]

names ["First", "Last"]
first, last = names
if condition:
    return first
else:
    return last
```

By unpacking, sure, we've added an extra line but we've made the code's intent more easily understandable and also easier to debug as now if the names contain less or more than 2 items, we get an "ValueError: ... expected 2" which allows the invoker for the function to find what's missing.