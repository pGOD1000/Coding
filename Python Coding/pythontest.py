import random

def options():
    player_choice = input("Pick one: rock, paper, scissors:")
    comuter_choice = options_to_choose.random(choice)
    options_to_choose = ["rock, paper, scissors"]
    return "You played {player_choice} and computer played {computer_choice}"

def check_win(player, computer):
    if (player == computer):
        return "It's a tie"
    elif (player == paper and computer == scissors):
        return "Scissors cuts paper, You lost"

start = options()
print(start)