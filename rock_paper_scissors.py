# importing modules
import random
from unittest import result

# welcoming message
print("\n\n\n\t\tWelcome Player! To the Rock, Paper, Scissors Game\n\n\n")


# play or quit
choice = input("Do you want to Play?(y/n) ")

if choice.lower() != "y":
    choice_quit = ("Do you want to Quit?(y/n) ")
    if choice_quit.lower() == "y":
        quit()

# conditions


def condition(bot_option, player_option):
    if bot_option == player_option:
        return "Draw"
    elif bot_option == "rock" and player_option == "scissor":
        return "Lose"
    elif bot_option == "rock" and player_option == "paper":
        return "Win"
    elif bot_option == "paper" and player_option == "rock":
        return "Lose"
    elif bot_option == "paper" and player_option == "scissor":
        return "Win"
    elif bot_option == "scissor" and player_option == "rock":
        return "Win"
    elif bot_option == "scissor" and player_option == "paper":
        return "Lose"
    else:
        return "Invalid"


options = ["rock", "paper", "scissor"]
play = "y"
player_win_count = 0
bot_win_count = 0
draw_count = 0

while play == "y":
    # player option
    player_option = input("What do you choose? ")
    while player_option not in options:
        player_option = input("Please input valid option: ")

    # bot option
    bot_option = options[random.randint(0, 2)]

    # comparison
    result = condition(bot_option, player_option)

    if result == "Win":
        print("Player Won")
        player_win_count += 1
    elif result == "Lose":
        print("Bot Won")
        bot_win_count += 1
    elif result == "Draw":
        print("Draw")
        draw_count += 1
    elif result == "Invalid":
        print("Invalid Input")

    play = input("Do you want to play Again? (y/n) ")
    while play not in ["y", "n"]:
        play = input("Invalid Input. Please Try again (y/n): ")

print(
    f"Player Won {player_win_count} times and Bot Won {bot_win_count} times. And Draw count {draw_count}")
