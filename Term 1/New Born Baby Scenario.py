"""
SCENARIO:
A new born baby is kept in a cot in a hospital; the temperature of the baby is monitored every 10 minutes.
The temperature of the baby is recorded in degrees Celsius to one decimal place and must be within the
range 36.0°C to 37.5°C.

TASK 1:
Input temperature; The routine should check whether the temperature is within the acceptable range, too high or too
low and output a suitable message in each case.

TASK 2:
Write another routine that stores the temperatures taken over a three hour period in an array. This routine
should output the highest and lowest temperatures and calculate the difference between these
temperatures.

TASK 3:
For a baby who has a temperature difference of more than one degree Celsius, and/or has been outside the
acceptable range more than twice in the three hour period, output a suitable message giving a summary of
the problem.

LINK for colorama: https://github.com/tartley/colorama

"""
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

while time < 180:                                  # 180 mins set because 3 hour period (change to 40 for testing so that there is no need for 18 number inputted)
    temp = float(input(Fore.MAGENTA + "\nPlease input the baby's temperature in °C: "))
    time += 10            # temperature recorded every ten minutes
    print(Style.RESET_ALL)
    print("\033[1;33m" + f"After {time} minutes of birth: {temp}°C")
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
    print(Fore.GREEN + f"The current highest recorded temperature was {highest}°C and the current lowest was {lowest}°C. The current difference was {difference}°C")
    print(Style.RESET_ALL)

    # TASK 3
    if outside > 2:
        print(Fore.RED + '\033[1m' + "WARNING: temperature of baby has been outside of suitable range more than two times")
        print(Style.RESET_ALL)
    elif difference > 1.0:
        print(Fore.RED + '\033[1m' + "WARNING: difference in temperature is over 1°C")
        print(Style.RESET_ALL)
    else:
        print(Fore.GREEN + "No abnormalities have been discovered yet")
        print(Style.RESET_ALL)

    temp_num = len(list)

print(Fore.YELLOW + '\033[1m' + Colors.UNDERLINE + "Summary" + Colors.END)              # Underlined + bold Text
print(Fore.RED + '\033[1m' + f" The highest recorded temperature was {highest}°C")
print(Fore.BLUE + '\033[1m' + f" The lowest temperature was {lowest}°C")
print(Fore.WHITE + '\033[1m' + f" The difference was {difference}°C")
print(Fore.GREEN + '\033[1m' + f" The list of temperature inputted chronologically was:")
print(Fore.WHITE + f"  {list}")
print(Fore.WHITE + '\033[1m' + f" There were {temp_num} temperatures were inputted over the 3 hour period")
print(Fore.RED + '\033[1m' + f" There were {outside} temperature outside normal range")


