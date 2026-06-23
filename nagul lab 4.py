#1
i = 1

while i <= 10:
    print(i)
    i += 1
#2
i=10

while i>=10:
    print(i)
    i-=1
#3
i = 2

while i <= 20:
    print(i)
    i += 2
#4
i = 1

while i <= 20:
    print(i)
    i += 2
#5
n = int(input("Enter N: "))

i = 1
total = 0

while i <= n:
    total += i
    i += 1

print("Sum =", total)
#6
n = int(input("Enter a number: "))

i = 1

while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1
#7
n = int(input("Enter a number: "))

fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1

print("Factorial =", fact)
#8
num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed Number =", reverse)
#9
num = int(input("Enter a number: "))

temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

if num == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
#10
num = int(input("Enter a number: "))

temp = num
sum_digits = 0
product = 1

while temp > 0:
    digit = temp % 10
    sum_digits += digit
    product *= digit
    temp = temp // 10

if sum_digits == product:
    print("Spy Number")
else:
    print("Not a Spy Number")

























