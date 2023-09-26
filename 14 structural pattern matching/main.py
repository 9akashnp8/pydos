color = (25, 56, 100)

match color:
    case r, g, b:
        print("No Alpha")
    case r, g, b, alpha:
        print(f"Alpha is {alpha}")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1) # 5x4x3x2x1

def factorial(n):
    match n:
        case 0 | 1:
            return 1
        case _:
            return n * factorial(n-1)

def normalise_color_info(color):
    # Normalise color info to (name, (r, g, b, a))
    match color:
        case (r, g, b):
            name = ""
            a = 0
        case (r, g, b, a):
            name = ""
        case (name, (r, g, b)):
            a = 0
        case (name, (r, g, b, a)):
            pass
        case _:
            raise ValueError("Unknow color info format")
    return (name, (r, g, b, a))

# We can also match the structure of object instances.
class Point2D():

    def __init__(self, x, y):
        self.x = x
        self.y = y

def describe_point(point):
    match point:
        case Point2D(x=0, y=0):
            desc = "at the origin"
        case Point2D(x=x, y=y) if x ==y:
            desc = f"along the x = y line"

# Notice how we have to specify x and y values like keyword
# arguments everytime, we can skip that using __match_args__
# with __match_args__, we can tell python how to match
# the attributes of our object in 'match'

class Point2DV2():

    __match_args__ = ["x", "y"]
    def __init__(self, x, y):
        self.x = x
        self.y = y

def describe_point_v2(point):
    match(point):
        case Point2DV2(0 , 0):
            desc = "at origin"
        case Point2DV2(x, 0):
            desc = "in the horizontal axis"

# Matching wildcards
# We can used asterisk (*) to match wildcards in list or tuple
seq = [1, 2, 3, 4]
new_seq = []
match seq:
    case [x, y, z, *tail] if x == y == z:
        new_seq.extend([3, x]) # 222 becomes 32
    case [x, y, *tail] if x == y:
        new_seq.extend([2, x]) # 22 becomes 22
    case [x, *tail]:
        new_seq.extend([1, x]) # 1 becomes 1

# We can use (**) to match wildcards in a dict
d = {0: "oi", 1: "uno"}
match d:
    case {0: "oi"}:
        print("yeah")
# Output: "yeah"

# When matching dictionories, only structure that was
# sepcified is important, any other extra keys that exists
# on the original dict are ignored. This is why the above
# example prints "yeah". Lists and tuples on the otherhand
# must have exact match.

# If you want to acces the extra keys, you can use a (**)
# wildcard.
d = {0: "oi", 1: "uno"}
match d:
    case {0: "oi", **remainder}:
        print(remainder)
# Output: {1: "uno"}

# To match dict with only specified keys:
d = {0: "oi", 1: "uno"}
match d:
    case {0: "oi", **remainder} if not remainder: # <= here
        print("only specified key")
    case {0: "oi"}:
        print("other keys present")

# Instead of specifying value, you can also destructure it
# from the dict
d = {0: "oi", 1: "uno"}
match d:
    case {0: zero_val, 1: one_val}:
        print(f"0 is mapped to {zero_val}, 1 is mapped to {one_val}")

# Naming Sub Patterns
# Wouln't it be nice if we could give a name to a part of
# the pattern (Or the whole thing?)
def go(direction):
    match direction:
        case "North" | "East" | "South" | "West": # <- here the whole pattern is named, either North, East, South or West
            return "Alright! I'm going"
        case _:
            return "I can't go that way..."

print(go("North")) # Alright, I'm going
print(go("asddfg")) # I can't go that way

# We can also name part of the pattern
def act(command: str):
    match command.split():
        case "Cook", "breakfast":
            return "I love breakfast"
        case "Cook", *wtv:
            return "Cooking..."
        case "Go", "North" | "South" | "East" | "West": # <- we've named the pattern Go
            return "Alright! I'm going"
        case "Go", *wtv: # <- we've named the pattern Go
            return "I can't go that way"
        case _:
            return "I can't do that"

print(act("Go North")) # Alright! I'm going 

# Notice how I can match the pattern with name "Go" and subsequent
# value is matched based on the cases in match

# We can also capture the result of a match using "as" keyword
def act(command: str):
    match command.split():
        case "Cook", "breakfast":
            return "I love breakfast"
        case "Cook", *wtv:
            return "Cooking..."
        case "Go", "North" | "South" | "East" | "West" as direction: # <- we're storing the result of match
            return f"Alright! I'm going {direction}"
        case "Go", *wtv: # <- we've named the pattern Go
            return "I can't go that way"
        case _:
            return "I can't do that"

print(act("Go North")) # Alright! I'm going North