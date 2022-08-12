from coffee import MENU

inmachine = {
"water":3000,
"milk": 1000,
"coffee":1000,
"coin" = 0,
}


# "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,


def check_ing(choice):
    w = choice["ingredients"]["water"]
    c = choice["ingredients"]["coffee"]
    m = choice["ingredients"]["milk"]
    global water
    global milk
    global coffee
    if w <= water and m <= milk and c <= coffee:
        water -= w
        coffee -= c
        milk -= m
        return True
    elif w > water:
        print("no water")
        return False
    elif m > milk:
        print("no milk")
        return False
    else:
        print('no coffee')
        return False


def money_in():
    q = int(input("How many quarters?" ))
    d = int(input("How many dimes? "))
    n = int(input("How many nickels? "))
    p = int(input("How many pennies? "))
    money_sum = round(q*0.25 + d*0.1 + n*0.05 + p*0.01 , 2)
    return money_sum


def check_money(choice,m):
    price = choice["cost"]
    if m >= price:
        change = round(m - price, 2)
        print(f"here's your change ${change}")
        return True
    else:
        refund = m
        print(f"sorry, not enough money, money refund ${refund}")
        return False

running = True
while running == True:
    ans = input("What would you like?(espresso/latte/cappuccino): ").lower()
    if ans == "report":
        print(f"Water: {water}")
        print(f"Coffee: {coffee}")
        print(f"Milk: {milk}")
    elif ans == "espresso" or ans == "latte" or ans == "cappuccino":
        print("please insert coins.")
        choice = MENU[ans]
        m = money_in()
        if check_ing(choice) and check_money(choice,m):
            print(f"here's your {ans}")
        else:
            running = False
    else:
        running = False
        print("bye")











