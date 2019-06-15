# game.py

import random

def my_message():
    return "HELLO"

def determine_winner(u,c):
    winners = {
        "rock":{
            "rock": None,
            "paper": "paper",
            "scissors": "rock",
        },
        "paper":{
            "rock": "paper",
            "paper": None,
            "scissors": "scissors",
        },
        "scissors":{
            "rock": "rock",
            "paper": "scissors",
            "scissors": None,
        },
    }
    winning_choice = winners[u][c]
    return winning_choice


if __name__ == "__main__":  # only if this script is executed from the command-line

    print("Rock, Paper, Scissors, Shoot!")

    # CAPTURE INPUTS

    user_choice = input("Please choose one of the following options: 'rock', 'paper', or 'scissors' (without the quotes):")

    print("----------")
    print("USER CHOICE", user_choice)  # making sure the input is captured properly

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

    #if user_choice == computer_choice:
    #    print("IT'S A TIE! PLAY AGAIN!")
    #elif user_choice == "rock" and computer_choice == "paper":
    #    print("AND THE WINNER IS ... PAPER")
    #    print("YOU LOSE!")
    #elif user_choice == "rock" and computer_choice == "scissors":
    #    print("AND THE WINNER IS ... ROCK")
    #    print("YOU WIN!")
    #elif user_choice == "paper" and computer_choice == "rock":
    #    print("AND THE WINNER IS ... PAPER")
    #    print("YOU WIN!")
    #elif user_choice == "paper" and computer_choice == "scissors":
    #    print("AND THE WINNER IS ... SCISSORS")
    #    print("YOU LOSE!")
    #elif user_choice == "scissors" and computer_choice == "rock":
    #    print("AND THE WINNER IS ... ROCK")
    #    print("YOU LOSE!")
    #elif user_choice == "scissors" and computer_choice == "paper":
    #print("AND THE WINNER IS ... SCISSORS")
    #print("YOU WIN!")


    winning_choice = determine_winner(user_choice, computer_choice)

    # DISPLAY FINAL OUTPUTS / OUTCOMES

    if winning_choice:
        if winning_choice == user_choice:
            print("YOU WON")
        elif winning_choice == computer_choice:
            print("YOU LOST")
    else:
            print("TIE")

    print("Thanks for playing. Please play again!")



    