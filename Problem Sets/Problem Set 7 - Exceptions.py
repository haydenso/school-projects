""""
Q1. Create a quadratic formula calculator that uses exceptions…

to ensure the a, b and c entered by the user are numbers
to detect if a is zero (would result in a division by zero)
to detect if there are no real solutions (square root of a negative number exception)

Q2. Question 5 of the Files problem set reads “Read a list of strings from a text file. Tell the user how many lines there are and ask them to enter a line number indicating one they would like to read. Print just the content of that line to the user”.

Add exception handling in case the file does not exist.
Add exception handling in case the user asks for a line number beyond the limits of the list (ie: if there are only 5 lines and the user askes for line 6).
"""


class Colors:
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    YELLOW = "\033[1;33m"
    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"

import math


# Question 1

print(Colors.BOLD + "Welcome! This is a Quadratic Formula solver and require 3 inputs; where ax^2 + bx + c = 0 \n")

loop = True

while True:                # while loop so it keeps looping
    try:
        a = float(input(Colors.BOLD + "Input a (note it cannot be 0): "))
        if a == 0:
            raise SyntaxError("a cannot be 0")      # forcing an exceptions so the user can be notified
        b = float(input(Colors.BOLD + "Input b: "))
        c = float(input(Colors.BOLD + "Input c: "))

        d = b ** 2 - 4 * a * c          # discriminant (to find how many possible solutions there are)
        try:
            if d == 0:
                answer = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a      # quadratic formula
                print(Colors.BOLD + f"\nThis equation has one solutions: {answer}")
                print(Colors.END)
            else:                        # assuming if the answer is not one solution, it will either have 2 or none. if there are none there would be a ValueError and that is addressed
                ans1 = (-b + math.sqrt((b ** 2) - (4 * (a * c)))) / (2 * a)
                ans2 = (-b - math.sqrt((b ** 2) - (4 * (a * c)))) / (2 * a)
                print(Colors.BOLD + f"\nThis equation has two solutions: {ans1} and {ans2}")
                print(Colors.END)
        except ValueError:                      # addressing the math domain error (if no solutions)
            print(Colors.RED + "\nNo possible solutions")
            print(Colors.END)

        end = input("input 0 if you wish to end the program, if not, enter anything else continue: ")
        if end == '0':
            break
        else:
            print("")     # printing empty line for spacing purposes
            continue

    except ValueError:            # not a number inputted
        print(Colors.RED + "\nSomething apart from numbers was inputted")
        print(Colors.END)
    except SyntaxError:           # a forced syntax error for if the input is 0
        print(Colors.RED + "\nvalue of 'a' cannot be 0")
        print(Colors.END)


# Question 2
print(Colors.BOLD + "\nText file Opener")
print(Colors.END)
filename = input(Colors.GREEN + "input file name and file path location in correct format (eg ../Misc/hangperson-words.txt): ")
print(Colors.END)

try:
    with open(filename, "r") as f:  # "r" as read and "w" as write
        content = f.read()              # loading content
        lines = content.splitlines()    # splitting contents of the txt file
        line_num = int(input(Colors.BOLD + "enter a line number for that line to open: "))  # line wanting to print
        print(Colors.END)
        print(Colors.BOLD + "The line is: " + Colors.END)                     # the line is printed below
        print(Colors.ITALIC + f"\"{lines[line_num - 1]}\" ")                 # minus 1 as index counts with first being a 0
except FileNotFoundError:
    print(Colors.RED + "file not found, please enter correct file name and path")
    print(Colors.END)
except IndexError:
    print(Colors.RED + "line number invalid as such does not exist within the file")
    print(Colors.END)




