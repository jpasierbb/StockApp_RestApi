import http.client
import json
class stockData:
    def check_price(self, exchange, shares, buySell):  
        conn = http.client.HTTPSConnection("zsutstockserver.azurewebsites.net")                                       #sprawdzanie cen akcji, wymagana nazwa gieldy, nazwa akcji
        conn.request("GET", url=f"/api/shareprice/{exchange}?share={shares}")           #request
        data = conn.getresponse().read()
        conn.close()           
        data = data.decode("utf-8") 
        data = json.loads(data)         #zamiana na liste tablic
        buy = data[0]                   #pierwszy dict zawiera ceny buy
        sell = data[1]                  #drugi dict zawiera ceny sell 
        if buySell == "buy":
            return buy["price"], buy["amount"]      #zwraca tuple cena, ilosc
        if buySell == "sell":
            return sell["price"], sell["amount"]    #zwraca tuple cena, ilosc
    def check_exchanges(self):
        conn = http.client.HTTPSConnection("zsutstockserver.azurewebsites.net")                                                               #sprawdzanie dostepnych gield
        conn.request("GET", url=f"/api/stockexchanges")
        data = conn.getresponse().read()
        conn.close()
        data = data.decode("utf-8")
        data = json.loads(data)
        return data
    def check_shares(self, exchange): 
        conn = http.client.HTTPSConnection("zsutstockserver.azurewebsites.net")                                                         #sprawdzanie dostepnych akcji, wymagana nazwa gieldy
        conn.request("GET", url=f"/api/shareslist/{exchange}")
        data = conn.getresponse().read()
        conn.close()
        data = data.decode("utf-8")
        data = json.loads(data)
        return data


if __name__ == "__main__":  #test
    info = stockData()
    for i in range(5):
        print(info.check_price("Warszawa", "KRUK", "sell"))
        print(info.check_exchanges())
        print(info.check_shares("Warszawa"))