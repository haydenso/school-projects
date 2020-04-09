""""
1. For any given number, extract the 10s digit. For example, The tens digit in 1234 is 3.
2. Area of a right angled triangle calculator. Given values for base and height, print the area.
3. For any two digit number, swap the position of the digits. For instance, 79 becomes 97.
4. For any three digit number, print the sum of the three digits. For instance 273 becomes 12 (2+7+3)
5. For any given year, print the century that year belongs to. Remember that 1999 and 2000 were the
20th century, whereas 2001 was the beginning of the 21st century.
6. Given a number representing the number of seconds since midnight, print the time in 24hour clock
format. For example 70500 seconds should print a time of 19:35.
7. Area of a non-right angled triangle calculator. Given values for length a, length b and angle in degrees
C, return the area of the triangle (remember you will have to convert degrees to radians first).
8. For any given values for a, b and c, will provide the solutions to the quadratic formula (you may
assume both solutions are required). Be careful with your order of precedence. Here is an example
solution set for testing: If y=2x^2-4x-10 then the solutions are 3.44949 and -1.44949.
"""

print("Question 1")
problem = int(input("Type me a number please:"))
a = problem // 10
b = a % 10
print (b)

print("") #Space in the middle

print("Question 2")
a = float(input('Enter base of triangle:'))
b = float(input('Enter height of triangle: '))
# Base time height for area
c = (0.5*a*b)
print (c)

print("") #Space in the middle

print("Question 3")
problem = int(input("Type me any two digit number please:"))
digit1 = problem // 10
digit2 = problem % 10
new_number = digit2* 10 + digit1
print (new_number)

print("") #Space in the middle

print("Question 4")
problem = int(input("Q4. Type me any three digit number please:"))
digit1 = problem // 100
digit2 = problem // 10 % 10
digit3 = problem % 10
print ( digit1 + digit2 + digit3 )

print("") #Space in the middle

print("Question 5")
problem = int(input("Q5. Type me any year date please:"))
a = problem + 99
b = a // 100
print (b,"th century")

print("") #Space in the middle

#unfinished - not working
print("Question 6")
seconds = int(input("Q6. Type me a second :"))
minutes_since_midnight = seconds // 60
hours_since_midnight = minutes_since_midnight // 60
minutes_left_over = minutes_since_midnight - hours_since_midnight * 60
print (hours_since_midnight, minutes_since_midnight)
