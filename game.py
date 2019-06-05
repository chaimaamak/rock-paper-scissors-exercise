# game.py

import random


print("Rock, Paper, Scissors, Shoot!")

# CAPTURE INPUTS

user_choice = input("Please choose one of the following options: 'rock', 'paper', or 'scissors' (without the quotes):")

print("----------")
print("USER CHOICE", user_choice)  # Making sure the input is captured properly

# VALIDATE INPUTS

options = ["rock", "paper", "scissors"]

if user_choice not in options:
    print("INVALID SELECTION, PLEASE TRY AGAIN...")
    exit()

# GENERATE COMPUTER SELECTION

print("GENERATING...")

computer_choice = random.choice(options)

print("----------")
print("COMPUTER CHOICE", computer_choice)

# DETERMINE THE WINNER
#
# rock beats scissors
# paper beats rock
# scissors beats paper
# same selections is a tie
# number of possible outcomes is 9 including the ties 
#

if user_choice == computer_choice:
    print("IT'S A TIE! PLAY AGAIN!")
elif user_choice == "rock" and computer_choice == "paper":
    print("AND THE WINNER IS ... PAPER")
elif user_choice == "rock" and computer_choice == "scissors":
    print("AND THE WINNER IS ... ROCK")
elif user_choice == "paper" and computer_choice == "rock":
    print("AND THE WINNER IS ... PAPER")
elif user_choice == "paper" and computer_choice == "scissors":
    print("AND THE WINNER IS ... SCISSORS")
elif user_choice == "scissors" and computer_choice == "rock":
    print("AND THE WINNER IS ... ROCK")
elif user_choice == "scissors" and computer_choice == "paper":
    print("AND THE WINNER IS ... SCISSORS")



# DISPLAY FINAL OUTPUTS / OUTCOMES

