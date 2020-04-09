"""
1. Write a program to sum all the items in a list.
2. Write a program to get the largest number from a list.
3. Write a program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
4. Write a program to remove duplicates from a list.
5. Write a function that takes two lists and returns True if they have at least one common member.
6. Write a program to print a specified list after removing the 0th, 4th and 5th elements. Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'] Expected Output : ['Green', 'White', 'Black']
7. Write a program to print the numbers of a specified list after removing even numbers from it.
8. Write a program to select an item randomly from a list, which is then removed from the original list so it can’t be re-drawn (just like a deck of cards scenario)
9. Write a program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).
10. Given two lists, write a program to print the items that are not in both lists.
11.Write a program to append the items from one list to a second list.
12. Write a program for computing primes up to 1000. Hint: Google for the Sieve of Eratosthenes
"""

# Unfinished Problem Set

#1
info = input("Type a bunch of numbers in")
parts = info.split(" ")
numbers = []
for item in parts:
    numbers.append(int(info))
total = sum(info)
print(f"The total was {total}")

#2
info = input("Type a bunch of numbers in")
parts = info.split(" ")
numbers = []
result = max(info)
print(result)

#3
data = ["hi", "hello", "s", "there", "boo", "h"]
count = 0
for item in data:
    if len(item) >= 2:
        count = count + 1
print(f"There are {count} items of length 2 or more")

#4
for item in list:
    print(item)
    location = list.index(item)

#7
nums = [1,2,3,4,5,6,7,8,9]
position = 0
while position < len(nums):
    num = nums[position]
    if num % 2 == 0:
        print(f"{num} is even, removing it")
        nums.pop(position)
    else:
        print(f"{num} is odd, moving on to the next")
        position = position + 1
print(nums)

#8
collection = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
collection.pop (0)
print(collection)


