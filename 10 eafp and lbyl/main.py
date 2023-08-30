# EAFP: Easier to Ask for Forgiveness than for Permission
# - run operate and handle any exception that might raise using try block
# LBYL: Look Before You Leap
# - check if the operation can be run before procceding.

# EAFP is more advantageous
# Example with LBYL:
d = {"a": 1, "b": 2}
print("What key do you want to access?")
key = input(" >> ")
if key in d: # access key once
    print(d[key]) # access key again
else:
    print(f"Cannot find {key} in {d}")
# Similar example with EAFP
try:
    print(d[key]) # accessed and used in one go
except KeyError:
    print(f"Cannot find key {key} in {d}")

# Sample inbuild method with EAFP like behaviour
# dict.get()
print(d.get(key, None))
