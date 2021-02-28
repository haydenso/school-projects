cost = 25

# list-structure = [time, total seats, count, revenue, status]
# status default value is "open" and is update to "closed" when total_steats==count

journey_up_one = ["9:00", 480, 0, 0, "open"]
journey_up_two = ["11:00", 480, 0, 0, "open"]
journey_up_three = ["13:00", 480, 0, 0, "open"]
journey_up_four = ["15:00", 480, 0, 0, "open"]
journey_up = [journey_up_one, journey_up_two, journey_up_three, journey_up_four]

journey_down_one = ["10:00", 480, 0, 0, "open"]
journey_down_two = ["12:00", 480, 0, 0, "open"]
journey_down_three = ["14:00", 480, 0, 0, "open"]
journey_down_four = ["16:00", 640, 0, 0, "open"]
journey_down = [journey_down_one, journey_down_two, journey_down_three, journey_down_four]

# the reason they are $25 each journey up and down is because when we go up we might have enough people for a free ticket, however we might come down different times, hence 

# Start of the day
def task_1():

    print("\nJourneys Up")
    count = 1
    for journey in journey_up:
        print(f"{count}. {journey[0]} - {journey[1]} seats")
        count+=1

    print("\nJourneys Down")
    count = 1
    for journey in journey_down:
        print(f"{count}. {journey[0]} - {journey[1]} seats")
        count += 1

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

            journey_up[time_up+1][2] += 1
            journey_up[time_down+1][2] += 1

            if journey[1] == journey[2]:
                journey[4] = "Closed"
            



        # Testing if it is still open for 

    
    num_free_tickets = int(num) // 10
    num_tickets_to_buy = num - num_free_tickets


# End of the day
def task_3():
    total_revenue = 0
    total_passengers = 0
    highest_passenger = 0

    print("\nJourneys Up")
    count = 1
    for journey in journey_up:
        print(f"{count}. {journey[0]} - {journey[2]} seats - ${journey[3]} made")
        total_revenue += journey[3]
        total_passengers += journey[2]
        count+=1

    print("\nJourneys Down")
    count = 1
    for journey in journey_down:
        print(f"{count}. {journey[0]} - {journey[2]} seats - ${journey[3]} made")
        total_revenue += journey[3]
        count += 1

    print(f"A total of ${total_revenue} has been made")
    print(f"There are {total_passengers} today")
    print(f"This journey had the most {highest_passenger}")


task_1()

