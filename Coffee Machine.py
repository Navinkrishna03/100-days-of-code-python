#Resources
water =  300
milk =  200
coffee =  100
profit = 0
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


#Menu

def print_report(current_water, current_milk, current_coffee, current_money):
    print(f"Water:{current_water}\n"
            f"Milk:{current_milk}\n"
            f"Coffee:{current_coffee}\n"
            f"Money:{current_money}\n")

def check_resources(current_water, current_milk, current_coffee, order):
    if order == "espresso":
        if current_water >= 50 and current_coffee >= 18:
            return True
        else:
            return False
    elif order == "latte":
        if current_water >= 200 and current_coffee >= 24 and current_milk >= 150:
            return True
        else:
            return False
    elif order == "cappuccino":
        if current_water >= 250 and current_coffee >= 24 and current_milk >= 100:
            return True
        else:
            return False
    else:
        return -1

def coin_process(quater_given,dimes_given,nickel_given,pennies_given):
    cal_quater_given = quater_given * 0.25
    cal_dimes_given = dimes_given * 0.1
    cal_nickel_given = nickel_given * 0.05
    cal_pennies_given = pennies_given * 0.01
    total_amount = cal_quater_given + cal_dimes_given + cal_nickel_given + cal_pennies_given
    return total_amount

def make_coffee(current_water, current_milk, current_coffee,order):
        if order == "espresso":
            current_water -= 50
            current_coffee -= 18
            return current_water,current_coffee,current_milk
        elif order == "latte":
            current_water -= 200
            current_coffee -= 24
            current_milk -= 150
            return current_water, current_coffee, current_milk
        elif order == "cappuccino":
            current_water -= 250
            current_coffee -= 24
            current_milk -= 100
            return current_water,current_coffee,current_milk
        else:
            return -1
def check_transaction(order,quater_given,dimes_given,nickel_given,pennies_given):
    if order == "espresso":
       if coin_process(quater_given=quarters,dimes_given=dimes,nickel_given=nickels,pennies_given=pennies) >= MENU["espresso"]["cost"] :
           return True
       else:
           return False
    elif order == "latte":
       if coin_process(quater_given=quarters,dimes_given=dimes,nickel_given=nickels,pennies_given=pennies) >= MENU["latte"]["cost"] :
           return True
       else:
           return False
    elif order == "cappuccino":
       if coin_process(quater_given=quarters,dimes_given=dimes,nickel_given=nickels,pennies_given=pennies) >= MENU["cappuccino"]["cost"] :
           return True
       else:
           return False
    else:
        return -1

machineOn = True
while machineOn:
    user_order = input("What would you like? (espresso/latte/cappuccino):")
    if user_order == "report":
        print_report(current_water=water, current_milk=milk, current_coffee=coffee, current_money=profit)
    else:
        if check_resources(current_water=water,current_milk=milk, current_coffee=coffee,order=user_order):
            print("Please insert coins")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            if check_transaction(user_order,quarters,dimes,nickels,pennies):
                profit += MENU[user_order]["cost"]
                water,coffee,milk = make_coffee(current_water=water,current_milk= milk,current_coffee= coffee,order= user_order)
                print("Thank you for your payment!")
                change =  coin_process(quarters,dimes,nickels,pennies) - MENU[user_order]["cost"]
                print(f"Here is your {user_order} Enjoy!")
                print(f"here is your change {round(change,2)}")
            else:
                print("Sorry, you do not have enough cash!")
                continue
        else:
            print("Insufficient resources")
            print_report(current_water=water, current_milk=milk, current_coffee=coffee, current_money=profit)
            machineOn = False