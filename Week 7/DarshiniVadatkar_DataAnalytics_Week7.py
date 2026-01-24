# WEEK 7 - PYTHON ASSIGNMENT

import csv
import json
import re

# TASK 1: PYTHON BASICS & DATA TYPES

print("\n--- TASK 1: PYTHON BASICS & DATA TYPES ---")

int_var = 10
float_var = 25.5
string_var = "Data Analytics"
bool_var = True

print("Integer:", int_var)
print("Float:", float_var)
print("String:", string_var)
print("Boolean:", bool_var)

name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))

print("\nEntered Values")
print("Name:", name)
print("Age:", age)
print("Marks:", marks)

a = 20
b = 5

print("\nArithmetic Operations")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# TASK 2: DATA STRUCTURES & LOOPS

print("\n--- TASK 2: DATA STRUCTURES & LOOPS ---")

numbers = [10, 25, 30, 45, 12, 8, 60, 90, 3, 15]

print("Numbers List:", numbers)
print("Sum:", sum(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

student = {
    "name": "Darshini",
    "age": 20,
    "course": "Data Analytics",
    "marks": 88
}

print("\nStudent Dictionary Values:")
for value in student.values():
    print(value)

# TASK 3: FUNCTIONS & LAMBDA

print("\n--- TASK 3: FUNCTIONS & LAMBDA ---")

def calculate_total_and_average(marks_list):
    total = sum(marks_list)
    average = total / len(marks_list)
    return total, average

def check_even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

square = lambda x: x * x

def get_even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

marks_list = [65, 70, 80, 90, 75]
total, average = calculate_total_and_average(marks_list)

print("Marks List:", marks_list)
print("Total Marks:", total)
print("Average Marks:", average)
print("7 is:", check_even_odd(7))
print("Square of 6:", square(6))
print("Even Numbers from numbers list:", get_even_numbers(numbers))


# TASK 4: FILE HANDLING

print("\n--- TASK 4: FILE HANDLING ---")

file_name = "sample.txt"

with open(file_name, "w") as file:
    file.write("Line 1: Python Basics\n")
    file.write("Line 2: Data Structures\n")
    file.write("Line 3: Functions\n")
    file.write("Line 4: File Handling\n")
    file.write("Line 5: Regex\n")

print("\nFile Content:")
with open(file_name, "r") as file:
    content = file.read()
    print(content)

with open(file_name, "a") as file:
    file.write("Line 6: CSV & JSON\n")

with open(file_name, "r") as file:
    line_count = len(file.readlines())

print("Total Lines in File:", line_count)

# TASK 5: CSV / JSON & REGEX

print("\n--- TASK 5: CSV / JSON & REGEX ---")


csv_file = "students.csv"
csv_data = [
    ["Name", "Age", "Marks"],
    ["Amit", 21, 85],
    ["Neha", 22, 90],
    ["Rohit", 20, 78]
]

with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)

print("\nCSV File Content:")
with open(csv_file, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


json_file = "students.json"
json_data = [
    {"name": "Amit", "age": 21, "marks": 85},
    {"name": "Neha", "age": 22, "marks": 90},
    {"name": "Rohit", "age": 20, "marks": 78}
]

with open(json_file, "w") as file:
    json.dump(json_data, file, indent=4)

print("\nJSON File Created Successfully")


text = "Contact me at 9876543210 or 123-456-7890!"

numbers_found = re.findall(r"\d+", text)
print("\nExtracted Numbers:", numbers_found)

clean_text = re.sub(r"[^a-zA-Z0-9 ]", "", text)
print("Text without special characters:", clean_text)

phone = "9876543210"
if re.fullmatch(r"[6-9]\d{9}", phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")

# TASK 6: MINI PYTHON PROGRAM


print("\n--- TASK 6: MINI PYTHON PROGRAM ---")

user_input = input("Enter some text (with numbers & symbols): ")

mini_file = "mini_data.txt"

with open(mini_file, "w") as file:
    file.write(user_input)

with open(mini_file, "r") as file:
    raw_data = file.read()

cleaned_data = re.sub(r"[^a-zA-Z0-9 ]", "", raw_data)

print("\nRaw Data:", raw_data)
print("Cleaned Data:", cleaned_data)

print("\n--- ALL TASKS COMPLETED SUCCESSFULLY ---")
