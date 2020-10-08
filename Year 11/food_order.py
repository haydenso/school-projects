import random
from collections import Counter 

class Menu():
    def __init__(self):
        self.items = [ {"name": "French Fries", "price": 2.00, "code": "FF"},
        {"name": "Quarter Pounder Burger", "price": 5.00, "code": "QPB"},
        {"name": "Quarter Pounder Cheeseburger", "price": 5.55, "code": "QPC"},
        {"name": "Half Pound Burger", "price": 7.00, "code": "HPB"},
        {"name": "Half Pound Cheeseburger", "price": 7.50, "code": "HPC"},
        {"name": "Medium Pizza", "price": 9.00, "code": "MP"},
        {"name": "Medium Pizza with Extra Toppings", "price": 11.00, "code": "MPWT"},
        {"name": "Large Pizza", "price": 12.00, "code": "LP"},
        {"name": "Large Pizza with Extra Toppings", "price": 14.50, "code": "LPWT"},
        {"name": "Garlic Bread", "price": 4.50, "code": "GB"} ]

    def show_menu(self):
        for item in self.items:
            print(f"{item['code']} - {item['name']}: ${item['price']}")
        return self.items

items_ordered = []
prices = []         # a list of all the prices

def rand_code():
    return random.randint(1111,9999)

def user_order(list_of_dict):
    print(f"\nYour Order Number: {rand_code()}")
    while True:
        id_of_order = str(input("\nWhat is the order code (input 0 to end): "))
        if id_of_order == "0":
            break
        else:
            quantity = input("How much of it do you want? ")
            for item in list_of_dict:
                if item['code'] == id_of_order:
                    prices.append(float(item['price']))
                    items_ordered.append(item['name'])
                    total = sum(prices)
            print(f"Your current total is ${total}")
            print(f"You have ordered {', '.join(items_ordered)}")
    return total
    
def find_profit(t):
    percentage = float(input("Input the percentage of the takings that are profts")) % 100
    profit = percentage * t
    print(f"The daily takings is ${t}, the profit is {round(profit)} and the percentage is {percentage}")

if __name__ == "__main__":
    print("\nWeclcome here is the menu:\n")
    menu = Menu()                            # initialising Menu Class
    menu_items = menu.show_menu()            # printing 
    total = user_order(menu_items)           # since the show_menu() returns the list of dicts, it is passed as a parameter for the user_order function
    find_profit(total)                       # takes the total returned from the previous function and finds the profit with the 'find_profit' function  