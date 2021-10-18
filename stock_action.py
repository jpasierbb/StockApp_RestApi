import http.client
import json
from base64 import b64encode
from stock_checking import stockData
import math
from stock_user import User

class stockDo:

    def __init__(self, user) -> None:   #przy tworzeniu obiektu trzeba przekazac obiekt klasy user dla ktorego beda transakcje
        self.user = user
        self.header = {
            "Authorization": "Basic {}".format(
                b64encode(bytes(f"{user.mail}:{user.password}", "utf-8")).decode("ascii")),
            "Content-Type": "application/json"
        }
    def stock_action(self, exchange, share, buySell, amount):
        conn = http.client.HTTPSConnection("zsutstockserver.azurewebsites.net")
        info = stockData()
        price = 0
        if buySell == "buy":                                             #dla kupienia trzeba sprawdzic cene sprzedazy i na odwrot
            price = (info.check_price(exchange, share, "sell"))[0]
            price = price + 0.05                                   #do gory
            limit = (info.check_price(exchange, share, "sell"))[1]
            if limit < amount:                                          #jezeli wiecej masz kupic niz mozna ustawia sie na max dostepnych
                amount = int(limit)
            if self.user.userfunds() < (amount * price):
                amount = self.user.userfunds()/price
            if amount == "0":
                return "Nie mozna kupic akcji"
        elif buySell == "sell":
            price = (info.check_price(exchange, share, "buy"))[0] - 0.05                                       #zaokraglenie do calkowitych od dolu
            limit = (self.user.shares())[share]
            if limit < amount:
                amount = int(limit)
            if amount == 0:
                return print("Brak akcji do sprzedania")
        body = json.dumps({
                "stockExchange":f'{exchange}',
                "share":f'{share}',
                "amount":amount,
                "price":price
                })

        #komenda zakupu
        conn.request("POST", url=f"/api/{str(buySell)}offer", headers=self.header, body=body)   #wysyla zlecenie
        if conn.getresponse().status == 200:
            return "ok"
        else:
            print("ERROR")
            print(conn.getresponse().read())

        #print(response)
        #print(response.status)





if __name__ == "__main__":
    user = User("01159465@pw.edu.pl", "1Lab1")
    transakcja = input("rozdzielone spacjami: gielda akcje buy/sell ile: ")
    transakcja = transakcja.split()
    action = stockDo(user=user)
    action.stock_action(transakcja[0],transakcja[1],transakcja[2],int(transakcja[3]))

    
#Znane Errory:
# sprzedawanie nieposiadanych akcji
# blad w zleceniu sprzedazy/kupna (np literowka)
