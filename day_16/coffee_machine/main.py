from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    menu = Menu()
    menu_items = menu.get_items()

    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    while True:
        o = input(f"​What would you like? ({menu_items}): ")
        if o == "off":
            break
        elif o == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(o)
            if drink is None:
                continue
            if not coffee_maker.is_resource_sufficient(drink):
                continue
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


if __name__ == "__main__":
    main()
