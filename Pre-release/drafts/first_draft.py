# TASK 1 - Start of Day 
# status default value is "open" and is update to "Closed" when seats == tally
up_times = ["9:00", "11:00", "13:00", "15:00"]
up_seats = [480, 480, 480, 480]
up_tally = [0, 0, 0, 0]
up_revenue = [0, 0, 0, 0]
up_status = ["open", "open", "open", "open"]

down_times = ["10:00", "12:00", "14:00", "16:00"]
down_seats = [480, 480, 480, 640]
down_tally = [0, 0, 0, 0]
down_revenue = [0, 0, 0, 0]
down_status = ["open", "open", "open", "open"]

ticket_cost = 25
# $25 each journey (and not $50 round trip) because when we go up we might have enough people for a free ticket, however we come down different times

def screen_display(times, seats):
    for i in range(0,4):
        print(f"{i+1}. {times[i]} - {seats[i]} seats")
    
print("\nJourney Up")
screen_display(up_times, up_seats)
print("\nJourney Down")
screen_display(down_times, down_seats)

# TASK 2 - Purchasing tickets
def check_seats(time, times, status, tally, session):
        if status != "Closed":
            print(f"\n{times[time-1]} journey seat allocated")
            tally[time-1] += 1
            session[time-1] += 1
            return True
        else:
            print(f"\nSorry {times} full already")
            return False

def calc_revenue(session, revenue): 
    for i in range(0,4):
        num_free_tickets = int(session[i]) // 10
        num_tickets_to_buy = session[i] - num_free_tickets
        # $25 being the ticket
        cost = num_tickets_to_buy * ticket_cost
        revenue[i] += cost

# While there are still spaces for going up 
while up_status != ["Closed", "Closed", "Closed", "Closed"]:
    # session running totals for finding number of free tickets, it resets back to 0 after each session closes
    up_session = [0, 0, 0, 0] 
    down_session = [0, 0, 0, 0]

    # Ask for how many passengers 1-80 inclusive
    while True:
        num = int(input("\nNumber of passengers going: "))
        if 1 <= num <= 80:
            break
        else:
            print("Invalid number of tickets (Must be between 1 and 80 inclusive)")

    # Ask individually each passenger
    for i in range(1,num+1):
        while True:
            # Ask for the journey number as listed from task 1 (e.g input 1 is 9:00)
            time_up = int(input(f"\nWhich journey down is passenger {i} going on? "))
            time_down = int(input(f"Which journey down is passenger {i} going on? "))

            if check_seats(time_up, up_times, up_status, up_tally, up_session) and check_seats(time_down, down_times, down_status, down_tally, down_session):
                break
            else:
                continue
        
        for i in range(0,4):
            if up_tally[i] == up_seats:
                up_status[i] = "Closed"
            if down_tally[i] == down_seats:
                down_status[i] = "Closed"

    # The reason there is a need for the up_session and down_session lists are because the tally is the running total; 
    # There will be multiple sessions each day hence it is inaccurate to find number of free tickets based on the tally 
    calc_revenue(up_session, up_revenue)
    calc_revenue(down_session, down_revenue)
    
    session_total_cost = sum(up_revenue) + sum(down_revenue)
    print(f"This session's total is ${session_total_cost}")

    up_session = [0, 0, 0, 0] 
    down_session = [0, 0, 0, 0]

# TASK 3
def task_3_display(times, tally, revenue):
    for i in range(0,4):
        print(f"{i+1}. {times[i]} - {tally[i]} passengers - ${revenue[i]} made")
        highest = max(tally)
        return highest

print("\nJourney Up")
up_highest = task_3_display(up_times, up_tally, up_revenue)
print("\nJourney Down")
down_highest = task_3_display(down_times, down_tally, down_revenue)

total_revenue = sum(up_revenue) + sum(down_revenue)
print(f"\nA total of ${total_revenue} has been made")
total_passengers = sum(up_tally) + sum(down_tally)
print(f"There are {total_passengers} passengers today")

# What if two journey have the same number of passenger tally, how do we determine the max?
highest_passenger = max(up_highest, down_highest)
if highest_passenger == max(up_tally):
    index = up_tally.index(highest_passenger)
    print(f"{up_times[index]} was the journey with most passengers")
elif highest_passenger == max(down_tally):
    index = up_tally.index(highest_passenger)
    print(f"{down_times[index]} was the journey with most passengers")
else:
    print(f"Two or more journeys had the same number of passengers")