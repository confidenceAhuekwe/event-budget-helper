#Tuples are another fundamental Python Data structures used to create IMMUTABLE groups of objects.
#By Immutable it means you cannot modify a tuple. However, you can create a new tuple from an existing tuple
names = ("Roger", "Syd", "Albert")

print(names[0])
print(names[-1])
print(names.index("Roger"))

print("Roger" in names)

#Using SORT in TUPLES
print(sorted(names))
print(names)

#Creating a new Tuple from an Existing Tuple
newTuple = names + ("Tina", "Quincy")
print(newTuple)