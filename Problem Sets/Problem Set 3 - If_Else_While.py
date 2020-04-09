"""
1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).

2. Suppose you ask the user what the temperature is. Create a program that will respond as follows:
– If the temperature is between 20 and 27, say that it is “Just right”
– If the temperature is below 20, say that it is “too cold”
– If the temperature is above 27, say that it is “too hot”

3. The fibonacci sequence is created by summing the two previous numbers together. The first 10
numbers in the sequence are 1, 1, 2, 3, 5, 8, 13, 21, 34, 55. Use a while() loop to create a program
that will calculate the n-th number of the sequence. For instance, if asked for the 8th number, it should
provide the answer of 21.

4. Create a program that allows the user to input the sides of any triangle, and then return True/False to
indicate if the triangle is a Pythagorean Triple or not.
10. Write a Python program which iterates the integers from 1 to 50. For multiples of three print
“Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are
multiples of both three and five print “FizzBuzz”.

5. Write a Python program to check a triangle is equilateral, isosceles or scalene. An equilateral triangle
is a triangle in which all three sides are equal. A scalene triangle is a triangle that has three unequal
sides. An isosceles triangle is a triangle with (at least) two equal sides.

6. Write a Python program to construct the following pattern, using a nested for loop.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

8. Write a Python program to check the validity of password input by users. The rules for a valid
password are:
• At least 1 letter between [a-z] and 1 letter between [A-Z].
• At least 1 number between [0-9].
• At least 1 character from [$#@].
• Minimum length 6 characters.
• Maximum length 16 characters.
"""

#1
n = 2000
while n <= 3200:
    if n % 7 == 0:
        print(f"{n} is divisible by 7")
        if not (n % 5 == 0):
            print(f"{n} is not divisble by 5")
    n = n + 1

#2
a = int(input("What is the temperature today?"))
if a <= 20:
    print(f" it is {a} degrees. It is too cold.")
elif a >= 27:
    print(f" it is {a} degrees. It is too hot")
else: print (f" it is {a} degrees. It is just right")

#3
n = int(input("Enter nth number of fibonnaci sequence"))
current_position = 2
prev1 = 1
prev2 = 1
while current_position < n:
    current_value = prev1 + prev2
    prev1 = prev2
    prev2 = current_value
    current_position = current_position + 1
    print(f"the {current_position}-th number is {current_value}")

#4
n = int(input ("Enter number between 1-50"))
if n % 3 ==0 and n % 5==0:
    print("Fizzbuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5==0:
    print("Buzz")
else:
    print(n)

#5
side1 = int(input("Input Side 1"))
side2 = int(input("Input Side 2"))
side3 = int(input("Input Side 3"))
if side1 == side2 and side2 == side3 and side1 == side3:
    print("It is an Equalilateral Triangle")
elif side1 == side2:
    print("It is an isoceles trinagle")
else:
    print ("It is a scalene triangle")

#6
num_of_rows = int(input("How many rows"))
# Growing Triangle
row_number = 1
while row_number < num_of_rows:
    # Print Stars for this row
    line = ""
    num_stars = row_number
    star_number = 1
    while star_number <= num_stars:
        line = line + "*"
        star_number = star_number + 1
    print(line)
    # Increment for next row
    row_number = row_number + 1

# Shrinking triangle
while row_number > 0:
    # print stars for this now
    line = " "
    num_stars = row_number
    star_number = 1
    while star_number <= num_stars:
        line = line + "*"
        star_number = star_number + 1
    print(line)
    # Decrement for next row
    row_number = row_number - 1

#8
import re
print('Password Checker')
print('The Rules are the following 1) at least 1 letter from (a-z) 2) one letter from (A-Z) 3) A number from (1-9) 4) a character from ($@#)')
print('It must be between  6 letters and 16 characters ')
while True:
    user_input = input("Type your password : ")
    is_valid = False
    if (len(user_input)<6 or len(user_input)>12):
        print("Not Valid it should be between 6 and 12 characters")
        continue
    elif not re.search("[A-Z]" ,user_input):
        print("Not Valid it should contain a letter from [A-Z]")
        continue
    elif not re.search("[a-z]", user_input):
        print("Not Valid it should contain a letter from [a-z]")
        continue
    elif not re.search("[1-9]", user_input):
        print("Not Valid needs to contain a number from [1-9]")
        continue
    elif not re.search("[$#@]", user_input):
        print("Not Valid needs a symbol from [$#@]")
        continue
    else :
        is_valid = True
        break
if(is_valid):
    print("Password is Valid")


