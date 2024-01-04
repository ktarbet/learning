from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cm = CoffeeMaker()
menu1 = Menu()
moneyMachine1 = MoneyMachine()

command=''
while command != 'off':
    command = input(f"What would you like? ({menu1.get_items()})")
    drink = menu1.find_drink(command)
    if command == 'off':
        exit(0)
    if command == 'report':
        cm.report()
        moneyMachine1.report()
    elif drink is not None:
        if cm.is_resource_sufficient(drink):
            if moneyMachine1.make_payment(drink.cost):
                cm.make_coffee(drink)
    else:
        print(f"unknown command '{command}'")
