"""conversion of one datatype into another
is knows as type-casting.
there are two types of type-casting
Implicit type conversion and explicit type conversion

1. Implicit -- where python itself change datatype.
2. Explicit -- where user change the datatype.
"""
#-----------Implicit conversion-----------------------
a=123
b=1.23

print(type(a))
print(type(b))

c=a+b
print(c)
print(type(c))
#------------explicit-conversion----------------------
a="123"
b=1.23

print(type(a))
print(type(b))
a = int(a)
print("type after", type(a))
c=a+b
print(c)
print(type(c))


