# Deep Unpacking

## Introduction

"Unpacking" is a more elegant and short way of assigning variables. For example, with regular assignment, one would have to do the following to assigned variables from a list

```python
people = ["Akash", "Adarsh"]
first_person = people[0]
second_person = people[1]
```

With *Multiple Assignment*, you can rewrite like this: 

```python
first_person, second_persion = people[0], people[1]
```

Now, with *Deep Unpacking*, you can rewrite like this:

```python
first_person, second_person = people
```
## Deep Unpacking

Deep Unpacking is similar to Multiple Assignment, as in, they both match the LHS and RHS but while Multiple Assignment matches the length of iterable on RHS to get each in a variable on LHS, with Deep Unpacking, you match the shape of iterable on RHS to extract each value from the same.

```python
color_info = ("Alice Blue", (240, 248, 255))
name, (r, g, b) = color_info
print(g)
# 248
```

Notice how, on the LHS we have matched the exact shape of RHS and this has allowed to extract the requirement information (rgb color values) more elegantly.
## In Loops

Deep Unpacking can also be used in loops, for example:

```python
people = ["Akash", "Adarsh"]
for index, item in enumerate(people):
	print(index, item)
```

Notice how we unpacked the tuple that the `enumerate` function would return in the loop statement itself. You can also use unpacking in list comprehensions.

```python
colors = [("Alice", (100, 200)), ("Akash", (100, 200))]
names = [name for (name, (r, g)) in colors]
print(names)
# ["Alice", "Akash"]
```
## Catching Bugs

With unpacking, since we are matching the shape on both sides, attempting to unpack any wrong shape will result in a error. Let's take an example where there is a bug wherein for the data being used, instead of just r and g values, another function also added b values. This is not expected behavior but with unpacking, using just indexing, this abnormal behavior would not come to our notice and might affect code elsewhere but with unpacking as the shape doesn't match, a ValueError is raised this allowing us to catch bugs faster.

```python
colors = [("Alice", (100, 200)), ("Akash", (100, 200, 300))]
names = [name for (name, (r, g)) in colors]
# ValueError: too many values to unpack (expected 2)
```






