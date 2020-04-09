
"""
1. Create a function area_right_angled_triangle(base, height) that returns the calculated area.
2. Create a function area_non_right_angled_triangle(base, height, angle) that returns the calculated area (remember you will need to convert the angle to radios before using it with the sine function).
3. Create a user input validation function that requires the input of a number.
4. Create a user input validation function that requires the input of a phone number (so +, spaces and - characeters are permitted).
5. Create a user input validation function that requires the input of a date in the dd/mm/yyyy format.
6. Create a user input validation function that accepts a list of strings as the parameter and presents them to the user as a list of menu choices, requiring the user to enter a number cooresponding to a valid choice before proceeding. For example if the code to run the funciton was….ction that accepts a list of strings as the parameter and presents them to the user as a list of menu choices, requiring the user to enter a number cooresponding to a valid choice before proceeding. For example if the code to run the funciton was….
"""

import math

#1
def area(base , height ):
    a: base * height / 2
    return a

""" not complete
def area_for_nonright_angle (base,height,angle):
    angle = math.sin(angle)
    workings = 1/2 * base * height * angle
    return workings
"""
    
#3
def input_confirmation(number):
    loop = True
    while loop:
        response = input(number)
        if response % 1 == 0:
            print(f"{response} is a number ")
            loop = False
        else:
            print("Only a number can be accepted")
    return response

#4
def input_validation_forphone(prompt):
    loop = True
    while loop:
        response = input(prompt)
        if '+' or ' ' or '-' in response:
            loop = False
        else:
            print ("include a telephone number with only + or -")
    return response

#5
def input_validation_fordate(date):
    loop = True
    while loop:
        response = input(date)
        if response.count("/") == 2:
            loop = False
        else:
            print("input valid date with the format dd/mm/yyyy ")

#6












