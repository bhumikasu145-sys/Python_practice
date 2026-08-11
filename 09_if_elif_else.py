🐍 Python if, elif and else

📌 Introduction

Conditional statements in Python are used to make decisions in a program.

They allow a program to execute different blocks of code depending on whether a condition is True or False.

Python mainly provides three conditional statements:

- "if"
- "elif"
- "else"

Example

age = 18

if age >= 18:
    print("You are eligible to vote")

Output:

You are eligible to vote

---

🔹 "if" Statement

The "if" statement executes a block of code when the given condition is True.

Syntax

if condition:
    # code to execute

Example

age = 20

if age >= 18:
    print("You are an adult")

Output:

You are an adult

---

🔹 "if" with Comparison Operators

We can use comparison operators with "if".

marks = 75

if marks >= 35:
    print("Pass")

Output:

Pass

Common Comparison Operators

Operator| Meaning| Example
"=="| Equal to| "a == b"
"!="| Not equal to| "a != b"
">"| Greater than| "a > b"
"<"| Less than| "a < b"
">="| Greater than or equal to| "a >= b"
"<="| Less than or equal to| "a <= b"

---

🔹 "if-else" Statement

The "else" statement executes when the "if" condition is False.

Syntax

if condition:
    # True block
else:
    # False block

Example

age = 16

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

Output:

Not eligible to vote

---

🔹 "if-elif-else" Statement

The "elif" statement means "else if".

It is used when we have multiple conditions.

Syntax

if condition1:
    # code
elif condition2:
    # code
else:
    # code

Example

marks = 75

if marks >= 90:
    print("Grade A+")
elif marks >= 75:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")

Output:

Grade A

---

🔹 Multiple "elif" Statements

We can use multiple "elif" statements in one program.

marks = 85

if marks >= 90:
    print("Excellent")
elif marks >= 80:
    print("Very Good")
elif marks >= 70:
    print("Good")
elif marks >= 35:
    print("Pass")
else:
    print("Fail")

Output:

Very Good

---

🔹 Nested "if"

An "if" statement inside another "if" statement is called a nested if.

Example

age = 20
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to vote")

Output:

Eligible to vote

---

🔹 Using Logical Operators

Conditional statements can be combined using logical operators.

"and"

Both conditions must be True.

age = 20
citizen = True

if age >= 18 and citizen:
    print("Eligible to vote")

"or"

At least one condition must be True.

day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")

"not"

Reverses the result.

is_raining = False

if not is_raining:
    print("You can go outside")

---

🔹 Checking Positive, Negative or Zero

number = -5

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

Output:

Negative

---

🔹 Checking Even or Odd

number = 10

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

Output:

Even number

---

🔹 Checking the Largest Number

a = 10
b = 20

if a > b:
    print("A is largest")
elif b > a:
    print("B is largest")
else:
    print("Both are equal")

Output:

B is largest

---

🔹 User Input with "if-else"

Conditional statements can be used with user input.

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

---

🔹 Short-Hand "if"

A simple "if" statement can be written in one line.

age = 20

if age >= 18: print("Adult")

Output:

Adult

---

🔹 Short-Hand "if-else"

Python also supports a one-line conditional expression.

Syntax

value_if_true if condition else value_if_false

Example

age = 20

result = "Adult" if age >= 18 else "Minor"

print(result)

Output:

Adult

---

🔹 Important Points About Indentation

Python uses indentation to define blocks of code.

Correct:

age = 20

if age >= 18:
    print("Adult")

Incorrect:

age = 20

if age >= 18:
print("Adult")

The second example causes an IndentationError.

---

🔹 Real-World Example

A simple login system can use "if-else".

username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid username or password")

Output:

Login successful

---

🔹 Advantages of Conditional Statements

- ✅ Used for decision-making
- ✅ Makes programs logical and flexible
- ✅ Allows different actions for different conditions
- ✅ Easy to understand
- ✅ Can be combined with logical and comparison operators
- ✅ Useful in real-world applications
- ✅ Supports nested conditions
- ✅ Helps control the flow of a program

---

🔹 Disadvantages of Conditional Statements

- ❌ Too many conditions can make code difficult to read
- ❌ Deeply nested "if" statements can become complicated
- ❌ Incorrect conditions can produce unexpected results
- ❌ Large "if-elif-else" blocks can make programs lengthy
- ❌ Poor indentation can cause errors in Python

---

🔹 "if" vs "elif" vs "else"

Statement| Purpose
"if"| Checks the first condition
"elif"| Checks another condition if previous conditions are False
"else"| Executes when all previous conditions are False

Example

marks = 65

if marks >= 90:
    print("A+")
elif marks >= 60:
    print("B")
else:
    print("Fail")

---

📌 Key Points

Conditional Statements
        ↓
      if
        ↓
     elif
        ↓
     else
        ↓
 Decision Making
        ↓
 Program Control

Basic Structure

if condition:
    statement
elif condition:
    statement
else:
    statement

---

🎯 Conclusion

Python "if", "elif", and "else" statements are important decision-making tools used to control the flow of a program.

- "if" checks a condition.
- "elif" checks additional conditions.
- "else" executes when all conditions are False.

Understanding conditional statements is essential before learning advanced concepts such as loops, functions, and problem-solving in Python.

---