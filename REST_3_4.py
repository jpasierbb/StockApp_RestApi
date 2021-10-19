from stock_checking import stockData
from stock_action import stockDo
from stock_user import User
import random

def REST_3_4(acc):
    info = stockData()
    unique_shares = []      #lista unikalnych spolek (bez duplikatow)
    for exchange in info.check_exchanges():
        for share in info.check_shares(exchange):
            if share not in unique_shares:
                unique_shares.append(share)
    for i in range(len(unique_shares)-1,-1,-1):
        current_share = unique_shares[i]
        where = info.where(current_share)
        while True:
            action.stock_action(where, current_share, "buy", 1)
            amount = acc.shares()[current_share]
            if amount == i+1:
                break





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
action = stockDo(user=account)
REST_3_4(account)
#action.sell_all()
