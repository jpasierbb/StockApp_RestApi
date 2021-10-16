from stock_checking import stockData
from stock_action import stockDo
from stock_user import User
import random

def random_50():
    exchanges = info.check_exchanges()
    exchange = exchanges[random.randint(0,len(exchanges)-1)]  #losowa gielda z przedzialu 0 - liczba gield
    shares = info.check_shares(exchange)
    share = shares[random.randint(0,len(shares)-1)]
    for i in range(50):
        action.stock_action(exchange,share,"buy",1)




mail = input("podaj mail podany przy rejestracji: ")
password = input("podaj haslo: ")
pick = input("\n \n \
    Wybierz co chcesz zrobic: \
    \n 1. Kup 50 losowych akcji \
    \n 2. Kup tyle akcji co nazwa dla 40 spolek \
    \n 3. Kup wszystkie spolki tak zeby nie miec tylu samo \
    \n Twoj wybor: ")

user = User(login=mail, password=password)
action = stockDo(login=mail, password=password)
info = stockData()
random_50()





