# Multiple Assignments
name, age = ("Akash", 24)
print(name, age)

# Starred Assignments
name, *other_info = ("Akash", 24, "M")
print(name, other_info)

# Deep unpacking
# It is unpacking by matching the shape of the value in LHS,
profile_info = ("Akash", (24, "M"))
name, (age, sex) = profile_info # notice how the RHS matches the shape of LHS
# (name, (age, sex)) = ("Akash", (24, "M")) # Alternative where we match the outer parenthesis as well
print(name, age, sex)

# Deep unpacking can also be done when looping
profiles = [
    ("Akash", (24, "M")),
    ("Akash2", (32, "M")),
    ("Akas3", (42, "M"))
]
age_squares = [
    age**2 for (name, (age, sex)) in profiles
]
print(age_squares)

# Deep unpacking helps in debugging as wherever it is used
# It sets an expected shaped. Eg: (a, b, c), a tuple with 3
# items. If anything is passed that doesn't comply to this
# shape then Python would throw a Value error stating too
# many values to unpack.