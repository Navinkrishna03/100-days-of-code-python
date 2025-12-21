from game_data import data
import random
#Display Art



score = 0

def format_data(account):

    # Format the account data into printable format
    acc_name = account['name']
    acc_description = account['description']
    acc_country = account['country']
    return f"{acc_name}, a {acc_description}, from {acc_country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        if guess == 'a':
            return True
        else:
            return False
    elif b_followers > a_followers:
        if guess == 'b':
            return True
        else:
            return False
acc_a = random.choice(data)

# make the game repeatable
game_should_continue = True

while game_should_continue:

    #Generate a random account from the game data
    acc_b = random.choice(data)
    next_round_b = acc_b
    if acc_a == acc_b:
        acc_b = random.choice(data)

    print(f"Compare A: {format_data(acc_a)}.")
    print(f"Compare B: {format_data(acc_b)}.")

    # Ask user for a guess.

    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    #clear the screen
    print("\n"*20)


    # - get the follower count of each account
    a_follower_count = acc_a['follower_count']
    b_follower_count = acc_b['follower_count']

    # check if user is correct
    # - use if statement to check if user is correct.
    is_correct = check_answer(user_guess, a_follower_count, b_follower_count)

    #Give user feedback on their guess
    #score keeping
    if is_correct:
        score += 1
        print(f"you are right! Your Current score is {score}.")
        # making account at position B become the next account at position A
        acc_a = next_round_b
    else:
        print(f"Sorry you are wrong, Your Final Score:{score}")
        game_should_continue = False



