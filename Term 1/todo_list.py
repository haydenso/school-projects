"""
Process:
1. Open file, create one if it does not exist
2. Ask for task
    - name and date (make sure format is a date)
3. Print tasks
    - keep track of count
4. Ask user what action they would like to do next
    - store whatever is changed

possible flaws:
-  cannot detect if the activity has already passed
"""

from datetime import datetime
from colorama import Fore, Style
import os
import random


class Colors:
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"


def openfile(alltasks):                                     # opens file
    try:
        with open("todo.txt", 'r') as file:
            details = file.readlines()
            for lines in details:                            # appends everything into a list so it is easier to print
                alltasks.append(lines)
            return alltasks
    except FileNotFoundError:                               # if file not found
        print("\033[1m" + "No file found, creating one" + "\033[0m")
        file = open("todo.txt", "w+")                         # creates file in the same folder the python file is
        details = file.read().splitlines()
        return details


def addingtask(n, d):                                     # n for name and d for date
    with open("todo.txt", 'a') as file:
        while True:
            try:
                d = datetime.strptime(d, "%d/%m/%y")
                today = datetime.today()
                difference = (d - today).days
                if difference < 0:
                    raise ValueError(Fore.RED + 'The date is in the past!' + Style.RESET_ALL)           # if the number is negative, it means the date has passed already so it forces an error (today doesnt work either)
                file.write(f"{n}/{difference + 1}")
                file.write("\n")
                file.close()
                break
            except ValueError:
                d = input(Fore.RED + "INVALID DATE - Please input a valid date: " + Style.RESET_ALL)           # new input
                continue


def remove(alltasks, line):                                       # removes the task from the list and rewrites the activities present
    with open("todo.txt", 'w') as file:
        alltasks.pop(line - 1)                                      # the counting starts at 0
        for todo in alltasks:
            file.write(todo)
            file.close()
    return alltasks


def quote():         # Task 3 (opens file, generates random word)
    with open("motivationalquotes.txt", "r") as w:           # Open file for reading
        words = w.read()                                   # Load entire file into 1 large string
        quotes = words.split("\n\n")                         # Split into lines
        chosen = random.choice(quotes)
    return chosen


loop = True                                           # outer loop

while loop:
    alltasks = []
    tasks = openfile(alltasks)                         # opens file to read
    print(Fore.CYAN + "\033[1m" + "\nHere is a motivational quote! " + "\033[0m" + Style.RESET_ALL)
    print(Fore.BLUE + "\033[3m" + quote() + Style.RESET_ALL + "\033[0m")
    print("\033[1m" + "\033[4m" + Fore.GREEN + "\nWelcome your tasks are:" + "\033[0m" + Style.RESET_ALL)
    count = 1
    if len(tasks) > 0:                         # if there are tasks present, continue down this path
        for todo in alltasks:
            if "\n" in todo:
                todo = todo.replace("\n", "")                    # the "\n" messes up the formatting so I remove it
            sections = todo.split("/")                    # splitting the name and the time difference
            print(f"{count}. {sections[0] :<20} Due in: {sections[1]} day(s)")
            count += 1                                                     # keeping track on number of tasks

        print(Fore.RED + "\nDelete task --> input task number" + Style.RESET_ALL)
        print(Fore.BLUE + "Create task --> type c" + Style.RESET_ALL)
        print(Fore.GREEN + "End --> type 0" + Style.RESET_ALL)
        action = input("\033[1m" + "\nWhat would you like to do next: " + "\033[0m")

        loop2 = True                                           # loop until valid response is sent
        while loop2:                                           # keep looping until a loop2 input is inputted
            if action == 0 or action == "0":
                loop2 = False
                loop = False                                                                   # break from outer loop

            elif action.isnumeric() and int(action) <= len(alltasks):      # if the number is numeric is within the list
                remove(alltasks, int(action))
                loop2 = False

            elif action == "c":
                name = input("\033[1m" + "\nType name of task: " + "\033[0m")
                date = input("\033[1m" + "Input date due in DD/MM/YY: " + "\033[0m")
                addingtask(name, date)
                loop2 = False

            else:
                print(Fore.RED + "Invalid input" + Style.RESET_ALL)
                action = input(Fore.RED + "What would you like to do" + Style.RESET_ALL)
                loop2 = True

    else:                                                          # no existing tasks
        print(Fore.BLUE + "\033[1m" + "You currently have no existing tasks" + "\033[0m" + Style.RESET_ALL)

        loop3 = True
        while loop3:
            print("\nPress 0 --> end and close program")
            print("Press 1 --> add a new task")
            choice = input("\nYour choice: ")

            if choice == "1" or choice == 1:
                name = input("\033[1m" + "\nType name of task: " + "\033[0m")
                date = input("\033[1m" + "Input date due in DD/MM/YY: " + "\033[0m")
                addingtask(name, date)                                     # loops again
                loop3 = False                                             # breaks from this smaller loop

            elif choice == "0" or choice == 0:
                loop3 = False                                                # break from this smaller loop
                loop = False                                                 # outer loop, end program completely

            else:
                print("Invalid input!!!")
                loop3 = True                                     # loop back to start so another value can be inputted


