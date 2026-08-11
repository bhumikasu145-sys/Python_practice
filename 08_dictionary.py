🐍 Python Dictionaries

📌 Introduction

A Dictionary in Python is a collection used to store data in key-value pairs. Dictionaries are ordered, mutable, and do not allow duplicate keys.

Dictionaries are useful when we want to store and access data using a meaningful key instead of an index.

Example

student = {
    "name": "Bhumika",
    "age": 18,
    "course": "BCA"
}

print(student)

Output:

{'name': 'Bhumika', 'age': 18, 'course': 'BCA'}

---

🔹 Creating a Dictionary

A dictionary is created using curly brackets "{}" with key-value pairs.

student = {
    "name": "Bhumika",
    "age": 18,
    "city": "Davanagere"
}

print(student)

Syntax

dictionary = {
    "key": "value"
}

---

🔹 Accessing Dictionary Values

We can access a value using its key.

student = {
    "name": "Bhumika",
    "age": 18
}

print(student["name"])
print(student["age"])

Output:

Bhumika
18

---

🔹 Using "get()"

The "get()" method is used to access a value safely.

student = {
    "name": "Bhumika",
    "age": 18
}

print(student.get("name"))

Output:

Bhumika

---

🔹 Adding a New Item

A new key-value pair can be added easily.

student = {
    "name": "Bhumika",
    "age": 18
}

student["course"] = "BCA"

print(student)

Output:

{'name': 'Bhumika', 'age': 18, 'course': 'BCA'}

---

🔹 Updating Dictionary Values

Existing values can be changed.

student = {
    "name": "Bhumika",
    "age": 18
}

student["age"] = 19

print(student)

Output:

{'name': 'Bhumika', 'age': 19}

---

🔹 Removing Items

"pop()"

Removes an item using its key.

student = {
    "name": "Bhumika",
    "age": 18,
    "course": "BCA"
}

student.pop("age")

print(student)

"del"

del student["course"]

"popitem()"

Removes the last inserted item.

student.popitem()

"clear()"

Removes all items.

student.clear()

---

🔹 Important Dictionary Methods

Method| Purpose
"get()"| Gets a value
"keys()"| Returns all keys
"values()"| Returns all values
"items()"| Returns key-value pairs
"update()"| Updates the dictionary
"pop()"| Removes a specified item
"popitem()"| Removes the last item
"clear()"| Removes all items
"copy()"| Creates a copy
"setdefault()"| Gets a value and adds key if missing

Example

student = {
    "name": "Bhumika",
    "age": 18,
    "course": "BCA"
}

print(student.keys())
print(student.values())
print(student.items())

---

🔹 Checking if a Key Exists

The "in" operator can be used to check whether a key exists.

student = {
    "name": "Bhumika",
    "age": 18
}

if "name" in student:
    print("Name is available")

Output:

Name is available

---

🔹 Looping Through a Dictionary

Loop Through Keys

student = {
    "name": "Bhumika",
    "age": 18,
    "course": "BCA"
}

for key in student:
    print(key)

Loop Through Values

for value in student.values():
    print(value)

Loop Through Key-Value Pairs

for key, value in student.items():
    print(key, ":", value)

Output:

name : Bhumika
age : 18
course : BCA

---

🔹 Dictionary Length

The "len()" function returns the number of key-value pairs.

student = {
    "name": "Bhumika",
    "age": 18,
    "course": "BCA"
}

print(len(student))

Output:

3

---

🔹 Nested Dictionaries

A dictionary can contain another dictionary.

students = {
    "student1": {
        "name": "Bhumika",
        "age": 18
    },
    "student2": {
        "name": "Anu",
        "age": 19
    }
}

print(students["student1"]["name"])

Output:

Bhumika

---

🔹 Dictionary with Different Data Types

Dictionary values can contain different types of data.

data = {
    "name": "Bhumika",
    "age": 18,
    "marks": 85.5,
    "passed": True,
    "subjects": ["Python", "Maths"]
}

print(data)

---

🔹 Dictionary Comprehension

Dictionary comprehension provides a short way to create dictionaries.

numbers = [1, 2, 3, 4, 5]

squares = {x: x * x for x in numbers}

print(squares)

Output:

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

---

🔹 "update()" Method

The "update()" method is used to add or update multiple key-value pairs.

student = {
    "name": "Bhumika",
    "age": 18
}

student.update({
    "course": "BCA",
    "city": "Davanagere"
})

print(student)

---

🔹 Copying a Dictionary

The "copy()" method creates a copy of a dictionary.

student = {
    "name": "Bhumika",
    "age": 18
}

new_student = student.copy()

print(new_student)

---

🔹 Real-World Example

A student's information can be stored using a dictionary:

student = {
    "name": "Bhumika",
    "course": "BCA",
    "semester": 5,
    "marks": 85
}

print("Student Details")

for key, value in student.items():
    print(key, ":", value)

Output:

Student Details
name : Bhumika
course : BCA
semester : 5
marks : 85

---

🔹 Dictionary vs List

Feature| List| Dictionary
Syntax| "[]"| "{}"
Access| Index| Key
Data| Values| Key-Value pairs
Mutable| ✅ Yes| ✅ Yes
Duplicates| ✅ Allowed| ❌ Duplicate keys not allowed
Example| "[10, 20, 30]"| "{"age": 18}"

---

🔹 Advantages of Dictionaries

- ✅ Stores data in key-value pairs
- ✅ Fast access using keys
- ✅ Easy to update data
- ✅ Mutable
- ✅ Can store different data types
- ✅ Useful for representing structured data
- ✅ Supports many built-in methods
- ✅ Very useful in real-world applications

---

🔹 Disadvantages of Dictionaries

- ❌ Uses more memory compared with some simpler data structures
- ❌ Keys must be unique
- ❌ Keys must be hashable
- ❌ Can be slightly more complex for beginners
- ❌ Not suitable when simple sequential data is required

---

📌 Key Points

Dictionary
     ↓
Key-Value Pairs
     ↓
Ordered
     ↓
Mutable
     ↓
No Duplicate Keys
     ↓
Uses {}
     ↓
Access Using Keys
     ↓
Many Built-in Methods

Example

person = {
    "name": "Bhumika",
    "age": 18
}

print(person["name"])       # Access
person["city"] = "Davanagere"  # Add
person["age"] = 19         # Update
person.pop("city")         # Remove

print(person)

---

🎯 Conclusion

Python Dictionaries are one of the most important data structures in Python. They store information in key-value pairs, making data easy to organize, access, and update. Dictionaries are widely used in applications such as student records, employee information, databases, JSON data, APIs, and configuration files.

Understanding dictionaries is an important step toward learning advanced Python programming.

---
