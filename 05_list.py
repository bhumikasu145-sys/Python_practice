🐍 Python Lists

📌 Introduction

A List in Python is a collection used to store multiple values in a single variable. Lists are ordered, mutable, and allow duplicate values.

Lists can store different types of data such as integers, strings, floats, and even other lists.

Example

numbers = [10, 20, 30, 40, 50]
print(numbers)

Output:

[10, 20, 30, 40, 50]

---

🔹 Creating a List

A list is created using square brackets "[]".

fruits = ["Apple", "Mango", "Orange"]
print(fruits)

---

🔹 List with Different Data Types

data = [10, "Python", 3.14, True]
print(data)

A list can contain different types of values.

---

🔹 Accessing List Elements

List indexing starts from 0.

fruits = ["Apple", "Mango", "Orange"]

print(fruits[0])
print(fruits[1])

Output:

Apple
Mango

Negative Indexing

print(fruits[-1])

Output:

Orange

---

🔹 Changing List Elements

Lists are mutable, which means their values can be changed.

fruits = ["Apple", "Mango", "Orange"]

fruits[1] = "Banana"

print(fruits)

Output:

['Apple', 'Banana', 'Orange']

---

🔹 Adding Elements

"append()"

Adds an element at the end.

fruits = ["Apple", "Mango"]
fruits.append("Orange")

print(fruits)

"insert()"

Adds an element at a specific position.

fruits.insert(1, "Banana")
print(fruits)

"extend()"

Adds multiple elements.

fruits.extend(["Grapes", "Pineapple"])
print(fruits)

---

🔹 Removing Elements

"remove()"

fruits.remove("Mango")

"pop()"

Removes an element using its index.

fruits.pop(0)

"del"

del fruits[1]

"clear()"

Removes all elements.

fruits.clear()

---

🔹 List Slicing

Slicing is used to get a part of a list.

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])

Output:

[20, 30, 40]

---

🔹 Important List Methods

Method| Purpose
"append()"| Adds an element
"insert()"| Adds at a specific position
"extend()"| Adds multiple elements
"remove()"| Removes a specified element
"pop()"| Removes an element by index
"clear()"| Removes all elements
"sort()"| Sorts the list
"reverse()"| Reverses the list
"index()"| Finds the position of an element
"count()"| Counts an element

Example

numbers = [30, 10, 20, 10, 40]

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

print(numbers.count(10))

---

🔹 Looping Through a List

fruits = ["Apple", "Mango", "Orange"]

for fruit in fruits:
    print(fruit)

Output:

Apple
Mango
Orange

---

🔹 Checking an Element

The "in" operator checks whether an element exists in a list.

fruits = ["Apple", "Mango", "Orange"]

if "Mango" in fruits:
    print("Mango is available")

---

🔹 Finding Length of a List

The "len()" function returns the number of elements.

numbers = [10, 20, 30, 40]

print(len(numbers))

Output:

4

---

🔹 List Comprehension

List comprehension provides a short way to create a list.

numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]

print(squares)

Output:

[1, 4, 9, 16, 25]

---

🔹 Nested Lists

A list can contain another list.

students = [
    ["Bhumika", 85],
    ["Anu", 90],
    ["Ravi", 78]
]

print(students[0])

Output:

['Bhumika', 85]

---

🔹 Advantages of Lists

- ✅ Easy to create and use
- ✅ Can store multiple values
- ✅ Allows duplicate elements
- ✅ Supports different data types
- ✅ Mutable — elements can be changed
- ✅ Supports indexing and slicing
- ✅ Many built-in methods are available
- ✅ Useful for storing and processing collections of data

---

🔹 Disadvantages of Lists

- ❌ Lists can use more memory than some other data structures
- ❌ Searching for an element can be slower for large lists
- ❌ Because lists are mutable, data can be changed accidentally
- ❌ Not ideal when data should remain unchanged
- ❌ Inserting or deleting elements in the middle can be slower

---

🔹 Real-World Example

A shopping cart can be represented using a list:

cart = ["Laptop", "Mouse", "Keyboard"]

cart.append("Headphones")

print("Shopping Cart:")
for item in cart:
    print(item)

Output:

Shopping Cart:
Laptop
Mouse
Keyboard
Headphones

---

📌 Key Points

List
 ↓
Ordered
 ↓
Mutable
 ↓
Allows Duplicates
 ↓
Uses []
 ↓
Supports Indexing & Slicing
 ↓
Supports Many Built-in Methods

Example

my_list = [10, 20, 30, 20]

print(my_list[0])       # Access
my_list.append(40)      # Add
my_list.remove(20)      # Remove
my_list[0] = 100        # Update

print(my_list)

---

🎯 Conclusion

Python Lists are one of the most commonly used data structures in Python. They are simple, flexible, and useful for storing and manipulating collections of data. Understanding lists is important before learning other Python data structures such as Tuples, Sets, and Dictionaries.

---