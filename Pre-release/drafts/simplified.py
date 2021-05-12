# TASK 1 - Start of Day 
up_times = ["9:00", "11:00", "13:00", "15:00"]  #Array of strings - variable
up_seats = [480, 480, 480, 480]   #Array of integers - variable
up_tally = [0, 0, 0, 0]     #Array of integers - variable
up_revenue = [0, 0, 0, 0]   #Array of integers - variable

down_times = ["10:00", "12:00", "14:00", "16:00"]
down_seats = [480, 480, 480, 640]
down_tally = [0, 0, 0, 0]
down_revenue = [0, 0, 0, 0] 

ticket_cost = 25 #integers - constant

print("\nJourney Up")
for i in range(0,4):
    print(f"{i+1}. {up_times[i]} - {up_seats[i]} seats")
print("\nJourney Down")
for i in range(0,4):
    print(f"{i+1}. {down_times[i]} - {down_seats[i]} seats")

# TASK 2 - Purchasing tickets

def calculate_revenue(session, revenue):
    for i in range(0,4):
        num_free_tickets = int(session[i]) // 10
        num_tickets_to_buy = session[i] - num_free_tickets
        cost = num_tickets_to_buy * ticket_cost
        revenue[i] += cost
    return revenue

# Tracks the current session
up_session = [0, 0, 0, 0] 
down_session = [0, 0, 0, 0]

#NUMBER OF PASSENGERS GOING UP --> while there are still seats avaiable to go up
while up_times != ["Closed", "Closed", "Closed", "Closed"]:
    num_passengers = input("\nHow many passengers are going? ")
    # Type check == Int and Range check 0 < x <= 80
    if num_passengers.isnumeric() and 0 < int(num_passengers) <= 80:               
        break
    else: 
        print("Please enter a valid number of passengers going on the trip")

#ASKING WHAT JOURNEY EACH PASSENGER IS GOING ON, CHECKING IF THERE IS STILL SPACE, CALCULATING SESSION TOTAL/REVENUE
for i in range(1, int(num_passengers) + 1):

    up = input(f"\nWhat time is passenger {i} going up? ")
    down = input(f"What time is passenger {i} going down? ")

    while up.isnumeric() and down.isnumeric():
        
        # if up_seats is not Closed and there are still seats available to be bought
        if up_seats[int(up)-1] != "Closed" and up_seats[int(up)-1] + up_tally[int(up)-1] <= up_seats[int(up)-1]:
            up_session[int(up)-1] += 1
        if down_seats[int(down)-1] != "Closed" and down_seats[int(down)-1] + down_tally[int(down)-1] <= down_seats[int(down)-1]:
            down_session[int(down)-1] += 1

        """
        for count, tally in zip(up_seats, up_tally):
            if count == tally: 
                count = "Closed"
        for count, tally in zip(down_seats, down_seats):
            if count == tally: 
                count = "Closed"
        """

        for i in range(0,4):
            if up_seats[i] == up_tally[i]:
                up_seats[i] = "Closed"
            if down_seats[i] == down_tally[i]:
                down_seats[i] = "Closed"
         
        #DISPLAY SCREEN
        print("\nJourney Up")
        for i in range(0,4):
            print(f"{i+1}. {up_times[i]} - {up_seats[i]} seats left")
        print("\nJourney Down")
        for i in range(0,4):
            print(f"{i+1}. {down_times[i]} - {down_seats[i]} seats left")
        break

    else:
        print(f"Please enter valid journey up and down for passenger {i}")

up_tally = [x + y for x, y in zip(up_session, up_tally)]
down_tally = [x + y for x, y in zip(down_session, down_tally)]

calculate_revenue(up_session, up_revenue)
calculate_revenue(down_session, down_revenue)

session_total_cost = sum(up_revenue) + sum(down_revenue)
print(f"This session's total is ${session_total_cost}")

# TASK 3
print("\nJourney Up")
for i in range(0,4):
        print(f"{i+1}. {up_times[i]} - {up_tally[i]} passengers - ${up_revenue[i]} made")
print("\nJourney Down")
for i in range(0,4):
        print(f"{i+1}. {down_times[i]} - {down_tally[i]} passengers - ${down_revenue[i]} made")

total_revenue = sum(up_revenue) + sum(down_revenue)
print(f"\nA total of ${total_revenue} has been made")
total_passengers = sum(up_tally) + sum(down_tally)
print(f"There are {int(total_passengers/2)} passengers today")
print(f"{up_times[up_tally.index(max(up_tally))]} had the most passengers") if max(up_tally) > max(down_tally) else print(f"{down_times[down_tally.index(max(down_tally))]} had the most passengers")

#Bugs in code:
# Do we get two free tickets if they go up and come down at the same time?
# Allows inputs over 4 (cannot be as no journey for it)