passengers = [480, 480, 480, 480, 480, 480, 480, 640]
money = [0, 0, 0, 0, 0, 0, 0, 0]
trains = [9, 11, 13, 15, 10, 12, 14, 16]

# Task 1
run = True
while run:
    n = 0
    print('Train No.', 'Time', 'No. seats', 'Revenue')
    for i in passengers:
        n += 1
        print(f'train {n}', f'{trains[n-1]}:00', i, money[passengers.index(i)])

# Task 2
    ppl = int(input("how many seats would you like to book?"))
    d_train = int(input('which train would you like to take at departure?(1, 2, 3, 4)'))
    while type(d_train) != int or passengers[d_train-1] < ppl or d_train > 4 or d_train < 1:
        d_train = input('This train is not available, please select another train:')
    d_train=int(d_train)
    r_train=int(input('which train would you like to take to return?(5, 6, 7, 8)'))
    while type(d_train) != int or passengers[r_train-1] < ppl or r_train < 5 or r_train > 8 or trains[d_train-1] > trains[r_train-1]:
        r_train=input('This train is not available, please select another train:')
    r_train=int(r_train)
    if ppl > 10 and ppl < 80:
        tickets=ppl-(ppl//10)
    else:
        tickets=ppl
    cost=tickets * 50
    print(f'total cost: ${cost}')
    money[d_train-1] += cost/2
    passengers[d_train-1] -= ppl
    money[r_train-1] += cost/2
    passengers[r_train-1] -= ppl
    end=input('If finished, press enter\n'
    'If you want to buy more tickets, press space then enter')
    if end == '':
        run=False
    if end == ' ':
        run=True
    elif end != '' and end != ' ':
        end=input(
            'If finished, press enter, but If you want to buy more tickets, press space then enter:')
    n=0
    print('Train No.', 'Time', 'No. seats', 'Revenue')
    for i in passengers:
        n += 1
        if i == 0:
            count = "Closed"
        else:
            count = i
        print(f'train {n}', f'{trains[n-1]}:00', count, money[passengers.index(i)])

# Task 3
total_revenue=0
most_passengers=640
for i in money:
    total_revenue += i
total_passengers=4000
big=0
for i in passengers:
    total_passengers -= i
    if passengers.index(i) != 7:
        number=480 - i
    else:
        number=640 - i
    if number > big:
        big=number
        most_passenger_train=trains[passengers.index(i)]
print(f'total revenue: {total_revenue} | total passengers: {total_passengers/2} | train with most passengers: The {most_passenger_train}:00 with {big} total passengers for the day')
