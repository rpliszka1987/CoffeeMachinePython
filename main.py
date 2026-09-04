# Coffee Machine Project

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

machine_money = 0.00

# TODO: Prompt user to choose what coffee they want
user_coffee = input("What would you want? (esspresso/latte/cappuccino): ").lower()

# TODO: Turn off machine by typing off

# TODO: Show machine supplies when typing in report
if user_coffee == "report":
    print(f"Water: {resources['water']}ml \n Milk: {resources['milk']}ml \n Coffee: {resources['coffee']}g \n Money: ${machine_money}")


# TODO: Process coins inserted by user

# TODO: Check if tansaction successful and give user output

# TODO: Make Coffee