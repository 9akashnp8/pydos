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
