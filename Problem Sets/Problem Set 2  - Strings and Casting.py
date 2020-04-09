""""
#1. For any string that consists of exactly two words with one space separating them, swap the two words around. For example: Given the string Hello world!, have the program print world! Hello.
#2. Create a program that asks for two numbers, and then prints out:
  – The addition of those two numbers
  – The subtraction of the first number minus the second
  – The multiplication of the two numbers
– The division of the first number divided by the second.
#3. Given a sentence input, return how many words are in the sentence. For example, The quick brown fox jumps over the lazy dog. is 9 words.
#4. Given a string input of a date in format, dd/mm/yyyy, print an output advising the current day, month and year number.
"""

# 1.
phrase = str(input("enter two words separated by a space please: "))
space = phrase.find(' ')
print(phrase[space:] + " " + phrase[:space])

# 2.
number1 = int(input('Please type in a number'))
number2 = int(input('Please type in another number'))
a = number1
b = number2
add = a+b
subtr = a-b
mult = a*b
div = a/b
print (f"additon = {add}, subtraction = {subtr}, multiplication = {mult}, division = {div}")

# 3.
sentence = str(input('Write a sentence please'))
L = len(sentence.split())
print(f"There are {L} words")

#4.
# (I am unsure about what to do about this question
date = input("type in a date in the format dd/mm/yyyy")
day = [:1]
month = [3:4]
year = [6:9]
print (f" the day {day}, the month is {month}, the year is {year}")



