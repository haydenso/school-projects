cost = 25           # Constant, integer

# list_structure = [time, total seats, count, revenue, status]
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