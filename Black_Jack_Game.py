import random as rd

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

playerHand = []
computerHand = []
Start = input("Play game? (y/n): ")
if Start == "y":
    for i in range(2):
        playerHand.append(rd.choice(cards))
        computerHand.append(rd.choice(cards))
print(f"Player's Card : {playerHand}\t player's score: {sum(playerHand)}")
print(f"Computer's Card : {computerHand[0]}")
GameOver = False
while not GameOver:
    User_Input = input("Pick another card ? (Y/N): ")
    if User_Input == "Y" or User_Input == "y":
        playerHand.append(rd.choice(cards))
        computerHand.append(rd.choice(cards))
        print(f"Computer's Card: {computerHand[0]}")
        print(f"Player's Card : {playerHand}\t player's score:{sum(playerHand)}")
    elif User_Input == "N" or User_Input == "n":
        if sum(playerHand) >= 21:
            print("You Lose!")
            print(f"Player's Card : {playerHand}\t player's score:{sum(playerHand)}")
            print(f"Computer's Card : {computerHand}\t Computer's score:{sum(computerHand)}")
            GameOver = True
        elif sum(computerHand) >= 21:
            print("You Win!")
            print(f"Player's Card : {playerHand}\t player's score:{sum(playerHand)}")
            print(f"Computer's Card : {computerHand}\t Computer's score:{sum(computerHand)}")
            GameOver = True


