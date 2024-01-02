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


command = ""
money = 0

def recipie(command):
    return MENU[command]["ingredients"]

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

def enough_resources(command):
    ingredients = recipie(command)
    for item in ingredients:
        need = ingredients[item]
        have = resources[item]
        if need > have :
            print(f"Sorry there is not enough {item}")
            return False

    return True


def subtract_resources(command):
    ingredients = recipie(command)
    for item in ingredients:
        need = ingredients[item]
        have = resources[item]
        have -= need
        resources[item] = have


def make_drink(command):
    subtract_resources(command)
    print(f"Here is your {command}. Enjoy")


def process_coins(command):
    global money
    cost = MENU[command]['cost']
    print(f"Please insert coins. Cost is {cost}")
    q = int(input("how many quarters?:"))
    d = int(input("how many dimes?:"))
    n = int(input("how many nickles?:"))
    p = int(input("how many pennies?:"))

    coin_total = q*.25 + d*.1 + n*.05 + p*.01
    print(f"Total = {coin_total}")
    if coin_total >= cost:
        if coin_total > cost:
            print(f"returning {round(coin_total - cost,2)} in change")
        money += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


while command != 'off':
    command = input("What would you like? (espresso/latte/cappuccino)")
    if command == 'off':
        exit(0)
    if command == 'report':
        print_report()
    elif command in MENU:
        if enough_resources(command):
            if process_coins(command):
                make_drink(command)
    else:
        print(f"unknown command '{command}'")

