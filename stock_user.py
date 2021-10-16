import http.client
from base64 import b64encode
import json

class User:
    def __init__(self, mail, password) -> None:
        self.mail = mail                #ustawienie maila dla tej instacji
        self.password = password        #ustawienie hasla
        self.header = {
            "Authorization":"Basic {}".format(
            b64encode(bytes(f"{self.mail}:{self.password}", "utf-8")).decode("ascii"))
            }
        self.conn = http.client.HTTPSConnection("zsutstockserver.azurewebsites.net")     #polaczenie z autoryzacja przez url
    def data(self):
        self.conn.request("GET", "/api/client", headers=self.header)
        data = self.conn.getresponse().read()
        data = json.loads(data)
        print(data)
if __name__ == "__main__":
    andrzej = User("01159465@pw.edu.pl","1Lab1")
    andrzej.data()