cost = 25

# list-structure = [time, total seats, count, revenue, status]
# status default value is "open" and is update to "closed" when total_steats==count

journey_up_one = ["9:00", 480, 0, 0, "open"]
journey_up_two = ["11:00", 480, 0, 0, "open"]
journey_up_three = ["13:00", 480, 0, 0, "open"]
journey_up_four = ["15:00", 480, 0, 0, "open"]
journey_up = [journey_up_one, journey_up_two, journey_up_three, journey_up_four]

time_up = 1

journey_up[time_up-1][2] += 1

print(journey_up[time_up-1][2])
print(journey_up_one)