import random as rd
import Hangman_Ess as He
print(He.hangman_logo)
lives = 6
guessed = False
place_holder = ""
chosen_word = rd.choice(He.words)
#print(chosen_word)
for letter in range(len(chosen_word)):
    place_holder+='_'
print(place_holder)


correct_guess = []
guessed = False
while not guessed:

    display = ""
    guess = input("Guess a letter:").lower()
    if guess in correct_guess:
        print(f"You have already entered the letter '{guess}' ")

    for letter in chosen_word:
        if letter == guess :
            display+= letter
            correct_guess.append(guess)
        elif letter in correct_guess:
            display += letter
        else:
            display += "_"

    print(display)
    if guess not in chosen_word:
        lives -= 1
        print(f"You've guessed it wrong remaining lives {lives}")
        if lives == 0:
            guessed = True
            print(f"***********-- You Lose!, It was '{chosen_word}' --*************")

    print(He.hangman_stages[lives])
    if "_" not in display:
        guessed = True
        print("***********--You Win!--*************")






