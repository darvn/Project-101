import random

response = "y"

while response == "y":
    no = random.randint(1,6)
    if no == 1:
        print(" ___________")
        print("|           |")
        print("|           |")
        print("|     O     |")
        print("|           |")
        print("|___________|")
        response = input("y for continue, n to stop  ")
    elif no == 2:
        print(" ___________")
        print("|           |")
        print("|     O     |")
        print("|           |")
        print("|     O     |")
        print("|___________|")
        response = input("y for continue, n to stop  ")
    elif no == 3:
        print(" ___________")
        print("|           |")
        print("|     O     |")
        print("|     O     |")
        print("|     O     |")
        print("|___________|")
        response = input("y for continue, n to stop  ")
    elif no == 4:
        print(" ___________")
        print("|           |")
        print("|   O   O   |")
        print("|           |")
        print("|   O   O   |")
        print("|___________|")
        response = input("y for continue, n to stop  ")
    elif no == 5:
        print(" ___________")
        print("|           |")
        print("|   O   O   |")
        print("|     O     |")
        print("|   O   O   |")
        print("|___________|")
        response = input("y for continue, n to stop  ")
    elif no == 6:
        print(" ___________")
        print("|           |")
        print("|   O   O   |")
        print("|   O   O   |")
        print("|   O   O   |")
        print("|___________|")
        response = input("y for continue, n to stop  ")
    
