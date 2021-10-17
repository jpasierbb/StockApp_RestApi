from stock_checking import stockData
from stock_action import stockDo
from stock_user import User
import random

def REST_3_3(acc):
    #print(type(acc.shares()))
    while True:
        amount = 0
        for key, value in acc.shares().items():
            amount += 1
        if amount == 40:
            print("Shares amount = 40 - OK")
            break
        elif amount < 40:
            while True:
                exchanges = info.check_exchanges()
                exchange = exchanges[random.randint(0, len(exchanges) - 1)]  # losowa gielda z przedzialu 0 - liczba gield
                shares = info.check_shares(exchange)
                share = shares[random.randint(0, len(shares) - 1)]
                action.stock_action(exchange, share, "buy", 1)
                amount = 0
                for key, value in acc.shares().items():
                    amount += 1
                if amount == 40:
                    break
        elif amount > 40:
            shares = []
            for key, value in acc.shares().items():
                shares.append(key)
            share = shares[random.randint(0, len(shares) - 1)]
            while True:
                if acc.shares()[share] == 1:
                    exchange = info.where(share)
                    action.stock_action(exchange, share, "sell", 1)
                    break
                exchange = info.where(share)
                action.stock_action(exchange, share, "sell", 1)


    for key, value in acc.shares().items():
        share = key
        amount = value
        exchange = info.where(share)
        print("")
        print(share, amount)
        if amount < len(share):
            while True:
                if amount < len(share):
                    action.stock_action(exchange, share, "buy", 1)
                    amount += 1
                    print(share, amount)
                if amount == len(share):
                    break
        if amount > len(share):
            while True:
                if amount > len(share):
                    action.stock_action(exchange, share, "sell", 1)
                    amount -= 1
                    print(share, amount)
                if amount == len(share):
                    break
    print("\nDone.")



account = 0
print("Wybierz uzytkownika: ")
print("1 - Andrzej\n2 - Kuba\n")
choice = int(input("Wybor: "))

Andrzej = ("01159465@pw.edu.pl", "1Lab1")
Kuba = ("01161816@pw.edu.pl", "kubapasierb1")

if choice == 1:
    account = User(login=Andrzej[0], password=Andrzej[1])
    #print(account)
if choice == 2:
    account = User(login=Kuba[0], password=Kuba[1])
    #print(account)

#print(account)
info = stockData()
action = stockDo(user=account)
REST_3_3(account)






