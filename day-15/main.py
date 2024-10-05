MENU = { 
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "costs": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "costs": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "costs": 3.0,
    }
}

resources = {
    "water": 300,
    "coffee": 100,
    "milk": 200,
    "money": 0,
}

def check_resources(drink_type):
    recipe =  MENU.get(drink_type).get('ingredients')

    for key in recipe:
        if recipe.get(key) > resources.get(key):
            print(f"​Sorry there is not enough {key}.\n")
            return False

    return True

def process_coins():
    quarters = int(input("Enter the number of Quarters: "))
    dimes = int(input("Enter the number of Dimes: "))
    nickles  = int(input("Enter the number of Nickles: "))
    pennies = int(input("Enter the number of Pennies: "))

    return 0.25*quarters + 0.1*dimes + 0.05*nickles + 0.01*pennies

def process_transaction(value_insert, instruction):
    product_costs = MENU.get(instruction).get('costs')

    if product_costs > value_insert:
        print('​Sorry that\'s not enough money. Money refunded.\n')
        return False

    exchange = value_insert - product_costs

    print("Here is ${:.2f} dollars in change.".format(exchange))

    resources.update({"money": resources.get("money") + product_costs})

    return True

def make_product(instruction):
    ingredients = MENU.get(instruction).get("ingredients")
    for key in ingredients: 
        resources.update({key: resources.get(key) - ingredients.get(key)})

    print(f"Here is your {instruction}. Enjoy!\n")

def main():
    while(True):
        instruction = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if instruction == 'off': 
            print('Turning off!')
            break
        elif instruction == 'report':
            print(f"""
                Water: {resources.get('water')}ml
                Milk: {resources.get('milk')}ml
                Coffe: {resources.get('coffee')}g
                Money: ${resources.get('money')}
            """)
        elif instruction == 'espresso' or instruction == 'latte' or instruction == 'cappuccino':
            if not check_resources(instruction):
                continue
            value_insert = process_coins()
            if not process_transaction(value_insert,instruction):
                continue
            make_product(instruction)
        else: 
            print('Wrong Command! Try again!\n')

main()