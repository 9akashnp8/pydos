# Structural pattern matching anti-patterns

The `match` statement might look similar to `switch` but it is infact
much more powerful that `switch`.

# When/How NOT to use match

1. You have only a couple of options and you are checking for strict equality (no pattern)

```python
while n != 1:
    match n % 2:
        case 0:
            n //= 2
        case 1:
            n = 3*n + 1
```

```python
while n != 1:
    if n % 2:
         = 3*n + 1
    else:
        n //= 2
```
Notice how we have implemented the same logic but save 1 line of code and 1 level of indentation