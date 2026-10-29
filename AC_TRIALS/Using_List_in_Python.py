## INPUT FUNCTION
# age = input("What is Your age? ")
#print("Your age is " + age)

# LIST IS IMPORTANT IN PYTHON DATA STRUCTURE
dogs = ["Roger", 1, "Syd", True, "Quincy", 70]

print("Syd" in dogs)
print("Josh" in dogs)
print(dogs[0])
print(dogs[2])

# Modifying an item in the List
dogs[2] = "Bingo"
print(dogs)
print(dogs[-1])
print(dogs[2:4])
print(dogs[2:])
print(dogs[:4])
print(len(dogs))

dogs.append("Judah")
print(dogs)
dogs.extend(["billy", 8])
print(dogs)
# Extending a list using the += operator
dogs += ["mophy", 13] # The += operator does the same thing like the .extend method
print(dogs)


dogs.remove("Quincy")
print(dogs)
print(dogs.pop())
print(dogs)


# How to add another item in the middle of the list at a specific index:
items = ["Roger", 1, "Syd", True, "Quincy", 70]
items.insert(2, "Test")
print(items)

#Using slices to add multiple items to a particular index of a list
items[1:1] = ["Test1", "Test2"]
print(items)

#To use the sort method on a list, all the items in the list must be of the same DataType.
items2 = ["Mike", "Sam", "Jon", "bob", "Lim", "Berry"]
items2copy = items2[:]

items2.sort()
print(items2)
items2.sort(key=str.lower) # Ensures that the lowercase item is not left for last instead of alphabetic order.
print(items2)
print(items2copy)

# Another way to sort a list without modifying the original list
items3 = ["Dave", "Zoe", "Miriam", "Baze", "Pascal", "ben"]
print(sorted(items3, key=str.lower))
print(items3)