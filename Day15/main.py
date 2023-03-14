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

flag_coffee = True


def print_report(resources_left):
    water = resources_left["water"]
    milk = resources_left["milk"]
    coffee = resources_left["coffee"]
    money = resources_left["money"]
    return f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g \nMoney: {money}$"


def make_coffee(menu, choice, resource):
    global flag_coffee
    if choice in menu:
        coffee_ingredients = menu[choice]["ingredients"]
        coffee_cost = menu[choice]["cost"]
    elif choice == "off":
        flag_coffee = False
        return flag_coffee
    elif choice == "report":
        print(print_report(resource))
        return False
    for ingredient in coffee_ingredients:
        if resource[ingredient] < coffee_ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False

    return True


def order(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


def convert_money(quarter, dime, nickle, penny):
    total = 0.25 * quarter + 0.1 * dime + 0.05 * nickle + 0.01 * penny
    return total


report = resources
report["money"] = 0
water = report["water"]
milk = report["milk"]
coffee = report["coffee"]
money = report["money"]

def coffee_machine():
    global flag_coffee
    while  flag_coffee:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        flag_resources = make_coffee(MENU, user_choice, report)

        if flag_resources:
            print("Please insert coins.")
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickles = int(input("How many nickles? "))
            pennies = int(input("How many pennies? "))
            money_user = convert_money(quarters, dimes, nickles, pennies)
            if money_user >= MENU[user_choice]["cost"]:
                difference=round(money_user - MENU[user_choice]["cost"],2)
                print(f"Here is ${difference} in change.")
                report["money"] += MENU[user_choice]["cost"]
                order(user_choice, MENU[user_choice]["ingredients"])
            else:
                print("Sorry! Not enough money. Money refunded")


coffee_machine()