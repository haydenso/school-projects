ticket_cost = 25

# status default value is "open" and is update to "closed" when total_steats==count
journey_up_times = ["9:00", "11:00", "13:00", "15:00"]
journey_up_seats = [480, 480, 480, 480]
journey_up_count = [0, 0, 0, 0]
journey_up_revenue = [0, 0, 0, 0]
journey_up_status = ["open", "open", "open", "open"]

journey_down_times = ["10:00", "12:00", "14:00", "16:00"]
journey_down_seats = [480, 480, 480, 640]
journey_down_count = [0, 0, 0, 0]
journey_down_revenue = [0, 0, 0, 0]
journey_down_status = ["open", "open", "open", "open"]

# the reason they are $25 each journey up and down is because when we go up we might have enough people for a free ticket, however we might come down different times, hence 
# Start of the day
def task_1():

    print("\nJourneys Up")
    for i in range(0,4):
        print(f"{i+1}. {journey_up_times[i]} - {journey_up_seats[i]} seats")
    
    print("\nJourneys Down")
    for i in range(0,4):
        print(f"{i+1}. {journey_down_times[i]} - {journey_down_seats[i]} seats")

# Purchasing tickets
def task_2():
    while True:
        num = int(input("Number of students going:"))
        if 1 <= num <= 80:
            break
        else:
            print("Invalid number of tickets (Must be between 1 and 80 inclusive)")
    
    while True:
        for i in range (1,num+1):
            # Ask for the journey number as listed from task 1 (e.g input 1 is 9:00)
            time_up = input(f"Which journey down is passenger {i} going on?")
            time_down = input(f"Which journey down is passenger {i} going on?")

            while journey_up_status[time_up-1] != "Closed":
                journey_up_count[time_up-1] += 1
                journey_up_revenue[time_up+1] += ticket_cost
                break
            while journey_down_status[time_down-1] != "Closed":
                journey_down_count[time_down-1] += 1
                journey_down_revenue[time_down+1] += ticket_cost
                break

            for i in range(0,4):
                if journey_up_count[i] == journey_up_seats:
                    journey_up_status[i] = "Closed"
                if journey_down_count[i] == journey_down_seats:
                    journey_down_status[i] = "Closed"

    # Testing if it is still open for 

    num_free_tickets = int(num) // 10
    num_tickets_to_buy = num - num_free_tickets
    total_cost = num_tickets_to_buy * ticket_cost
    print(f"This session's total is ${total_cost}")

# End of the day
def task_3():
    print("\nJourneys Up")
    for i in range(1,5):
        print(f"{i}. {journey_up_times[i-1]} - {journey_up_count[i-1]} passengers - ${journey_up_revenue[i-1]} made")
    
    print("\nJourneys Down")
    for i in range(1,5):
        print(f"{i}. {journey_down_times[i-1]} - {journey_down_count[i-1]} passengers - ${journey_down_revenue[i-1]} made")

    total_revenue = sum(journey_up_revenue) + sum(journey_down_revenue)
    total_passengers = sum(journey_up_count) + sum(journey_down_count)
    # Two lists are combined
    highest_passenger_up = max(journey_up_count)
    highest_passenger_down = max(journey_down_count)

    if highest_passenger_up > highest_passenger_down:
        highest_passenger = highest_passenger_up
    elif highest_passenger_up < highest_passenger_down:
        highest_passenger = highest_passenger_down
    else:
        highest_passenger = [highest_passenger_up, highest_passenger_down]

    print(f"\nA total of ${total_revenue} has been made")
    print(f"There are {total_passengers} passengers today")
    print(f"This journey had the most {highest_passenger}")

task_1()
task_3()

# What if two journey have the same number of passenger count?