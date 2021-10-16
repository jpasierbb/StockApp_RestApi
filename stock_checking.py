import http.client
import json
class stockData:
    def __init__(self) -> None:
        self.conn = http.client.HTTPSConnection("zsutstockserver.azurewebsites.net")        #nawiazanie polaczenia(jednorazowo przy wywolaniu instancji)
    def check_price(self, exchange, shares, buySell):                                        #sprawdzanie cen akcji, wymagana nazwa gieldy, nazwa akcji
        self.conn.request("GET", url=f"/api/shareprice/{exchange}?share={shares}")           #request
        data = self.conn.getresponse().read()           
        data = data.decode("utf-8") 
        data = json.loads(data)         #zamiana na liste tablic
        buy = data[0]                   #pierwszy dict zawiera ceny buy
        sell = data[1]                  #drugi dict zawiera ceny sell 
        if buySell == "buy":
            return buy["price"], buy["amount"]      #zwraca tuple cena, ilosc
        if buySell == "sell":
            return sell["price"], sell["amount"]    #zwraca tuple cena, ilosc
    def check_exchanges(self):                                                               #sprawdzanie dostepnych gield
        self.conn.request("GET", url=f"/api/stockexchanges")
        data = self.conn.getresponse().read()
        data = data.decode("utf-8")
        data = json.loads(data)
        return data
    def check_shares(self, exchange):                                                          #sprawdzanie dostepnych akcji, wymagana nazwa gieldy
        self.conn.request("GET", url=f"/api/shareslist/{exchange}")
        data = self.conn.getresponse().read()
        data = data.decode("utf-8")
        data = json.loads(data)
        return data


if __name__ == "__main__":  #test
    info = stockData()
    print(info.check_price("Warszawa", "GRODNO", "sell"))
    print(info.check_exchanges())
    print(info.check_shares("Warszawa"))