# TASK 1 - Start of Day 
up_times = ["9:00", "11:00", "13:00", "15:00"]  #Array of strings - variable
up_seats = [480, 480, 480, 480]     #Array of integers - variable
up_tally = [0, 0, 0, 0]             #Array of integers - variable
up_revenue = [0.0, 0.0, 0.0, 0.0]   #Array of real - variable

down_times = ["10:00", "12:00", "14:00", "16:00"]
down_seats = [480, 480, 480, 640]
down_tally = [0, 0, 0, 0]
down_revenue = [0.0, 0.0, 0.0, 0.0] 

ticket_cost = 25.0 #real/float - constant

def screenDisplay():
    print("\nJourney Up")
    for i in range(0,4):
        if up_seats[i] == up_tally[i]: 
            seats = "Closed"
        else:
            seats = up_seats[i] - up_tally[i]
        print(f"{i+1}. {up_times[i]} - {seats}") 
        
    print("\nJourney Down")
    for i in range(0,4):
        if down_seats[i] == down_tally[i]:
            seats = "Closed"
        else:
            seats = down_seats[i] - down_tally[i]
        print(f"{i+1}. {down_times[i]} - {seats}")

screenDisplay()

# TASK 2 - Purchasing tickets
def calculate_revenue(journey, num, revenue):
    num_tickets_to_buy = int(num) - int(num) // 10 # total - free tickets
    revenue[int(journey)-1] += num_tickets_to_buy * ticket_cost
    return revenue

while up_times != up_tally:
    
    while True:
        num_passengers = input("\nHow many passengers are going? ") 
        if num_passengers.isnumeric() and 0 < int(num_passengers) <= 80: # Type check == Int and Range check 0 < x <= 80
            num_passengers = int(num_passengers)
            break
        else:
            print("Invalid input, number must be in between 1 and 80")

    while True:
        up = input(f"\nUp Journey Time? ")
        up_index = int(up)-1
        if up_index <= 3 and up_seats[up_index] - up_tally[up_index] >= num_passengers: # Range check
            up_tally[up_index] += num_passengers
            calculate_revenue(up, num_passengers, up_revenue)
        else: 
            print("Sorry invalid choice or not enough seats")
            continue

        down = input(f"Down Journey Time? ")
        down_index = int(down) - 1 
        if down_index <= 3 and down_seats[down_index] - down_tally[down_index] >= num_passengers and down_index >= up_index:
            # checks if it is a valid choice, checks if there are enough seats, check if the journey is after their up journey
            down_tally[down_index] += num_passengers
            calculate_revenue(down, num_passengers, down_revenue)
            break
        else: 
            print("Sorry invalid choice / you chose a time before your up journey or not enough seats")
            continue
    
    screenDisplay() 
    booking = input("\nCreate another booking? Type n to stop, anything else to continue ")
    if booking.lower() == 'n':
        break

# TASK 3
total_passengers = 0
max_passengers = up_tally[0]
max_time = up_times[0]

print("\nJourney Up")
for i in range(0,4):
        print(f"{i+1}. {up_times[i]} - {up_tally[i]} passengers - ${up_revenue[i]} made")
        total_passengers += up_tally[i] 
        if up_tally[i] > max_passengers:
            max_passengers = up_tally[i]
            max_time = up_times[i]

print("\nJourney Down")
for i in range(0,4):
        print(f"{i+1}. {down_times[i]} - {down_tally[i]} passengers - ${down_revenue[i]} made")
        if down_tally[i] > max_passengers:
            max_passengers = down_tally[i]
            max_time = down_times[i]

total_revenue = 0
combined_revenue = up_revenue + down_revenue
for i in combined_revenue:
    total_revenue += i

print(f"\n${total_revenue} total revenue, {total_passengers} total passengers, {max_time} had the most passengers, with {max_passengers} passengers")