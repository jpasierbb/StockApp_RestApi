from stock_checking import stockData
from stock_action import stockDo
from stock_user import User
import random

def REST_3_2():
    for i in range(53):
        exchanges = info.check_exchanges()
        exchange = exchanges[random.randint(0, len(exchanges) - 1)]  # losowa gielda z przedzialu 0 - liczba gield
        shares = info.check_shares(exchange)
        share = shares[random.randint(0, len(shares) - 1)]
        action.stock_action(exchange, share, "buy", 1)


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
REST_3_2()






