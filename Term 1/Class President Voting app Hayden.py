import matplotlib.pyplot as plt


count = 0  # number of voters (30 maximum)
num_votes = []  # all votes stored
candidates = []
num1 = 0  # number of votes candidate 1 gets
num2 = 0  # vote count for candidate 2
num3 = 0
num4 = 0

print("\nWelcome to the Class Presidential Voting App")

while True:
    try:
        num = int(input("\nHow many candidates are there (2 or 3 or 4 candidates): "))
        if 2 <= num <= 4:
            break
        else:
            raise ValueError
    except ValueError:
        continue

if num == 2:
    cand1 = input("\nEnter first candidate name: ")
    cand2 = input("Enter second candidate name: ")

    print("\nCandidates:")
    print(f"1. {cand1}")
    print(f"2. {cand2}\n")

    num_votes.extend([num1, num2])  # used 'extend' as multiple variables are appended
    candidates.extend([cand1, cand2])

elif num == 3:
    cand1 = input("\nEnter first candidate name: ")
    cand2 = input("Enter second candidate name: ")
    cand3 = input("Enter third candidate name: ")

    print("\nCandidates:")
    print(f"1. {cand1}")
    print(f"2. {cand2}")
    print(f"3. {cand3}\n")

    num_votes.extend([num1, num2, num3])
    candidates.extend([cand1, cand2, cand3])

elif num == 4:
    cand1 = input("\nEnter first candidate name: ")
    cand2 = input("Enter second candidate name: ")
    cand3 = input("Enter third candidate name: ")
    cand4 = input("Enter fourth candidate name: ")

    print("\nCandidates:")
    print(f"1. {cand1}")
    print(f"2. {cand2}")
    print(f"3. {cand3}")
    print(f"4. {cand4}\n")

    num_votes.extend([num1, num2, num3, num4])
    candidates.extend([cand1, cand2, cand3, cand4])

while count < 30:  # to test, change this to a smaller number
    try:
        vote = int(input("Which candidate number would you like to vote: "))
        count += 1
        if vote == 1:
            num_votes[0] += 1
            continue
        elif vote == 2:
            num_votes[1] += 1
            continue
        elif vote == 3:
            num_votes[2] += 1
            continue
        elif vote == 4:
            num_votes[3] += 1
            continue
        else:
            raise IndexError
    except IndexError:
        print("Invalid candidate option")
        count = count - 1  # minus the vote
        continue
    except ValueError:
        print("Invalid candidate option")
        count = count - 1
        continue

print("\nAll 30 votes have been collected")

num_votes, candidates = zip(*sorted(zip(num_votes, candidates))) # https://stackoverflow.com/questions/9764298/is-it-possible-to-sort-two-listswhich-reference-each-other-in-the-exact-same-w
candidates = list(candidates)  # converted to list from tuple
num_votes = list(num_votes)

candidates.reverse()                    # reverse for descending order
num_votes.reverse()

print("\nThe results are...")

if num_votes[0] == num_votes[1]:  # if the numbers match, there means there is no winner
    print("NO OVERALL WINNER, there is a tie!")
    print("\nResults (no winner): ")
    try:
        print(f"{candidates[0]} with {num_votes[0]} votes")
        print(f"{candidates[1]} with {num_votes[1]} votes")
        print(f"{candidates[2]} with {num_votes[2]} votes")
        print(f"{candidates[3]} with {num_votes[3]} votes")
    except:
        pass
else:
    highest = max(num_votes)  # finds highest voters
    pos = num_votes.index(highest)  # find position of highest value
    print(f"THE WINNER IS {candidates[pos]} WITH {highest} VOTES")
    print("\nRanking:")
    try:
        print(f"1. {candidates[0]} with {num_votes[0]} votes - NEW CLASS PRESIDENT")
        print(f"2. {candidates[1]} with {num_votes[1]} votes")
        print(f"3. {candidates[2]} with {num_votes[2]} votes")
        print(f"4. {candidates[3]} with {num_votes[3]} votes")
    except IndexError:
        pass                  # ignore lines where the variable is not defined or the code does not exist

fig1, ax1 = plt.subplots()            # minor error is that if the value is zero (0.00%), the graphing is weird
ax1.pie(num_votes, labels=candidates, autopct='%1.2f%%',
        shadow=True, startangle=90)     # 'autopct' is decimal figs.
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()          # shows the graph




