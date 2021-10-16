import http.client
from base64 import b64encode
import json

class User:
    def __init__(self, mail, password) -> None:
        self.mail = mail                #ustawienie maila dla tej instacji
        self.password = password        #ustawienie hasla
        self.header = {
            "Authorization":"Basic {}".format(
            b64encode(bytes(f"{self.mail}:{self.password}", "utf-8")).decode("ascii"))  #
            }
        self.conn = http.client.HTTPSConnection("zsutstockserver.azurewebsites.net")     #polaczenie z autoryzacja przez url
    def userinfo(self):
        self.conn.request("GET", "/api/client", headers=self.header)
        data = self.conn.getresponse().read()
        self.conn.close()
        data = json.loads(data)
        print(data)
    def userfunds(self):
        self.conn.request("GET", "/api/client", headers=self.header)
        data = self.conn.getresponse().read()
        self.conn.close()
        data = json.loads(data)
        funds = data["funds"]
        return funds
    def history(self):
        self.conn.request("GET", "/api/history", headers=self.header)
        data = self.conn.getresponse().read()
        self.conn.close()
        data = json.loads(data)
        return data
if __name__ == "__main__":
    mail = input("wprowadz mail ")
    password = input("wprowadz haslo ")
    user = User(mail,password)
    print(user.userinfo())
    print(f"\n"*3)
    print(user.history())
    print(f"\n"*3)
    print(user.userfunds())
