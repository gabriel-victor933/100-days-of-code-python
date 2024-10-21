from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
maker = CoffeeMaker()
money = MoneyMachine()

while True:
    order = input(f"“What would you like? ({menu.get_items()}) ")

    if order == 'report':
        maker.report()
        money.report()
        continue

    if order == 'off':
        break

    item = menu.find_drink(order)

    if item is None:
        continue
    
    if maker.is_resource_sufficient(item):

        if not money.make_payment(item.cost):
            continue

        maker.make_coffee(item)
    
    print('\n')
