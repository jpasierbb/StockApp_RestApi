import http.client
import json
from base64 import b64encode
from stock_checking import stockData

class stockDo:

    def __init__(self, login, password) -> None:
        self.login = str(login)
        self.password = str(password)
        self.conn = http.client.HTTPSConnection("zsutstockserver.azurewebsites.net")

    def stock_action(self, stock, name, buySell, amount):
        # Klasa zczytuje ceny i ilosc akcji sprzedazy/kupowania
        # Cena danej spolki
        # Limit czyli ilosc dostepnych akcji, przyda sie zeby program nie chcial kupic wiecej niz jest
        info = stockData()
        price_limit = info.check_price(stock, name, buySell)
        price = price_limit[0]
        limit = price_limit[1]

        #paramtery, ktore trzerba podac do kupna sprzedazy, login itd
        header = {
            "Authorization": "Basic {}".format(
                b64encode(bytes(f"{self.login}:{self.password}", "utf-8")).decode("ascii")),
        }
        body = json.dumps({"price": price, "buySell": str(buySell), "amount": amount,
            "stockExchange": str(stock), "share": str(name)})

        #komenda zakupu
        self.conn.request("POST", url=f"/api/{buySell}offer", headers=header, body=body)
        response = self.conn.getresponse()

        #print(response)
        #print(response.status)





if __name__ == "__main__":
    action = stockDo("01159465@pw.edu.pl","1Lab1")
    action.stock_action("Warszawa", "11BIT", "buy", 10)
    print(action.stock_action("Warszawa", "11BIT", "buy", 10))
