import random
logo = """ ██████╗ ██╗   ██╗███████╗███████╗███████╗    ████████╗██╗  ██╗███████╗
██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝    ╚══██╔══╝██║  ██║██╔════╝
██║  ███╗██║   ██║█████╗  ███████╗███████╗       ██║   ███████║█████╗  
██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║       ██║   ██╔══██║██╔══╝  
╚██████╔╝╚██████╔╝███████╗███████║███████║       ██║   ██║  ██║███████╗
 ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝       ╚═╝   ╚═╝  ╚═╝╚══════╝
                                                                       
███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗                  
████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗                 
██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝                 
██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗                 
██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║                 
╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝"""
def random_number():
    return random.randint(1,100)

Computers_Number = random_number()

def checkin_guess(guess, number_to_guess):
    if number_to_guess == guess:
        print("You guessed right!")
        return True   # ✅ return True when guessed correctly
    elif number_to_guess > guess:
        print("Too low!\nGuess Again!")
        return False
    elif number_to_guess < guess:
        print("Too high!\nGuess Again!")
        return False
    else:
        print("Enter Valid Input")
        return False


easy = 10
hard = 5
print(logo)
# print(Computers_Number) for debugging
Difficulty = input("choose a difficulty level, type 'easy' or 'hard': ")
if Difficulty == 'easy':
    level = easy
else:
    level = hard

while level:

    user_guess = int(input(f"You have {level} attempts remaining to guess the number.\n"
                      "Make a guess:"))

    if level == 0 :
        print("You've run out of guesses")
        break
    if checkin_guess(user_guess, Computers_Number):
        break
    level = level - 1






