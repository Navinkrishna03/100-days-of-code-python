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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#Menu

def print_report():
    print(f"Water: {resources["water"]}\n"
            f"Milk:{resources["milk"]}\n"
            f"Coffee:{resources["coffee"]}\n"
            f"Money:{profit}\n")

def check_resources(order):
    for item in order["ingredients"]:
        if order["ingredients"][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def coin_process(quater_given,dimes_given,nickel_given,pennies_given):
    cal_quater_given = quater_given * 0.25
    cal_dimes_given = dimes_given * 0.1
    cal_nickel_given = nickel_given * 0.05
    cal_pennies_given = pennies_given * 0.01
    total_amount = cal_quater_given + cal_dimes_given + cal_nickel_given + cal_pennies_given
    return total_amount

def make_coffee(order):
        for item in MENU[order]["ingredients"]:
            resources[item] -= MENU[order]["ingredients"][item]
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
        print_report()
    elif user_order == "off":
        machineOn = False
    else:
        drink = MENU[user_order]
        if check_resources(order=drink):
            print("Please insert coins")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            if check_transaction(user_order,quarters,dimes,nickels,pennies):
                profit += MENU[user_order]["cost"]
                make_coffee(order= user_order)
                print("Thank you for your payment!")
                change =  coin_process(quarters,dimes,nickels,pennies) - MENU[user_order]["cost"]
                print(f"Here is your {user_order} Enjoy!")
                print(f"here is your change {round(change,2)}")
            else:
                print("Sorry that's not enough money. Money refunded.")
                continue
