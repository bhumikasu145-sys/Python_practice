🐍 Python Lists – Complete Guide 🚀

✨ Beginner to Advanced Concepts with Examples

---

📚 Table of Contents

- 📌 What is a List?
- 🛠️ Creating Lists
- 🔍 Accessing Elements
- ✂️ Slicing
- ✏️ Updating List
- ➕ Adding Elements
- ❌ Removing Elements
- 🔁 Looping
- ⚡ List Comprehension
- 🧩 Nested Lists
- 💻 Programs
- ✅ Advantages & ❌ Disadvantages
- 🚀 Next Steps

--

📌 What is a List?

A list is a collection of items stored in a single variable.

✨ Features:
✔ Ordered
✔ Mutable (changeable)
✔ Allows duplicates

fruits = ["apple", "banana", "mango"]
numbers = [1, 2, 3, 4]

---

🛠️ Creating Lists

empty = []
numbers = [10, 20, 30]
mixed = [1, "hello", 3.5]

---

🔍 Accessing Elements

fruits = ["apple", "banana", "mango"]

print(fruits[0])   # apple
print(fruits[-1])  # mango

---

✂️ List Slicing

numbers = [1, 2, 3, 4, 5]

print(numbers[1:4])   # [2,3,4]
print(numbers[:3])    # [1,2,3]
print(numbers[::2])   # [1,3,5]

---

✏️ Updating List

fruits = ["apple", "banana", "mango"]

fruits[1] = "orange"
print(fruits)

---

➕ Adding Elements

fruits = ["apple", "banana"]

fruits.append("mango")
fruits.insert(1, "orange")
print(fruits)

---

❌ Removing Elements

fruits = ["apple", "banana", "mango"]

fruits.remove("banana")
fruits.pop()
del fruits[0]
print(fruits)

---

🔁 Looping Through List

numbers = [1, 2, 3, 4]

for num in numbers:
    print(num)

---

⚡ List Comprehension ⭐

numbers = [1, 2, 3, 4, 5]

squares = [x**2 for x in numbers]
print(squares)

---

🧩 Nested Lists

matrix = [[1, 2], [3, 4], [5, 6]]

print(matrix[0][1])  # 2

---

💻 Practice Programs

🔹 Find Largest Number

numbers = [10, 20, 5, 40]

largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print("Largest:", largest)

---

🔹 Count Even & Odd

numbers = [1, 2, 3, 4, 5]

even = odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even, "Odd:", odd)

---

🔹 Remove Duplicates

numbers = [1, 2, 2, 3, 4, 4]

unique = list(set(numbers))
print(unique)

---

🔹 Simple To-Do List

tasks = []

tasks.append("Study Python")
tasks.append("Practice coding")

print(tasks)

---

✅ Advantages

✔ Easy to use
✔ Flexible data storage
✔ Dynamic size
✔ Supports multiple data types

---

❌ Disadvantages

❌ Uses more memory
❌ Slower for very large data

---

🚀 Next Steps

After Lists, learn:
👉 Tuples
👉 Sets
👉 Dictionaries

---

🙋‍♀️ Author

✨ Bhoomika
📌 Python Learner | Future Developer 💻

---

⭐ If you like this repo, don’t forget to star it! ⭐
