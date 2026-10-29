name = "Beau"; print(name)
age = float(39)
print(type(name) == str)
print(isinstance(name, str))

print(isinstance(age, float))

# OR Operators
print(0 or 1) ##1
print(False or 'hey') ##outputs hey
print('hi' or 'hey') ##outputs hi
print([] or False) ##outputs False
print(False or []) ##outputs []

# AND Operators
print(0 and 1) ##0
print(1 and 0) ##outputs 0
print(False and 'hey') ##outputs False
print('hi' and 'hey') ##outputs hey
print([] and False) ##outputs []
print(False and []) ##outputs False

print("""Beau

is coming

Tomorrow""")

# Methods in Python
print("beau".upper())