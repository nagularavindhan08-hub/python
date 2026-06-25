'''# 1. Add two numbers
add = lambda a, b: a + b
print("Addition:", add(10, 20))

# 2. Square of a number
square = lambda x: x ** 2
print("Square:", square(5))

# 3. Cube of a number
cube = lambda x: x ** 3
print("Cube:", cube(3))

# 4. Check even or odd
even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print("Number is:", even_odd(7))

# 5. Largest of two numbers
largest = lambda a, b: a if a > b else b
print("Largest:", largest(15, 25))
numbers = [2, 5, 8, 11, 14, 17, -3, 20, 25]

# 1. Filter even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)

# 2. Filter odd numbers
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print("Odd Numbers:", odd_numbers)

# 3. Filter numbers greater than 10
greater_than_10 = list(filter(lambda x: x > 10, numbers))
print("Greater than 10:", greater_than_10)

# 4. Filter positive numbers
positive_numbers = list(filter(lambda x: x > 0, numbers))
print("Positive Numbers:", positive_numbers)

# 5. Filter numbers divisible by 5
divisible_by_5 = list(filter(lambda x: x % 5 == 0, numbers))
print("Divisible by 5:", divisible_by_50
numbers = [1, 2, 3, 4, 5]'''

# 1. Find squares
squares = list(map(lambda x: x ** 2, numbers))
print("Squares:", squares)

# 2. Double all numbers
double_numbers = list(map(lambda x: x * 2, numbers))
print("Doubled:", double_numbers)

# 3. Add 5 to each element
add_five = list(map(lambda x: x + 5, numbers))
print("Add 5:", add_five)

# 4. Find cubes
cubes = list(map(lambda x: x ** 3, numbers))
print("Cubes:", cubes)

# 5. Convert numbers into strings
string_numbers = list(map(str, numbers))
print("String Numbers:", string_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -3, -6]

# 1. Filter even numbers and find their squares
result1 = list(map(lambda x: x ** 2,
                   filter(lambda x: x % 2 == 0, numbers)))
print("Even Squares:", result1)

# 2. Filter odd numbers and double them
result2 = list(map(lambda x: x * 2,
                   filter(lambda x: x % 2 != 0, numbers)))
print("Double Odd:", result2)

# 3. Filter numbers greater than 5 and find their cubes
result3 = list(map(lambda x: x ** 3,
                   filter(lambda x: x > 5, numbers)))
print("Cubes > 5:", result3)

# 4. Filter positive numbers and add 10
result4 = list(map(lambda x: x + 10,
                   filter(lambda x: x > 0, numbers)))
print("Positive + 10:", result4)

# 5. Filter numbers divisible by 3 and multiply by 2
result5 = list(map(lambda x: x * 2,
                   filter(lambda x: x % 3 == 0, numbers)))
print("Divisible by 3 * 2:", result5)


Addition: 30
Square: 25
Cube: 27
Number is: Odd
Largest: 25

Even Numbers: [2, 8, 14, 20]
Odd Numbers: [5, 11, 17, -3, 25]
Greater than 10: [11, 14, 17, 20, 25]
Positive Numbers: [2, 5, 8, 11, 14, 17, 20, 25]
Divisible by 5: [5, 20, 25]

Squares: [1, 4, 9, 16, 25]
Doubled: [2, 4, 6, 8, 10]
Add 5: [6, 7, 8, 9, 10]
Cubes: [1, 8, 27, 64, 125]
String Numbers: ['1', '2', '3', '4', '5']

Even Squares: [4, 16, 36, 64, 100, 36]
Double Odd: [2, 6, 10, 14, 18, -6]
Cubes > 5: [216, 343, 512, 729, 1000]
Positive + 10: [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Divisible by 3 * 2: [6, 12, 18, -12]





















    
