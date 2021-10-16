import http.client
import json
class stockData:
    def __init__(self) -> None:
        self.conn = http.client.HTTPSConnection("zsutstockserver.azurewebsites.net")
    def check_price(self, exchange, shares, buySell):                                        #sprawdzanie cen akcji
        self.conn.request("GET", url=f"/api/shareprice/{exchange}?share={shares}")           #request
        data = self.conn.getresponse().read()
        data = data.decode("utf-8")
        data = json.loads(data)
        buy = data[0]
        sell = data[1]
        if buySell == "buy":
            return buy["price"], buy["amount"]
        if buySell == "sell":
            return sell["price"], sell["amount"]
    def check_exchanges(self):                                                               #sprawdzanie dostepnych gield
        self.conn.request("GET", url=f"/api/stockexchanges")
        data = self.conn.getresponse().read()
        data = data.decode("utf-8")
        data = json.loads(data)
        return data
    def check_shares(self, exchange):
        self.conn.request("GET", url=f"/api/shareslist/{exchange}")
        data = self.conn.getresponse().read()
        data = data.decode("utf-8")
        data = json.loads(data)
        return data


if __name__ == "__main__":  #test
    info = stockData()
    print(info.check_price("Warszawa", "11BIT", "buy"))
    print(info.check_exchanges())
    print(info.check_shares("Warszawa"))