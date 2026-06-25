

# Create a dictionary with 5 students and their marks
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 88,
    "Eva": 95
}

print("Student Marks Dictionary:")
print(students)

# Access and print marks of a specific student
print("\nMarks of Bob:", students["Bob"])

# Add a new student
students["Frank"] = 90
print("\nAfter Adding Frank:")
print(students)

# Find the student with the highest marks
top_student = max(students, key=students.get)
print("\nHighest Marks Student:", top_student)
print("Marks:", students[top_student])

# Merge two dictionaries
students2 = {
    "Grace": 89,
    "Henry": 91
}

merged_dict = students | students2   # Python 3.9+
print("\nMerged Dictionary:")
print(merged_dict)

# Count character frequencies in a string
text = "dictionary"
freq = {}

for char in text:
    freq[char] = freq.get(char, 0) + 1

print("\nCharacter Frequencies:")
print(freq)

# Find the length of a string
def string_length(s):
    return len(s)

print("\nLength of String:", string_length("Python"))


# Find maximum value
def find_max(numbers):
    return max(numbers)

nums = [10, 20, 5, 40, 15]
print("Maximum Value:", find_max(nums))


# Find minimum value
def find_min(numbers):
    return min(numbers)

print("Minimum Value:", find_min(nums))


# Find sum of numbers
def find_sum(numbers):
    return sum(numbers)

print("Sum of Numbers:", find_sum(nums))


# Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))


# Student details using positional arguments
def student_details(name, roll, dept):
    print("\nStudent Details")
    print("Name:", name)
    print("Roll No:", roll)
    print("Department:", dept)

student_details("John", 101, "Computer Science")


# Calculate total marks using positional arguments
def calculate_total(marks1, marks2, marks3):
    return marks1 + marks2 + marks3

total = calculate_total(85, 90, 88)
print("\nTotal Marks:", total)


# Rectangle area using positional arguments
def rectangle_area(length, width):
    return length * width

print("Rectangle Area:", rectangle_area(10, 5))


# Greeting using default argument
def greet_user(name, message="Good Morning"):
    print(f"{message}, {name}!")

greet_user("Alice")
greet_user("Bob", "Good Evening")


# Add any number of values using *args
def add_numbers(*args):
    return sum(args)

print("\nSum using *args:", add_numbers(10, 20, 30, 40))


# Multiply any number of values using *args
def multiply_all(*args):
    result = 1
    for num in args:
        result *= num
    return result

print("Multiplication using *args:", multiply_all(2, 3, 4, 5))
