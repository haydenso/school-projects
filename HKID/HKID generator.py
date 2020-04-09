import random

while True:
    # randomly generating the first letter
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'X', 'Y', 'Z']
    hkid_prefix = random.choice(alpha)

    # randomly generating body number
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    num3 = random.randint(0, 9)
    num4 = random.randint(0, 9)
    num5 = random.randint(0, 9)
    num6 = random.randint(0, 9)

    # randomly generating bracket number
    hkid_bracket = random.randint(0, 9)

    # forming the HKID code as one string
    hkid = (f"{hkid_prefix}{num1}{num2}{num3}{num4}{num5}{num6}({hkid_bracket})")

    # testing to see if valid begins

    # first alphabet
    hkid_prefix = hkid[0]

    # body number
    hkid_number = hkid[1:7]

    # finding value in the brackets
    hkid = hkid.replace(")", "")
    hkid_bracket = hkid.split("(")
    hkid_bracket = hkid_bracket[1]

    # replacing the first alphabet to the numeric value
    a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'X', 'Y', 'Z']
    num = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192,
           200, 208]

    hkid_prefix = a.index(hkid_prefix)
    hkid_prefix = num[hkid_prefix]

    # changing the each digit in the hkid number with a multiplier
    num1 = int(hkid_number[0]) * 7
    num2 = int(hkid_number[1]) * 6
    num3 = int(hkid_number[2]) * 5
    num4 = int(hkid_number[3]) * 4
    num5 = int(hkid_number[4]) * 3
    num6 = int(hkid_number[5]) * 2
    total = num1 + num2 + num3 + num4 + num5 + num6

    # step 3 calculating remainder
    calc = int(hkid_prefix) + total
    calc = calc % 11

    # step 4
    check = 11 - calc

    # checking if valid and printing the results
    if int(check) - int(hkid_bracket) == 0:
        print(f"This HKID check digit is valid: {hkid}) ")
        break
