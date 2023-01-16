import math

"""
# NAME: ODII MARSHALL CHIBUEZE
# REG NO: 20181091813
# FORM NUMBER:
"""

"""
  Q1. Mention and briefly explain the 3 common errors in python programming.

# Syntax errors: This occurs when the code is not written in the correct format according to the Python language.
  Examples include missing parentheses or colons.

#  Name errors: This occurs when a variable or function is not defined or not in the correct scope.
   An example would be trying to use a variable that has not been defined yet.

# Type errors: This occurs when an operation is attempted on the wrong type of value. For example, trying to add a number to a string.

"""

""" Q2.14 Write a program that prompts the user to enter three points (x1, y1), (x2, y2) and (x3, y3) of a triangle 
and display its area """


def triangle_area(x1, y1, x2, y2, x3, y3):
    # Calculate the lengths of the sides of the triangle
    a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    c = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
    # Calculate the semi-perimeter of the triangle
    s = (a + b + c) / 2
    # Calculate the area of the triangle using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


# Main program starts here
x1, y1 = input("Enter the coordinates of the first point (x1, y1): ").split(",")
x2, y2 = input("Enter the coordinates of the second point (x2, y2): ").split(",")
x3, y3 = input("Enter the coordinates of the third point (x3, y3): ").split(",")

x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)
x3 = float(x3)
y3 = float(y3)

area = triangle_area(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is:", area)

"""

2. Mention and briefly explain 3 common control structures in python programming

# If-else statements: This allow the programmer to specify different actions to be taken depending on whether a
  certain condition is true or false. It allows the execution of certain code blocks depending on the outcome of 
  the evaluation of a certain condition.

# For loops:  For loops allow the programmer to repeat a block of code a certain number of times. It is used for 
  iterating through a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# While loops, which allow the programmer to repeatedly execute a block of code as long as a certain condition 
  is true. It is used for iterating through a sequence as long as the certain condition is True.

"""

""" Q2.1 Write a program that reads a celsius degree from the console and converts it to Fahrenheit and displays 
the result """

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (9/5) * celsius + 32
print("Temperature in Fahrenheit:", fahrenheit)
