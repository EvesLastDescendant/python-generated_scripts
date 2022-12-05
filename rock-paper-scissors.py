rock = '''
    _________
---'    _____)
        (_____)
        (_____)
        (____)
---.____(____)
'''

paper = '''
    _______
---'   ____)____
        ______)
        _______)
        _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
        ______)
    __________)
    (____)
---.(___)
'''

#Write your code below this line 👇
import random
rock == 0
paper == 1
scissors == 2


choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_choice = random.randint(0, 2)

if choice and computer_choice == 0:
    print(f"you choose rock {rock}")
    print(f"computer choose rock {rock}")
    print("It's a draw")
if choice == 0 and computer_choice == 1:
    print(f"you choose rock {rock}")
    print(f"computer choose paper {paper}")
    print("you lost")
if choice == 0 and computer_choice == 2:
    print(f"you choose rock {rock}")
    print(f"computer choose scissors {scissors}")
    print("you won")
if choice == 1 and computer_choice == 1:
    print(f"you choose paper {paper}")
    print(f"computer choose paper {paper}")
    print("It's a draw")
if choice == 1 and computer_choice == 0:
    print(f"you choose paper {paper}")
    print(f"computer choose rock {rock}")
    print("You won")
if choice == 1 and computer_choice == 2:
    print(f"you choose paper {paper}")
    print(f"computer choose scissors {scissors}")
    print("You Lost")
if choice == 2 and computer_choice == 2:
    print(f"you choose scissors {scissors}")
    print(f"computer choose scissors {scissors}")
    print("It's a draw")
if choice == 2 and computer_choice == 0:
    print(f"you choose scissors {scissors}")
    print(f"computer choose rock {rock}")
    print("You Lost")
if choice == 2 and computer_choice == 1:
    print(f"you choose scissors {scissors}")
    print(f"computer choose paper {paper}")
    print("You Won")