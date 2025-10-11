from os import system

logo = r'''
  _______ _             _____ _ _            _                        _   _             
 |__   __| |           / ____(_) |          | |       /\             | | (_)            
    | |  | |__   ___  | (___  _| | ___ _ __ | |_     /  \  _   _  ___| |_ _  ___  _ __  
    | |  | '_ \ / _ \  \___ \| | |/ _ \ '_ \| __|   / /\ \| | | |/ __| __| |/ _ \| '_ \ 
    | |  | | | |  __/  ____) | | |  __/ | | | |_   / ____ \ |_| | (__| |_| | (_) | | | |
    |_|  |_| |_|\___| |_____/|_|_|\___|_| |_|\__| /_/    \_\__,_|\___|\__|_|\___/|_| |_|                                                                                        
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                       .-------------.
                      /_______________\
'''

print(logo)
bidders_dict = {}
yes = True

while yes:
    bidders = input("What is your name?")
    bid= input("Enter your bid")
    bidders_dict.update({bidders:bid})
    YesOrNo = input("Would you like to play again? Type 'yes' or 'no'")
    if YesOrNo == "no":
        Winner = max(bidders_dict, key=bidders_dict.get)
        print(f"The winner is {Winner}")
        yes = False
    elif YesOrNo == "yes":
        print("\n" * 20)
    else:
        print("You have entered wrong input. Please try again.")



