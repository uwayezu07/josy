
import random
import time

def option_value(num):
    # print("hello")
    player_input = num
    if player_input == 1:
        return "rock"
        # print("you are a rock")
    elif player_input == 2:
        return "scissor"
        # print("you are a scissor")
    elif player_input == 3:
        return "paper"
        # print("you are a paper")
    # else:
    #     print("you entered the wrong option")

def player_result(machine_option, player_option):

    if machine_option == "rock" and player_option == "scissor":
        return "lose"
    elif machine_option == "rock" and player_option == "paper":
        return "win"

    elif machine_option == "scissor" and player_option == "rock":
        return "win"
    elif machine_option == "scissor" and player_option == "paper":
        return "lose"

    elif machine_option == "paper" and player_option == "scissor":
        return "win"
    elif machine_option == "paper" and player_option == "rock":
        return "lose"
    else:
        return "It's a match"

if __name__ == '__main__':

    random.seed(time.time())

    machine_option = option_value(random.randint(1,3))

    print("Enter a 1 if you want to be a rock, a 2 if you want to be a scissor or a 3 if you want to be a paper:")
    player_option = option_value(int(input()))

    print("Machine is equal to " + machine_option)
    print("Player is equal to " + player_option)

    print(player_result(machine_option, player_option))
