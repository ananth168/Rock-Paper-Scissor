import random
while True:
    choices = ["rock", "paper", "scissor"]
    player = None
    computer = random.choice(choices)

    while player not in choices:
        player = input("rock, paper, scissor?: ").lower()
        print("computer: ", computer)
        print("player: ", player)

    if player == computer:
        print("Tie")

    elif player == "rock":
        if computer == "paper":
            print("you lose !")
        elif computer == "scissor":
            print("you won!!")

    elif player == "paper":
        if computer == "rock":
            print("you won!!")
        elif computer == "scissor":
            print("you lose!")

        elif player == "scissor":
            if computer == "paper":
                print("you won!!")
            elif computer == "rock":
                print("you lose!")
    

    Play_again = input("wanna play again ? (yes/no): ").lower()

    if Play_again != "yes":
        break
print("Byeee ;)")

        