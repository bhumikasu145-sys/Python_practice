🐍 Python Tuples – Complete Guide

Welcome to this guide on Python Tuples!
This README covers everything from basics to advanced concepts with examples.

---

📌 What is a Tuple?

A tuple is a collection of items that is:

- ✅ Ordered
- ✅ Immutable (cannot be changed)
- ✅ Allows duplicate values

my_tuple = (1, 2, 3, 4)
print(my_tuple)

---

🔹 Creating Tuples

# Empty tuple
t1 = ()

# Tuple with elements
t2 = (10, 20, 30)

# Without parentheses
t3 = 1, 2, 3

# Mixed data types
t4 = (1, "Hello", 3.5, True)

---

🔹 Accessing Elements

t = (10, 20, 30, 40)

print(t[0])     # First element
print(t[-1])    # Last element

---

🔹 Slicing Tuples

t = (1, 2, 3, 4, 5)

print(t[1:4])   # (2, 3, 4)
print(t[:3])    # (1, 2, 3)
print(t[::2])   # (1, 3, 5)

---

🔹 Tuple is Immutable

t = (1, 2, 3)

# ❌ This will give error
# t[0] = 10

---

🔹 Tuple Methods

t = (1, 2, 2, 3, 4)

print(t.count(2))   # Count occurrences
print(t.index(3))   # Find index

---

🔹 Tuple Packing & Unpacking

# Packing
t = (1, 2, 3)

# Unpacking
a, b, c = t

print(a, b, c)

---

🔹 Nested Tuples

t = (1, (2, 3), (4, 5))

print(t[1])      # (2, 3)
print(t[1][0])   # 2

---

🔹 Looping Through Tuple

t = (10, 20, 30)

for i in t:
    print(i)

---

🔹 Tuple Operations

t1 = (1, 2)
t2 = (3, 4)

print(t1 + t2)   # Concatenation
print(t1 * 2)    # Repetition

---

🔹 Convert Tuple

# Tuple to List
t = (1, 2, 3)
l = list(t)

# List to Tuple
l = [4, 5, 6]
t = tuple(l)

---

🔹 Built-in Functions

t = (5, 2, 8, 1)

print(len(t))
print(max(t))
print(min(t))
print(sum(t))

---

🔹 Advantages of Tuples

- Faster than lists 🚀
- Safe (cannot be modified) 🔒
- Can be used as dictionary keys

---

🔹 When to Use Tuples?

Use tuples when:

- Data should not change
- You need faster performance
- Fixed collection (like coordinates)

---

🧠 Example Program

# Student data using tuple
student = ("Bhumika", 18, "BCA")

name, age, course = student

print("Name:", name)
print("Age:", age)
print("Course:", course)

---

🚀 Conclusion

Tuples are a powerful and efficient data structure in Python.
They are best used when your data should remain constant.

---

⭐ If you like this, give a star to your repo!
Happy Coding 💻✨