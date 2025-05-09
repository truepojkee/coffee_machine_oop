from importlib.resources import is_resource

from menu import Menu, MenuItem
from art import logo
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()



print(logo)
coffee_machine_on = True
while coffee_machine_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")
    if choice == "off":
        print("Turning off in 3..2..1...")
        coffee_machine_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        find_drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(find_drink):
            if money_machine.make_payment(find_drink.cost):
                 coffee_maker.make_coffee(find_drink)













