import random

keywords = ['Not A', 'Not B', 'Not C', 'A', 'B', 'C']
connection = ['AND', 'NAND', 'OR', 'NOR', 'XOR']

level = input("Choose what level you want 1,2,3: ")

if level == "1":
    print(f"({random.choice(keywords)} {random.choice(connection)} {random.choice(keywords)}) {random.choice(connection)} ({random.choice(keywords)} {random.choice(connection)} {random.choice(keywords)})")
elif level == "2":
    print(f"({random.choice(keywords)} {random.choice(connection)} {random.choice(keywords)}) {random.choice(connection)} ({random.choice(keywords)} {random.choice(connection)} {random.choice(keywords)}) {random.choice(connection)} ({random.choice(keywords)})")
elif level == "3":
    print(f"({random.choice(keywords)} {random.choice(connection)} {random.choice(keywords)}) {random.choice(connection)} ({random.choice(keywords)} {random.choice(connection)} {random.choice(keywords)}) {random.choice(connection)} ({random.choice(keywords)} {random.choice(connection)} {random.choice(keywords)})")