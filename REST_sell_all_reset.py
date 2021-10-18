from stock_action import stockDo
from stock_user import User

x = input("Podaj komu wyzerowac akcje: \
    \n 1 - Andrzej \
    \n 2 - Kuba")
if x == "1":
    user = User(login="01159465@pw.edu.pl", password="1Lab1")
elif x == "2":
    user = User(login="01161816@pw.edu.pl",password="kubapasierb1")
else:
    raise Exception("Blad wyboru")
action = stockDo(user=user)
action.sell_all()
