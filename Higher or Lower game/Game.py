from random import randint

from Procedural_Approach_Hangman import guess
from game_data import data
MAXIMUM_ELEMENTS = len(data)

#Getting Random Personalities

first = data[randint(0,MAXIMUM_ELEMENTS)]
second = data[randint(0,MAXIMUM_ELEMENTS)]


#Assigning the followers count to variables A and B

player_a = first['follower_count']
player_b = second['follower_count']

def higher_or_lower(a, b, guess):
    if guess == player_a:
        return True
    elif guess == player_b:
        return True
    else:
        return False

game_continues = True
while game_continues:
    user_input = str(input(f"Choose A: {first['name']} or B: {second['name']} "))

    if user_input == 'A':
        guess = player_a
    elif user_input == 'B':
        guess = player_b
    elif user_input == '':
        game_continues = False

    if higher_or_lower(a=player_a, b=player_b, guess=guess):
        player_a = player_b
        print("You move to next round")
        player_b = data[randint(0,MAXIMUM_ELEMENTS)]

    else:
        game_continues = False
