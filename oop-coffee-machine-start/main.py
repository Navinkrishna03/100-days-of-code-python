from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
bill_process = MoneyMachine()
menu = Menu()

machine_on = True
while machine_on:
    user_order = input(f"What would you like? ({menu.get_items()}) :")
    if user_order == "report":
        coffee.report()
        bill_process.report()
    elif user_order == "off":
        machine_on = False
    else:
        drink = menu.find_drink(user_order)
        if coffee.is_resource_sufficient(drink) and  bill_process.make_payment(drink.cost):
                coffee.make_coffee(drink)






