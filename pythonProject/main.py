# practice from Angelia course in Udemy

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
def is_resources_sufficient(order_ingredients):
    """
    Return True when order can be made, False if ingredients are insufficient
    :param order_ingredients:
    :return:
    """
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    """
    Returns the total calculated from coin inserted.
    :return: total amounts of coin inserted.
    """
    print("Please insert coins. ")
    total =  float(input("How many quarters?: ")) * 0.25
    total += float(input("How many diems?: ")) * 0.1
    total += float(input("How many nickles?: ")) * 0.05
    total += float(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False is money is insufficient."""
    if money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, there is not enough money. Money was refunded. ")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deducted the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")



is_on=True
while is_on:
    choice=input("What would you like ? (espresso/latte/cappuccino) :")
    if choice=='off':
        is_on=False
    elif choice=='report':
        print(f"Milk: {resources['water']}ml")
        print(f"Water: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink=MENU[choice]
        if is_resources_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice,drink['ingredients'])








