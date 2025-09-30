import random as rd

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
random_choice = [rock, paper, scissor]
computer_choice = rd.randint(0, 2)
user_choice = int(input("Type 0 for rock, 1 for paper, 2 for scissor: "))
print(f"You have chosen{random_choice[user_choice]}")
print(f"The computer have chosen{random_choice[computer_choice]}")
flag = False
if computer_choice == user_choice:
    flag = True
    print('Its a Tie, Try Again')
elif computer_choice == 0 and user_choice == 2:
    flag = True
    print("You Lose")
elif computer_choice == 1 and user_choice == 0:
    flag = True
    print("You Lose")

elif computer_choice == 2 and user_choice == 1:
    flag = True
    print("You Lose")

elif flag == False:
    print("You Have Won !!!")
else:
    print("Enter Valid Number")