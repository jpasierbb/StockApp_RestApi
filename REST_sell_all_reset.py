from stock_action import stockDo
from stock_user import User

x = input("Podaj komu wyzerowac akcje: \
    \n 1 - Andrzej \
    \n 2 - Kuba")
if x == "1":
    user = User("example_email_one@example.com", "passwordOne")
elif x == "2":
    user = User("example_email_two@example.com", "passwordTwo")
else:
    raise Exception("Blad wyboru")
action = stockDo(user=user)
action.sell_all()
