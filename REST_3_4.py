from stock_checking import stockData
from stock_action import stockDo
from stock_user import User
import random

def REST_3_4(acc):
    #print(type(acc.shares()))
    exchanges = info.check_exchanges()
    for exchange in exchanges:
        shares = info.check_shares(exchange)
        print(f"\nGielda: {exchange}")
        print(f"Spolki: \n{shares}\n")
        gieldy = [k for k, v in acc.shares().items()]
        if acc.shares()[gieldy[0]] == 1:
            break
        for share in shares:
            action.stock_action(exchange, share, "buy", 1)
            print(f"Kupiono udzial: {share}")
    print("\nAll shares - OK\n")

    shares = [k for k, v in acc.shares().items()]
    amounts = [v for k, v in acc.shares().items()]
    print(shares, "\n", amounts)
    if acc.shares()[shares[0]] > 1:
        while True:
            if acc.shares()[shares[0]] == 1:
                break
            action.stock_action(info.where(shares[0]), shares[0], "sell", 1)
            print(f"Sprzedano akcje {shares[0]}")
    amounts = [v for k, v in acc.shares().items()]
    print(shares[0])
    print(amounts[0])

    i = 0
    while True:
        i += 1
        if i == len(shares):
            break
        if acc.shares()[shares[i]] == acc.shares()[shares[i-1]] + 1:
            continue
        if acc.shares()[shares[i]] > acc.shares()[shares[i-1]] + 1:
            while True:
                if acc.shares()[shares[i]] == acc.shares()[shares[i-1]] + 1:
                    break
                action.stock_action(info.where(shares[i]), shares[i], "sell", 1)
                print(f"Sprzedano akcje {shares[i]}")
        elif acc.shares()[shares[i]] < acc.shares()[shares[i-1]] + 1:
            while True:
                if acc.shares()[shares[i]] == acc.shares()[shares[i-1]] + 1:
                    break
                action.stock_action(info.where(shares[i]), shares[i], "buy", int(acc.shares()[shares[i]] - acc.shares()[shares[i-1]]))
                print(f"Kupiono akcje {shares[i]}")
    print("\nDone.")



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
REST_3_4(account)
#print(info.where("WORKSERV"))

