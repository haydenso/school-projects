#1
amount_words = 0
num_of_5 = 0
num_of_3 = 0

while amount_words < 1000:
    word = input("type in a word")
    amount_words += 1
    if len(word) >= 5:
        num_of_5 += 1
    elif len(word) <= 3:
        num_of_3 += 1
    print(f"there {num_of_5} number of words which had 5 or more characters; and there were {num_of_3} number of words which had 3 or less characters")

#2
sept_temps = []

temp = input("type in the temperatures of september in chronological order")
split = temp.split(" ")
for item in split:
    adding = sept_temps.append(float(item))
print(f"this is your input {sept_temps}")
average = sum(sept_temps) / len(sept_temps)
highest = max(sept_temps)
day_highest = sept_temps.index(highest)
print(f"Average temperature was {average} degrees; Highest temperature was {highest} degrees on September {day_highest + 1}")

#3
pos_count = 0
total = 0

is_valid = True
while is_valid and pos_count < 1000:
    num = int(input("enter a number"))
    if num > 0:
        pos_count += 1
        total = total + num
        is_valid = True
    elif num == 0:
        print("the count has finished since 0 was inputted")
        is_valid = False
    else:
        is_valid = True
print(f"the number of positive numbers counted is {pos_count} and the sum of all the positive number was {total}")

#4
"""
a: list of string
b: string
c: float
d: 
e:
"""

#5
list = []
total = 0
lowest = list[0]
highest = list[0]

for words in list:
    total = total + int(len(words))
    average = total / len(list)
    if len(words) < len(lowest):
        lowest = words
    elif len(words) > len(highest):
        highest = words
print(f"the average characters was {average}")
print(f"the word with least characters is {lowest}")
print(f"the word with most characters is {highest}")

#6a
birthdate = '29/09/2005'
parts = birthdate.split('/')
print(f"You were born on {parts[0]} on the month {parts[1]} in the year {parts[2]}")

#6b


def day_suffix (number):
    if number % 10 == 1:
        return str(number) + 'st'                               # convert back to string so they can be printed together
    elif number % 10 == 2:
        return str(number) + 'nd'
    elif number % 10 == 3:
        return str(number) + 'rd'
    else:
        return str(number) + 'th'


def month_name (number):
    if number == 1:
        return "January"
    elif number == 2:
        return "February"
    elif number == 3:
        return "March"
    elif number == 4:
        return "April"
    elif number == 5:
        return "May"
    elif number == 6:
        return "June"
    elif number == 7:
        return "July"
    elif number == 8:
        return "August"
    elif number == 9:
        return "September"
    elif number == 10:
        return "October"
    elif number == 11:
        return "November"
    elif number == 12:
        return "December"


date = []

birthdate = input('Type in your birthday in the format of DD/MM/YYYY')
parts = birthdate.split('/')
for n in parts:
    adding_casting = date.append(int(n))        # change to integer so modulus can be done for finding the suffix for day
day = day_suffix(date[0])
month = month_name(date[1])
year = date[2]
print(f"You were born on {day} of {month} in the year {year}")
