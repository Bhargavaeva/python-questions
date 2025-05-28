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
