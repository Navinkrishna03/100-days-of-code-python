alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(original_text,shift_amount,user_choice):
    output_text = ""
    if user_choice == "decrypt":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabets:
            output_text += letter
        else:
            index_of_alphabets_in_text = alphabets.index(letter) + shift_amount
            index_of_alphabets_in_text %= len(alphabets)
            output_text += alphabets[index_of_alphabets_in_text]
    print(f"Your {user_choice}ed text is {output_text}")



logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
flag = True
while flag:

    user_choice_1 = input("Type 'encrypt' or 'decrypt':").lower()
    original_text = input("Type your message:")
    shift_amount = int(input("Type the shift number:"))
    caeser(original_text=original_text, shift_amount=shift_amount, user_choice=user_choice_1)
    user_choice_2 = input("Type 'yes' to continue or 'no' to stop:").lower()
    if user_choice_2 == "no":
        print("Thanks for using, Have a good day!")
        flag = False
        break
