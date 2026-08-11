 🐍 Python For Loops with Lists, Dictionaries & String Splitting

1. 🔹 Lists and Dictionaries with For Loop

Looping Through a List

cities = ["Bangalore", "Mysore", "Hubli", "Davangere"]

for city in cities:
    print(city)

Doubling Each Number in a List

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number * 2)

Output:

2
4
6
8
10

Looping Through a Dictionary

student = {
    "name": "Bhumika",
    "age": 18,
    "course": "BCA"
}

for key in student:
    print(key)

Iterating Over Dictionary Values

student = {
    "name": "Bhumika",
    "age": 18,
    "course": "BCA"
}

for value in student.values():
    print(value)

Iterating Over Both Keys and Values

student = {
    "name": "Bhumika",
    "age": 18,
    "course": "BCA"
}

for key, value in student.items():
    print(key, ":", value)

---

2. 🔹 For Loops with "range()"

for i in range(1, 6):
    print(i)

Output:

1
2
3
4
5

Squaring Numbers in a List

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number ** 2)

Output:

1
4
9
16
25

Filtering Even Numbers

numbers = [10, 15, 20, 25, 30, 35]

for number in numbers:
    if number % 2 == 0:
        print(number)

Output:

10
20
30

Uppercasing Kannada City Names

cities = ["bengaluru", "mysuru", "hubballi", "dharwad"]

for city in cities:
    print(city.upper())

Output:

BENGALURU
MYSURU
HUBBALLI
DHARWAD

---

3. 🔹 Dictionary Operations

Creating a Dictionary of Squares

numbers = [1, 2, 3, 4, 5]

squares = {}

for number in numbers:
    squares[number] = number ** 2

print(squares)

Output:

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

Dictionary Comparison

Two dictionaries can be compared using "==".

dict1 = {"a": 1, "b": 2}
dict2 = {"a": 1, "b": 2}

if dict1 == dict2:
    print("Dictionaries are equal")
else:
    print("Dictionaries are different")

Output:

Dictionaries are equal

Comparing Dictionary Values

students = {
    "Bhumika": 85,
    "Anu": 65,
    "Ravi": 90
}

for name, marks in students.items():
    if marks > 70:
        print(name, marks)

Output:

Bhumika 85
Ravi 90

---

4. 🔹 Converting a List of Names to Dictionary of Name Length

names = ["Bhumika", "Anu", "Ravi", "Kiran"]

name_lengths = {}

for name in names:
    name_lengths[name] = len(name)

print(name_lengths)

Output:

{'Bhumika': 7, 'Anu': 3, 'Ravi': 4, 'Kiran': 5}

---

5. 🔹 Filtering Names with Population Above 10 Lakh

cities = {
    "Bengaluru": 85,
    "Mysuru": 10,
    "Hubballi": 9,
    "Mangaluru": 7
}

for city, population in cities.items():
    if population > 10:
        print(city)

Output:

Bengaluru

«Here, population is represented in lakhs.»

---

6. 🔹 Splitting Strings

The "split()" method divides a string into a list.

Basic Splitting

text = "Python is easy to learn"

words = text.split()

print(words)

Output:

['Python', 'is', 'easy', 'to', 'learn']

---

🔹 Separator and "maxsplit"

Using a Separator

data = "Apple,Mango,Orange"

fruits = data.split(",")

print(fruits)

Output:

['Apple', 'Mango', 'Orange']

Using "maxsplit"

"maxsplit" specifies the maximum number of splits.

data = "Apple,Mango,Orange,Grapes"

result = data.split(",", 2)

print(result)

Output:

['Apple', 'Mango', 'Orange,Grapes']

---

🔹 Splitting a Sentence into Words

sentence = "Python is a powerful programming language"

words = sentence.split()

for word in words:
    print(word)

Output:

Python
is
a
powerful
programming
language

---

🔹 Splitting a String with Commas

data = "Bengaluru,Mysuru,Hubballi,Dharwad"

cities = data.split(",")

print(cities)

Output:

['Bengaluru', 'Mysuru', 'Hubballi', 'Dharwad']

---

🔹 Limiting the Number of Splits

data = "Python,Java,C++,JavaScript"

languages = data.split(",", 2)

print(languages)

Output:

['Python', 'Java', 'C++,JavaScript']

---

📌 Quick Summary

Topic| Method / Concept
Loop through List| "for item in list"
Double List Values| "number * 2"
Loop Dictionary| "for key in dict"
Dictionary Values| "dict.values()"
Key + Value| "dict.items()"
Range Loop| "range()"
Square Numbers| "number ** 2"
Filter Even Numbers| "number % 2 == 0"
Uppercase| ".upper()"
Dictionary Comparison| "dict1 == dict2"
Dictionary of Squares| "number ** 2"
Name Length| "len(name)"
String Splitting| ".split()"
Separator| ".split(",")"
Limit Splits| ".split(",", maxsplit)"

---

🎯 Conclusion

This page covers practical Python operations using "for" loops, Lists, Dictionaries, and String "split()". These concepts are useful for Python programming, data processing, and beginner-level problem solving.