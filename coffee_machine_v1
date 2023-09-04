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

#report (water/milk/coffee/money)

def report(drink_choice):

    if drink_choice == 'latte' or drink_choice == 'cappuccino':

        user_water = MENU[drink_choice]['ingredients']['water']
        user_milk = MENU[drink_choice]['ingredients']['milk']
        user_coffee = MENU[drink_choice]['ingredients']['coffee']

        machine_water = resources['water']
        machine_milk = resources['milk']
        machine_coffee = resources['coffee']

        #check resources sufficient
        if machine_water - user_water < 0 or machine_milk - user_milk < 0 or machine_coffee - user_coffee < 0:
            print("Sorry, there are not enough ingredients to make this drink.")
            drink_choice = input("What would you like instead? (espresso/latte/cappuccino) ")
            report(drink_choice)
        else:
            resources['water'] = machine_water - user_water
            resources['milk'] = machine_milk - user_milk
            resources['coffee'] = machine_coffee - user_coffee

    elif drink_choice == 'espresso':

        user_water = MENU[drink_choice]['ingredients']['water']
        user_coffee = MENU[drink_choice]['ingredients']['coffee']

        machine_water = resources['water']
        machine_coffee = resources['coffee']

        # check resources sufficient
        if machine_water - user_water < 0 or machine_coffee - user_coffee < 0:
            print("Sorry, there are not enough ingredients to make this drink.")
            drink_choice = input("What would you like instead? (espresso/latte/cappuccino) ")
            report(drink_choice)
        else:
            resources['water'] = machine_water - user_water
            resources['coffee'] = machine_coffee - user_coffee


q = 0.25
d = 0.1
n = 0.05
p = 0.01

money = 0
user_change = 0
drink_list = []
machine_on = True

while machine_on == True:

    # prompt user - espresso/latte/cappuccino
    drink_choice = input("What would you like? (espresso/latte/cappuccino) ")
    report(drink_choice)

    # turn off coffee machine (exit code)

    if drink_choice == 'off':
        machine_on = False

    if drink_choice == 'report' and machine_on == True:
        print(resources)

    elif machine_on == True:

    # process coins

        print("Please insert coins.")

        tot_quarters = float(input("how many quarters?: "))
        tot_dimes = float(input("how many dimes?: "))
        tot_nickels = float(input("how many nickels?: "))
        tot_pennies = float(input("how many pennies?: "))

        user_money = (tot_quarters * q) + (tot_dimes * d) + (tot_nickels * n) + (tot_pennies * p)

        # check if transaction was successful (q+d+n+p)

        if user_money < MENU[drink_choice]['cost']:
            print("Sorry that's not enough money. Money refunded.")
        else:
            user_change = round(user_money - MENU[drink_choice]['cost'], 2)
            print(f"Here is ${user_change} in change.")

            money += MENU[drink_choice]['cost']
            resources['money'] = money

            # make coffee
            print(f"Here is your {drink_choice}. Enjoy!")
            print(drink_list)

