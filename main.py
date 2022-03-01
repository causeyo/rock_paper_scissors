import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Type rock/paper/scissors or q to quit: ").lower()
    if user_choice == "q":
        break

    if user_choice not in options:
        print("Wrong choice, try again!")
        continue
    random_number = random.randint(0, 2)
    computer_choice = options[random_number]
    print("Computer choice: {}".format(computer_choice))

    if user_choice == "rock" and computer_choice == "scissors":
        print('you won!')
        user_wins += 1
    elif user_choice == "paper" and computer_choice == "rock":
        print('you won!')
        user_wins += 1
    elif user_choice == "scissors" and computer_choice == "paper":
        print('you won!')
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1

print("You won for the {} time".format(user_wins))
print("Computer won for the {} time".format(computer_wins))
print("See you next time!")
