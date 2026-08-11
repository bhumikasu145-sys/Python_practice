🐍 Python Loops

📌 Introduction

Loops in Python are used to execute a block of code repeatedly.

Python mainly provides two types of loops:

1. "for" loop
2. "while" loop

Loops help reduce code repetition and make programs shorter, cleaner, and easier to manage.

---

🔹 1. For Loop

A for loop is used to iterate over a sequence such as a list, tuple, string, dictionary, set, or range.

Syntax

for variable in sequence:
    # code to execute

Example

fruits = ["Apple", "Mango", "Orange"]

for fruit in fruits:
    print(fruit)

Output:

Apple
Mango
Orange

---

🔹 For Loop with "range()"

The "range()" function is commonly used with a for loop.

for i in range(1, 6):
    print(i)

Output:

1
2
3
4
5

---

🔹 Printing Even Numbers

for i in range(2, 11, 2):
    print(i)

Output:

2
4
6
8
10

---

🔹 Printing Odd Numbers

for i in range(1, 11, 2):
    print(i)

Output:

1
3
5
7
9

---

🔹 For Loop with String

A for loop can iterate through each character of a string.

name = "Python"

for character in name:
    print(character)

Output:

P
y
t
h
o
n

---

🔹 For Loop with Dictionary

student = {
    "name": "Bhumika",
    "age": 18,
    "course": "BCA"
}

for key, value in student.items():
    print(key, ":", value)

Output:

name : Bhumika
age : 18
course : BCA

---

🔹 2. While Loop

A while loop repeatedly executes a block of code as long as a given condition is True.

Syntax

while condition:
    # code to execute

Example

i = 1

while i <= 5:
    print(i)
    i += 1

Output:

1
2
3
4
5

---

🔹 How While Loop Works

Start
  ↓
Check Condition
  ↓
Condition True?
  ↓ Yes
Execute Code
  ↓
Update Variable
  ↓
Check Again
  ↓
Condition False
  ↓
Stop

---

🔹 While Loop with Even Numbers

i = 2

while i <= 10:
    print(i)
    i += 2

Output:

2
4
6
8
10

---

🔹 While Loop with User Input

number = int(input("Enter a number: "))

while number != 0:
    print("You entered:", number)
    number = int(input("Enter 0 to stop: "))

The loop continues until the user enters "0".

---

🔹 Loop Control Statements

Python provides special statements to control loops.

1. "break"

Stops the loop immediately.

for i in range(1, 10):
    if i == 5:
        break

    print(i)

Output:

1
2
3
4

---

2. "continue"

Skips the current iteration and continues with the next iteration.

for i in range(1, 6):
    if i == 3:
        continue

    print(i)

Output:

1
2
4
5

---

3. "pass"

Does nothing and is used as a placeholder.

for i in range(5):
    pass

---

🔹 Nested Loops

A loop inside another loop is called a nested loop.

Example

for i in range(1, 4):
    for j in range(1, 3):
        print(i, j)

Output:

1 1
1 2
2 1
2 2
3 1
3 2

---

🔹 Sum of Numbers Using For Loop

total = 0

for i in range(1, 6):
    total += i

print("Sum =", total)

Output:

Sum = 15

---

🔹 Sum of Numbers Using While Loop

i = 1
total = 0

while i <= 5:
    total += i
    i += 1

print("Sum =", total)

Output:

Sum = 15

---

🔹 Multiplication Table

Using For Loop

number = 7

for i in range(1, 11):
    print(number, "x", i, "=", number * i)

Using While Loop

number = 7
i = 1

while i <= 10:
    print(number, "x", i, "=", number * i)
    i += 1

---

🔹 For Loop vs While Loop

Feature| For Loop| While Loop
Main use| Iterating over a sequence| Repeating while a condition is True
Condition| Not written separately in most cases| Required
Best when| Number of iterations is known| Number of iterations may be unknown
Common use| Lists, strings, ranges| User input, validation
Infinite loop| Less common| More likely
Example| "for i in range(5)"| "while i < 5"

---

🔹 Advantages of Loops

- ✅ Reduces code repetition
- ✅ Makes programs shorter
- ✅ Saves development time
- ✅ Makes repetitive tasks easier
- ✅ Useful for processing large amounts of data
- ✅ Supports "break", "continue", and "pass"
- ✅ Useful in problem-solving and DSA
- ✅ Can be combined with conditional statements

---

🔹 Disadvantages of Loops

- ❌ Incorrect conditions can cause infinite loops
- ❌ Nested loops can make code complicated
- ❌ Too many loops can affect program performance
- ❌ Difficult loop logic can be harder to debug
- ❌ Poorly written loops can cause unnecessary processing

---

🔹 Real-World Example

Loops are commonly used to process student marks.

marks = [85, 72, 90, 65, 78]

for mark in marks:
    if mark >= 35:
        print(mark, "Pass")
    else:
        print(mark, "Fail")

Output:

85 Pass
72 Pass
90 Pass
65 Pass
78 Pass

---

📌 Key Points

Python Loops
     ↓
 ┌───────────────┐
 ↓               ↓
For Loop      While Loop
 ↓               ↓
Sequence       Condition
 ↓               ↓
range()       True/False
 ↓               ↓
break / continue / pass

Basic Examples

For Loop:

for i in range(1, 6):
    print(i)

While Loop:

i = 1

while i <= 5:
    print(i)
    i += 1

---

🎯 Conclusion

Loops are an important part of Python programming.

The "for" loop is mainly used when we want to iterate through a sequence or when the number of iterations is known.

The "while" loop is mainly used when we want to repeat code as long as a condition remains True.
----
--