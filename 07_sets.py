🐍 Python Sets – Topic-wise Examples

---

📌 1. Creating Sets

# Creating a set
set1 = {1, 2, 3, 4}
print("Set:", set1)

# Using set() function
set2 = set([5, 6, 7])
print("Set2:", set2)

---

📌 2. Adding Elements

s = {1, 2, 3}

# Add single element
s.add(4)

# Add multiple elements
s.update([5, 6])

print("After adding:", s)

---

📌 3. Removing Elements

s = {1, 2, 3, 4}

s.remove(2)   # Removes 2
s.discard(5)  # No error if not present
removed = s.pop()  # Removes random element

print("After removing:", s)
print("Popped element:", removed)

---

📌 4. Set Operations

A = {1, 2, 3}
B = {3, 4, 5}

# Union
print("Union:", A | B)

# Intersection
print("Intersection:", A & B)

# Difference
print("A - B:", A - B)

# Symmetric Difference
print("Symmetric Difference:", A ^ B)

---

📌 5. Checking Membership

s = {10, 20, 30}

print(10 in s)   # True
print(40 in s)   # False

---

📌 6. Looping Through Set

s = {1, 2, 3}

for item in s:
    print(item)

---

📌 7. Set Methods

A = {1, 2, 3}
B = {3, 4, 5}

print("Union:", A.union(B))
print("Intersection:", A.intersection(B))
print("Difference:", A.difference(B))

---

📌 8. Removing Duplicates from List

numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = set(numbers)

print("Unique:", unique_numbers)

---

📌 9. Frozen Set (Immutable Set)

fs = frozenset([1, 2, 3])

# fs.add(4) ❌ Not allowed

print("Frozen Set:", fs)

---

📌 10. Practical Example

students = {"Bhumika", "Ravi", "Anu"}

# Add new student
students.add("Kiran")

# Remove student
students.discard("Ravi")

print("Final Students:", students)

---

🎯 Summary

- Sets store unique elements
- No indexing allowed
- Useful for fast searching & removing duplicates

---