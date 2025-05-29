# Write a Python program to print "Hello Python".
print("hello world")


# Write a Python program to do arithmetical operations addition and division.
# Addition
num1 = float(input("Enter the first number for addition: "))
num2 = float(input("Enter the second number for addition: "))
sum_result = num1 + num2
print(f"sum: {num1} + {num2} = {sum_result}")


# Division
num3 = float(input("Enter the dividend: "))
num4 = float(input("Enter the divisor: "))
if num4 == 0:
 print("Error: Division by zero is not allowed.")
else:
 div_result = num3 / num4
 print(f"Division: {num3} / {num4} = {div_result}")


 # Write a Python program to find the area of a triangle.
# take height and base from user
base = float(input("enter base value: "))
height = float(input("enter height value: "))         
# calculating the area of triangle
area = 0.5 * base * height
print(f"The area of the triangle is: {area}")


# Write a Python program to swap two variables.
# Input two variables
a = input("Enter the value of the first variable (a): ")
b = input("Enter the value of the second variable (b): ")
# Display the original values
print(f"Original values: a = {a}, b = {b}")
# Swap the values using a temporary variable
temp = a
a = b
b = temp
# Display the swapped values
print(f"Swapped values: a = {a}, b = {b}")


# Write a Python program to generate a random number
import random
print(f"Random number: {random.randint(1, 100)}")


# Write a Python program to convert kilometers to miles
kilometers = float(input("Enter distance in kilometers: "))
# Conversion factor: 1 kilometer = 0.621371 miles
conversion_factor = 0.621371
miles = kilometers * conversion_factor
print(f"{kilometers} kilometers is equal to {miles} miles")


# Write a Python program to convert Celsius to Fahrenheit.
celsius = float(input("Enter temperature in Celsius: "))
# Conversion formula: Fahrenheit = (Celsius * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32
print("temperature in fahrenheit",fahrenheit)


# Write a Python program to display calendar
import calendar
year = int(input("Enter year: "))
month = int(input("Enter month: "))
cal = calendar.month(year, month)
print(cal)


# Write a Python program to swap two variables without temp variable.
a = 5
b = 10
a,b = b,a
print("After swapping:")
print("a =", a)
print("b =", b)


# Write a Python Program to Check if a Number is Positive, Negative or Zero
num = float(input("enter any number: "))
if num > 0:
 print("Positive number")
elif num == 0:
 print("Zero")
else:
 print("Negative number")


# Write a Python Program to Check if a Number is Odd or Even
num = int(input("Enter a number: "))
if num%2 == 0:
 print("This is a even number")
else:
 print("This is a odd number")


# Write a Python Program to Check Leap Year.
year = int(input("Enter a year: "))
# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year

if (year % 400 == 0) and (year % 100 == 0):
 print("{0} is a leap year".format(year))

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
 print("{0} is a leap year".format(year))
 
# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
 print("{0} is not a leap year".format(year))
 



# Write a Python Program to Check Prime Number.
# Prime Numbers:
# A prime number is a whole number that cannot be evenly divided by any other number
# except for 1 and itself. For example, 2, 3, 5, 7, 11, and 13 are prime numbers because they
# cannot be divided by any other positive integer except for 1 and their own value.
num = int(input("Enter a number: "))
# define a flag variable
flag = False
if num == 1:
 print(f"{num}, is not a prime number")
elif num > 1:
 # check for factors
    for i in range(2, num):
       if (num % i) == 0:
          flag = True # if factor is found, set flag to True
 # break out of loop
          break
 # check if flag is True
if flag:
 print(f"{num}, is not a prime number")
else:
 print(f"{num}, is a prime number")



#  Write a Python Program to Print all Prime Numbers in an Interval of 1-10
# Python program to display all the prime numbers within an interval
 lower = 1
 upper = 10
 print("Prime numbers between", lower, "and", upper, "are:")
 for num in range(lower, upper + 1):
 # all prime numbers are greater than 1
  if num > 1:
    for i in range(2, num):
      if (num % i) == 0:
        break
    else:
       print(num)


#  Write a Python Program to Find the Factorial of a Number
num = int(input("Enter a number: "))
factorial = 1
if num <0:
  print("Factirial does not exist for negative numbers")
elif num == 0:
  print("Factorial of 0 is 1")
else:
  for i in range(1, num+1):
     factorial = factorial*i
  print(f'The factorial of {num} is {factorial}')