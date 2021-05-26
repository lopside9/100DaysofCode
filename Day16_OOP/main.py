from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_start = True
profit = 0


while machine_start:
    choice = input(f"What would you like? {menu.get_items()}:\n")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        chosen_coffee = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(chosen_coffee):
            print(f"Your {chosen_coffee.name} will be ${chosen_coffee.cost:.2f}.")
            if money_machine.make_payment(chosen_coffee.cost):
                coffee_maker.make_coffee(chosen_coffee)
                print("True. End Program.")
        else:
            machine_start = False
