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
    "money":0
}

def show_resources():
    """Show all Resources"""
    for name in resources:
        print(f"{name.capitalize()}: {resources[name]}")

def check_resources(coffee):
    """Check if there's enough resources for the coffee order"""
    coffee_ingredients = MENU[coffee]['ingredients']
    insufficient = []
    for ingredient in coffee_ingredients:
        if coffee_ingredients[ingredient] > resources[ingredient]:
            insufficient.append(ingredient)

    return insufficient

def insert_coin():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * .25
    dimes = int(input("How many dimes?: ")) * .10
    nickle = int(input("How many nickle?: ")) * .05
    pennies = int(input("How many pennies?: ")) * .01

    return quarters + dimes + nickle + pennies

def make_coffee(coffee):
    coffee_ingredients = MENU[coffee]['ingredients']
    for ingredient in coffee_ingredients:
        resources[ingredient] = resources[ingredient] - coffee_ingredients[ingredient]

is_machine_on = True
while is_machine_on:
    user_input = input("What would you like? (espresso/latte/cappuccino):")

    if user_input == "off":
        print("GoodBye!")
        is_machine_on = False
    elif user_input == "report":
        show_resources()
    elif user_input in MENU:
        #Check if there's enough resources
        checked_resource = check_resources(user_input)
        if checked_resource:
            print(f"Sorry there is not enough {" ".join(checked_resource)}.")
            continue

        #Insert Coins prompt
        total_money = insert_coin()
        coffee_cost = MENU[user_input]['cost']

        #Check money
        if total_money == coffee_cost:
            print("exact")
        elif total_money > coffee_cost:
            print(f"Here's your change {total_money - coffee_cost}")
        else:
            print("Sorry that's not enough money. Money refunded.")
            continue

        resources["money"] += coffee_cost
        # deductions of the used resources
        make_coffee(user_input)
        # Hand over the coffee message
        print(f"Here's your {user_input} enjoy!")
    else:
        print("Please enter one of the following: (espresso/latte/cappuccino)")