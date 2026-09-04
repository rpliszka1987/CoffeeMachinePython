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
machine_running = True

while machine_running:
# TODO: Prompt user to choose what coffee they want
    user_coffee = input("What would you want? (espresso/latte/cappuccino): ").lower()

# TODO: Show machine supplies when typing in report
    if user_coffee == "report":
        print(f"Water: {resources['water']}ml \n Milk: {resources['milk']}ml \n Coffee: {resources['coffee']}g \n Money: ${machine_money}")
# TODO: Turn off machine by typing off
    elif user_coffee == "off":
        machine_running = False
    elif user_coffee == "espresso":
        print("Espresso")
    elif user_coffee == "latte":
        print("Latte")
    elif user_coffee == "cappuccino":
        print("Cappuccino")
    else:
        print("Please enter a valid option")



# TODO: Process coins inserted by user

# TODO: Check if tansaction successful and give user output

# TODO: Make Coffee