# TASK 1 - Start of Day 
up_times = ["9:00", "11:00", "13:00", "15:00"]  #Array of strings - variable
up_seats = [480, 480, 480, 480]   #Array of integers - variable
up_tally = [0, 0, 0, 0]     #Array of integers - variable
up_revenue = [0.0, 0.0, 0.0, 0.0]   #Array of real - variable

down_times = ["10:00", "12:00", "14:00", "16:00"]
down_seats = [480, 480, 480, 640]
down_tally = [0, 0, 0, 0]
down_revenue = [0.0, 0.0, 0.0, 0.0] 

ticket_cost = 25.0 #real/float - constant

def screenDisplay():
    print("\nJourney Up")
    for i in range(0,4):
        if up_seats[i] == up_tally[i]: # the up_seats - up_tally no longer works when if up_seats[i] is closed
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
    num_free_tickets = int(num) // 10
    num_tickets_to_buy = int(num) - num_free_tickets
    cost = num_tickets_to_buy * ticket_cost
    revenue[int(journey)-1] += cost
    return revenue

def passengerCount_input():
    while True:
        num_passengers = input("\nHow many passengers are going? ") 
        # Type check == Int and Range check 0 < x <= 80
        if num_passengers.isnumeric() and 0 < int(num_passengers) <= 80:
            return int(num_passengers)
            break
        else:
            print("Invalid input, number must be in between 1 and 80")

#NUMBER OF PASSENGERS GOING UP --> while there are still seats avaiable to go up
while up_times != up_tally:
    
    num_passengers = passengerCount_input()

    while True:
        up = input(f"\nUp Journey Time? ")
        up_index = int(up)-1
        if up_index <= 3 and up_seats[up_index] - up_tally[up_index] >= num_passengers:
            up_tally[up_index] += num_passengers
            calculate_revenue(up, num_passengers, up_revenue)
        else: 
            print("Sorry invalid choice or not enough seats")
            continue

        down = input(f"Down Journey Time? ")
        down_index = int(down) - 1 
        if down_index <= 3 and down_seats[down_index] - down_tally[down_index] >= num_passengers:
            down_tally[down_index] += num_passengers
            calculate_revenue(down, num_passengers, down_revenue)
            break
        else: 
            print("Sorry invalid choice or not enough seats")
            continue
    
    screenDisplay() 
    booking = input("\nCreate another booking (y/n)? ")
    # this is not completely validated, is it ok
    if booking.lower() == 'n':
        break

# TASK 3
print("\nJourney Up")
for i in range(0,4):
        print(f"{i+1}. {up_times[i]} - {up_tally[i]} passengers - ${up_revenue[i]} made")
print("\nJourney Down")
for i in range(0,4):
        print(f"{i+1}. {down_times[i]} - {down_tally[i]} passengers - ${down_revenue[i]} made")

total_revenue = sum(up_revenue) + sum(down_revenue)
total_passengers = sum(up_tally) 
# total passenger is the sum of up and down? or total number of unique passengers
print(f"\n${total_revenue} total revenue, {total_passengers} total passengers")

if max(up_tally) > max(down_tally):
    index = up_tally.index(max(up_tally))
    print(f"{up_times[index]} had the most passengers")
elif max(up_tally) < max(down_tally):
    index = down_tally.index(max(down_tally))
    print(f"{down_times[index]} had the most passengers")