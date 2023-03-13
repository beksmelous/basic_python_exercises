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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

cost_of_espresso = (MENU["espresso"]["cost"])
cost_of_latte = (MENU["latte"]["cost"])
cost_of_cappuccino = (MENU["cappuccino"]["cost"])


def resources_taken(drink_name, ordered_ingredients):
    for item in ordered_ingredients:
        resources[item] -= ordered_ingredients[item]
    print(f"Here is your {drink_name}. ☕")


def enough_resources(ingredients):
    """Return True when order can be made, False if ingredients are insufficient"""
    for item in resources:
        if resources[item] < ingredients[item]:
            print(f"Sorry. There is not enough {item}. ")
            return False
        return True


def coins_taken():
    """Returns the total calculated from the money inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


is_on = True
while is_on:
    choice = input("What would you like to drink? Choose 'espresso', 'latte' or 'cappuccino': ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}g")
        print(f"Money : ${profit}")
    else:
        drink = MENU[choice]
        if enough_resources(drink["ingredients"]):
            payment = coins_taken()
            if payment < drink["cost"]:
                print(f"You did not inserted the right amount of money. Here are your money back: ${payment}.")
            elif payment >= drink["cost"]:
                change = round(payment - drink["cost"], 2)
                profit = drink["cost"]
                print(f"Here is your change ${change}.")
                resources_taken(choice, drink["ingredients"])
