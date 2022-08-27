# Rock, paper, scissors

import random

def rpsGame():

    print("============================================")
    print("Rock paper scissors")
    print("============================================")

    keep_playing = True
    score = [0, 0, 0]

    print("Play rock, paper, scissors! Best out of 5")

    while keep_playing:
        rps1 = "a"
        while rps1 not in "rps" or len(rps1) > 1:
            rps1 = input("Player 1: [r]ock, [p]aper, [s]cissors? ")

        # rps2 = "a"
        # while rps2 not in "rps" or len(rps2) > 1:
        #     rps2 = input("Player2: rock, paper, scissors? ")

        rps2 = random.choice("rps")
        print(f"Computer played: {rps2}")

        if rps1 == "r":
            if rps2 == "s":
                print("Player 1 wins.")
                score[0] += 1
            elif rps2 == "p":
                print("Player 2 wins.")
                score[1] += 1
            else: 
                print("Draw.")
                score[2] += 1
        elif rps1 == "p":
            if rps2 == "r":
                print("Player 1 wins.")
                score[0] += 1
            elif rps2 == "s":
                print("Player 2 wins.")
                score[1] += 1
            else: 
                print("Draw.")
                score[2] += 1
        else: 
            if rps2 == "p":
                print("Player 1 wins.")
                score[0] += 1
            elif rps2 == "r":
                print("Player 2 wins.")
                score[1] += 1
            else: 
                print("Draw.")
                score[2] += 1

        print("Current score:" )
        print(f"P1: {score[0]}  CPU: {score[1]}  draws: {score[2]}")
        print("===================================================")

        if score[0] == 3 or score[1] == 3:
            if score[0] == 3:
                print("You win!")
            elif score[1] == 3:
                print("You lose!")

            another_round = input("Enter 'y' to play another round? ").lower()
            if another_round == "y":
                score = [0, 0, 0]
            else:
                break

        # cont = input("Press C to continue! ").lower()
        # if cont == "c": keep_playing = True
        # else: keep_playing = False

        # if keep_playing == False:
        #     break

    print("Thanks for playing!")
    