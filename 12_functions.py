🐍 Python Functions

📌 Introduction

A function is a reusable block of code that performs a specific task.

Functions help us:

- ✅ Reuse code
- ✅ Reduce repetition
- ✅ Organize programs
- ✅ Make code easier to read and maintain

---

🔹 1. Basics of Functions

A function is created using the "def" keyword.

Syntax

def function_name():
    # code

Example

def greet():
    print("Hello, Python!")

greet()

Output:

Hello, Python!

---

🔹 2. Defining Functions

A function is defined using "def" followed by the function name and parentheses.

def add():
    a = 10
    b = 20
    print(a + b)

add()

Output:

30

---

🔹 3. Function Parameters

Parameters are variables written inside the function definition. They allow us to pass data into a function.

def greet(name):
    print("Hello", name)

greet("Bhumika")

Output:

Hello Bhumika

Multiple Parameters

def add(a, b):
    print(a + b)

add(10, 20)

Output:

30

---

🔹 4. Returning Values from a Function

The "return" statement sends a value back to the caller.

def add(a, b):
    return a + b

result = add(10, 20)

print(result)

Output:

30

Return Multiple Values

def calculate(a, b):
    return a + b, a - b

addition, subtraction = calculate(10, 5)

print(addition)
print(subtraction)

Output:

15
5

---

🔹 5. Default Parameter Values

A parameter can have a default value.

If no value is provided, Python uses the default value.

def greet(name="User"):
    print("Hello", name)

greet()
greet("Bhumika")

Output:

Hello User
Hello Bhumika

---

🔹 6. Local and Global Variables

Local Variable

A variable created inside a function is called a local variable.

def show():
    message = "Hello"
    print(message)

show()

"message" can normally be accessed only inside the function.

Global Variable

A variable created outside a function is called a global variable.

name = "Bhumika"

def show():
    print(name)

show()

Output:

Bhumika

Using "global"

The "global" keyword can be used to modify a global variable inside a function.

count = 0

def update():
    global count
    count += 1

update()

print(count)

Output:

1

---

🔹 7. Keyword Arguments

Arguments can be passed using parameter names.

def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=18, name="Bhumika")

Output:

Name: Bhumika
Age: 18

Keyword arguments allow us to pass arguments in a different order.

---

🔹 8. Variable-Length Arguments

Variable-length arguments allow a function to accept any number of arguments.

"*args"

"*args" is used for multiple positional arguments.

def add(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total

print(add(10, 20, 30, 40))

Output:

100

"**kwargs"

"**kwargs" is used for multiple keyword arguments.

def student(**details):
    for key, value in details.items():
        print(key, ":", value)

student(name="Bhumika", age=18, course="BCA")

Output:

name : Bhumika
age : 18
course : BCA

---

🔹 9. Lambda Functions

A lambda function is a small anonymous function written in a single line.

Syntax

lambda arguments: expression

Example

square = lambda x: x ** 2

print(square(5))

Output:

25

Multiple Arguments

add = lambda a, b: a + b

print(add(10, 20))

Output:

30

---

🔹 10. Recursion

Recursion is a technique where a function calls itself.

A recursive function must have a base condition to stop the recursion.

Example: Factorial

def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))

Output:

120

How It Works

5 × 4 × 3 × 2 × 1
        ↓
       120

---

🔹 11. Nested Functions

A function defined inside another function is called a nested function.

def outer():
    print("Outer function")

    def inner():
        print("Inner function")

    inner()

outer()

Output:

Outer function
Inner function

---

🔹 12. Advanced Function Example

Different function concepts can be combined in one program.

def calculate(name, *numbers, bonus=0):

    total = sum(numbers)
    total += bonus

    return name, total


student, marks = calculate(
    "Bhumika",
    80, 75, 90,
    bonus=5
)

print(student)
print(marks)

Output:

Bhumika
250

---

📌 Function Concepts Summary

Concept| Purpose
"def"| Defines a function
Parameter| Receives data
"return"| Returns a value
Default Parameter| Provides a default value
Local Variable| Exists inside a function
Global Variable| Exists outside a function
Keyword Argument| Passes value using parameter name
"*args"| Multiple positional arguments
"**kwargs"| Multiple keyword arguments
"lambda"| Creates a small anonymous function
Recursion| Function calls itself
Nested Function| Function inside another function

---

🔹 Advantages of Functions

- ✅ Code reusability
- ✅ Reduces code duplication
- ✅ Makes programs modular
- ✅ Easier debugging
- ✅ Improves readability
- ✅ Makes large programs easier to manage
- ✅ Supports code organization

---

🔹 Disadvantages of Functions

- ❌ Too many small functions can make code difficult to follow
- ❌ Function calls add some overhead
- ❌ Recursion can use more memory
- ❌ Poorly designed functions can make programs complex

---

📌 Key Points

Python Functions
       ↓
     def
       ↓
   Parameters
       ↓
     Code
       ↓
    return
       ↓
   Function Call

Basic Example

def greet(name):
    return "Hello " + name

message = greet("Bhumika")

print(message)

Output:

Hello Bhumika

---

🎯 Conclusion

Functions are one of the most important concepts in Python.

They allow us to divide a large program into smaller, reusable blocks of code.
---