import consts

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "balance": 0
}


def turn_off():
    quit()


def print_report():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Balance: ${resources["balance"]}')


def hasEnoughResources(drink):
    recipe = consts.RECIPES[drink]["ingredients"]
    for k in recipe:
        if resources[k] < recipe[k]:
            return k
    return None


def hasResources(drink):
    resource = hasEnoughResources(drink)
    if resource is not None:
        print(f"Sorry there is not enough {resource}.")
        return False
    return True


def hasEnoughBalance(drink, credit):
    return credit >= consts.RECIPES[drink]["cost"]


def updateResources(drink):
    recipe = consts.RECIPES[drink]["ingredients"]
    for k in recipe:
        resources[k] -= recipe[k]


def updateBalance(drink):
    resources["balance"] += consts.RECIPES[drink]["cost"]


def offerChange(drink, credit):
    if credit > consts.RECIPES[drink]["cost"]:
        print(f'Here is ${round(credit - consts.RECIPES[drink]["cost"], 2)} dollars in change.')


def chargeUser(drink):
    print("Please insert coints.")

    p = int(input("Pennies: "))
    n = int(input("Nickles: "))
    d = int(input("Dimes: "))
    q = int(input("Quarters: "))

    return round(0.25 * q + 0.10 * d + 0.05 * n + 0.01 * p, 2)


def process_order(drink):
    if not hasResources(drink):
        return

    credit = chargeUser(drink)
    if not hasEnoughBalance(drink, credit):
        print("Sorry that's not enough money. Money refunded.")
        return

    updateResources(drink)
    updateBalance(drink)

    print(f"Here is your {drink}. Enjoy!")
    offerChange(drink, credit)


def main():
    while True:
        o = input("​What would you like? (espresso/latte/cappuccino): ").lower()
        if o == "off":
            turn_off()
        elif o == "report":
            print_report()
        elif o == "espresso" or o == "latte" or o == "cappuccino":
            process_order(o)


if __name__ == "__main__":
    main()
