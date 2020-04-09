from colorama import Fore, Style


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


list = []               # array of temperature
time = 0                # minutes past (3 hour period)
outside = 0             # number of abnormal temperatures

temp = input(Fore.MAGENTA + "Please input the baby's temperature in °C: ")
print(Style.RESET_ALL)

while time < 180:                                 # 180 mins set because 3 hour period (change to 40 for testing so that there is no need for 18 number inputted)
    time += 10                                    # temperature recorded every ten minutes

    while True:
        if temp.replace(".", "", 1).isnumeric():
            temp = float(temp)
            print("\033[0;32m" + "Is a valid number for temperature" + "\033[0m")
            print(Style.RESET_ALL)
            break
        else:
            print("\033[0;31m" + "Not numeric or valid temperature input" + "\033[0m")     # error message, invalid value not stored
            temp = input(Fore.RED + '\033[1m' + "\nPlease input the baby's temperature in °C again: ")   # asking for new valid temperature inputted
            print(Style.RESET_ALL)

    print("\033[1;33m" + f"Temperature after {time} minutes of birth: {temp}°C")
    print(Style.RESET_ALL)

    # TASK 1:
    if temp > 37.5:
        print(Fore.RED + '\033[1m' + "Temperature is too high")
        outside += 1
        print(Style.RESET_ALL)
    elif temp < 36.0:
        print(Fore.BLUE + '\033[1m' + "Temperature is too low")
        outside += 1
        print(Style.RESET_ALL)
    else:
        print(Fore.GREEN + "Temperature is normal")
        print(Style.RESET_ALL)

    # TASK 2:
    list.append(temp)
    highest = list[0]
    lowest = list[0]
    for n in list:
        if n > highest:
            highest = n
        elif n < lowest:
            lowest = n
    difference = highest - lowest
    print(Fore.GREEN + f"The current highest recorded temperature was {highest}°C and the current lowest is {lowest}°C. The current difference was {difference}°C")
    print(Style.RESET_ALL)

    # TASK 3
    if outside > 2.0:
        print(Fore.RED + '\033[1m' + "WARNING: temperature of baby has been outside of suitable range more than two times")
        print(Style.RESET_ALL)
    elif difference > 1.0:
        print(Fore.RED + '\033[1m' + "WARNING: difference in temperature is over 1°C")
        print(Style.RESET_ALL)
    else:
        print(Fore.GREEN + "No abnormalities have been discovered yet")
        print(Style.RESET_ALL)

    temp_num = len(list)

    print(Fore.YELLOW + '\033[1m' + Colors.UNDERLINE + "Summary" + Colors.END)  # Underlined + bold Text
    print(Fore.RED + '\033[1m' + f" The highest recorded temperature was {highest}°C")
    print(Fore.BLUE + '\033[1m' + f" The lowest temperature was {lowest}°C")
    print(Fore.WHITE + '\033[1m' + f" The difference was {difference}°C")
    print(Fore.GREEN + '\033[1m' + f" The list of temperature inputted chronologically was:")
    print(Fore.WHITE + f"  {list}")
    print(Fore.WHITE + '\033[1m' + f" There were {temp_num} temperatures were inputted over the 3 hour period")
    print(Fore.RED + '\033[1m' + f" There were {outside} temperature outside normal range")

    temp = input(Fore.MAGENTA + "\nPlease input the baby's temperature in °C: ")

print("Baby Monitoring Program Ended")              # Ends after 3 hour period


