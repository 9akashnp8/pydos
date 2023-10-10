# Idiomatic Sequence Slicing

Slicing is a more "advanced" way of accessing portions of sequences (like lists and tuples). Slicing is the act of accessing a sequence of elements that are extracted from successive positions of a larger sequence.

To Slice, you need to use brackets [] and a color : to separate the start and end points. How we identify the points are using the indexes of the sequence.

Word: "EXAMPLE"

Indexes:
| E | X | A | M | P | L | E
0   1   2   3   4   5   6   7

With the above, you can visualize indexes. The "character"/item belongs to the number behind it i.e., "E" is 0th index, "X" is 1st index

Coming to slicing, to extract the "amp" sequence, you can get it throught the following:

```py
word = "EXAMPLE"
seq = word[2:5]
>>> amp
```
The start and end points give you the bar that enclose what you will extract

