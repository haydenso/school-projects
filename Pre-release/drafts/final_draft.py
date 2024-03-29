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
        print(f"{i+1}. {up_times[i]} - {up_seats[i]} seats")
    print("\nJourney Down")
    for i in range(0,4):
        print(f"{i+1}. {down_times[i]} - {down_seats[i]} seats")

screenDisplay()

# TASK 2 - Purchasing tickets
def calculate_revenue(journey, num, revenue):
    num_free_tickets = int(num) // 10
    num_tickets_to_buy = int(num) - num_free_tickets
    cost = num_tickets_to_buy * ticket_cost
    revenue[int(journey)-1] += cost
    return revenue

#NUMBER OF PASSENGERS GOING UP --> while there are still seats avaiable to go up
while up_times != ["Closed", "Closed", "Closed", "Closed"]:
    num_passengers = input("\nHow many passengers are going? ")
    # Type check == Int and Range check 0 < x <= 80
    if num_passengers.isnumeric() and 0 < int(num_passengers) <= 80: 
        up = input(f"\nUp Journey Time?")
        down = input(f"Down Journey Time?")

        while up.isnumeric() and down.isnumeric():
            
            # if up_seats is not Closed and there are still seats available to be bought
            up_index = int(up) - 1
            down_index = int(down) - 1
            if up_seats[up_index] != "Closed" and up_seats[up_index] + up_tally[up_index] <= up_seats[up_index]:
                up_tally[up_index] += int(num_passengers)
            if down_seats[down_index] != "Closed" and down_seats[down_index] + down_tally[down_index] <= down_seats[down_index]:
                down_tally[down_index] += int(num_passengers)

            calculate_revenue(up, num_passengers, up_revenue)
            calculate_revenue(down, num_passengers, down_revenue)

            for i in range(0,4):
                if up_seats[i] == up_tally[i]:
                    up_seats[i] = "Closed"
                if down_seats[i] == down_tally[i]:
                    down_seats[i] = "Closed"

            screenDisplay() 
            
            booking = input("Create another booking (y/n)?")
            if booking.lower() == 'n':
                break
            else:
                continue
                
    else:
        print(f"Please enter valid journey up and down for passenger")    



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
print(f"\n${total_revenue} total revenue, {int(total_passengers)} total passengers")

if max(up_tally) > max(down_tally):
    index = up_tally.index(max(up_tally))
    print(f"{up_times[index]} had the most passengers")
else: 
    index = down_tally.index(max(down_tally))
    print(f"{down_times[index]} had the most passengers")