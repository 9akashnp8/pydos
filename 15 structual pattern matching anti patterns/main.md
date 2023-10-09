# Structural pattern matching anti-patterns

The `match` statement might look similar to `switch` but it is infact
much more powerful that `switch`.

# When/How NOT to use match

1. You have only a couple of options and you are checking for strict equality (no pattern)

```py
while n != 1:
    match n % 2:
        case 0:
            n //= 2
        case 1:
            n = 3*n + 1
```

```py
while n != 1:
    if n % 2:
         = 3*n + 1
    else:
        n //= 2
```
Notice how we have implemented the same logic but save 1 line of code and 1 level of indentation

2. Sometimes you might feel like you have a list of cases and corresponding values, so that you can map one to the other. However, it might be that there exists an algorithm or formula that makes things much simpler.

```py
def rule30(bits):
    match bits:
        case 0, 0, 0:
            return 0
        case 0, 0, 1:
            return 1
        # ... so on for 16 cases
```
Instead if we research a bit more, we can find there exists a solid formula that calculates the result of inputed bits

```py
def rule30(bits):
    p, q, r = bits
    return (p + q + r + q*r) % 2
```
This solid formula is much more cleaner and simpler than using a `match`

3. Having nested matches

Instead of having nested matches like

```py
match key:
    case a:
        return a
    case b:
        return b
    case c:
        match key2:
            case d:
                return d
            case e:
                return d
```

We can extract the inner match to it's own function, better yet, to ensure that the function doesn't grow vertically for every new operation (it would add 2 lines), we can implement a dictionary for mapping.

```py

def op_to_str(op):
    ops = {
        ast.Add: "+",
        ast.Sub: "-",
        ...
    }
    return ops.get(op.__class__, None)

```

Here you implement the same logic but via dictionaty mapping instead of match. This is much more cleaner as 1) we get the same functionality that is required & 2) It doesn't too much vertical or horizontal space