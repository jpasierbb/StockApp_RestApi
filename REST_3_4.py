from stock_checking import stockData
from stock_action import stockDo
from stock_user import User
import random

def REST_3_4(acc):
    action.sell_all()
    list = info.sort()
    print(list)
    for i in range(len(list)):
        print("----"*4)
        print(info.where(list[i][0]))
        print(list[i][0])
        action.stock_action(info.where(list[i][0]), list[i][0], "buy", i+1)
    print("***** ***")
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
#action.sell_all()
