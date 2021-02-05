coach_cost = 550
ticket_cost = 30
max_students = 45

while True:
    num_students = int(input("Number of students taking part on the trip: "))
    if 0 <= num_students <= max_students:
        break
    else:
        print("Number of students out of range, please enter a valid number")

free_tickets = num_students//11

number_tickets = num_students - free_tickets
estimated_total_cost = coach_cost + (number_tickets * ticket_cost)
cost_per_student = round(estimated_total_cost/num_students, 1)  

print(f"Each student has to pay ${cost_per_student}, there are {free_tickets} free tickets")

names = []
payments = []

while len(names) <= 45:
    name = input("Enter the name of the student taking part (enter X to stop): ")
    if name == "X":
        break
    else:
        names.append(name)

    while True:
        payment = input("Enter if they have payed: ")
        if payment == "Yes" or payment == "No":
            payments.append(payment)
            break
        else:
            print("Please enter either Yes or No.")
            continue

paid = payments.count("Yes")

collected_total = cost_per_student * paid 
print(f"You have collected ${collected_total} with {paid} students paid")

difference = collected_total - estimated_total_cost

if difference > 0.0:
    print(f"Made a profit of ${difference}")
elif difference < 0.0:
    print(f"Made a lost of ${difference}")
elif difference == 0.0:
    print("0 profit made or lost (even)")