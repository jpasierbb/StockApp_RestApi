from stock_checking import stockData
from stock_action import stockDo
from stock_user import User
import random

def REST_3_1():
    exchanges = info.check_exchanges()
    exchange = exchanges[random.randint(0, len(exchanges) - 1)]  # losowa gielda z przedzialu 0 - liczba gield
    shares = info.check_shares(exchange)
    share = shares[random.randint(0, len(shares) - 1)]
    action.stock_action(exchange, share, "buy", 1)



print("Wybierz uzytkownika: ")
print("1 - Andrzej\n2 - Kuba\n")
choice = int(input("Wybor: "))

Andrzej = ("example_email_one@example.com", "passwordOne")
Kuba = ("example_email_two@example.com", "passwordTwo")

if choice == 1:
    account = User(login=Andrzej[0], password=Andrzej[1])
    #print(account)
if choice == 2:
    account = User(login=Kuba[0], password=Kuba[1])
    #print(account)

#print(account)
info = stockData()
action = stockDo(user=account)
REST_3_1()
