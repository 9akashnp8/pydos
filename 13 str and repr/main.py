# str used to convert object to string
# repr used to return an unambigious representation
# unambigiour as in, for example, we don't know the type
# of the output.

# print uses str, thus all of it's output is string.
# we won;t be able to tell if the arguement was integer
# or something else because print converts it to string
# via str.
print(4)
# Output: 4
print("4")
# Output: 4

# Instead if you simple write the number in repl, it will
# return an unambigious representation
4
# Output: 4
"4"
# Output: '4'
# Here we can tell what type the argument is, that's the benefit
# of repr.

# printing containers like lists and dicts also use repr
# under the hood
print([3, "3"])
# Output = [3, "3"]

# __str__ and __repr__ dunder methods
# By default how python displays and object is
# not very helpful
# a = A()
# a
# <__main__.A object at 0x12314>

# The __str__ and __repr__ dunder methods can help you better
# represent your object, similar to the use case menioned using
# the respective built in functions
class A:
    def __str__(self):
        return "A"
a = A()
a
# Output: <__main__.A object at 0x232343>
print(a)
# Output: A

class B:
    def __repr__(self) -> str:
        return "B"
b = B()
b
# Output: 'B'
print(b)
# Output: 'B'

# Notice how if only the __repr__ method is defined,
# Python takes that implementation for __str__ as well.
# If only __str__ is defined, __repr__ still is left
# unimplemented. It is recommended to implement __repr__
# first
import datetime
date = datetime.datetime(2021, 2, 2)
print(repr(date))
# Output: datetime.datetime(2021, 2, 2, 0, 0)
print(str(date))
# Output: 2021-02-02 00:00:00

# Notice how we can recreate the date object using
# it's repr
date = eval(repr(date))
# Output: True