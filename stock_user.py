import http.client
from base64 import b64encode
import json

class User:
    def __init__(self, login, password) -> None:
        self.mail = login               #ustawienie maila dla tej instacji
        self.password = password        #ustawienie hasla
        self.header = {
            "Authorization":"Basic {}".format(
            b64encode(bytes(f"{self.mail}:{self.password}", "utf-8")).decode("ascii"))  #base64 dziala tylko w zapisie bitowym, potem trzeba decodowac na ascii
            }
        self.conn = http.client.HTTPSConnection("zsutstockserver.azurewebsites.net")     #polaczenie z autoryzacja przez url
    def userinfo(self):     #zwraca dane o uzytkowniku
        self.conn.request("GET", "/api/client", headers=self.header)
        data = self.conn.getresponse().read()
        self.conn.close()
        data = json.loads(data)
        return data
    def userfunds(self):    #zwraca liczbe funduszy
        data = self.userinfo()
        data = data["funds"]
        return data
    def history(self):  #zwraca json historii
        self.conn.request("GET", "/api/history", headers=self.header)
        data = self.conn.getresponse().read()
        self.conn.close()
        data = json.loads(data)
        return data
    def transactions(self): #zwraca liste transakcji
        data = self.history()
        data = data["transactions"]
        return data
    def transactions_amount(self):  #zwraca liczbe transakcji
        return len(self.transactions())
    def grade(self):    #zwraca ocene
        return (self.history())["mark"]
    def shares(self):   #zwraca liste akcji; nazwa, gielda, ilosc
        return (self.userinfo())["shares"] #zwraca dict {akcja: liczba}
    def shares_amount(self):    #zwraca liczbe akcji
        data = (self.userinfo())["shares"]
        sum = 0
        for key, value in data.items():
            sum = sum + value
        return sum

        
if __name__ == "__main__":      #testowanie
    mail = input("wprowadz mail ")
    password = input("wprowadz haslo ")
    user = User(mail,password)
    for i in range(10):
        print(user.userinfo())
        print(f"\n"*3)
        print(user.history())
        print(f"\n"*3)
        print(user.userfunds())
        print(f"\n"*3)
        print(user.transactions())
        print(f"\n"*3)
        print(user.transactions_amount())
        print(f"\n"*3)
        print(user.grade())
        print(f"\n"*3)
        print(user.shares())
        print(f"\n"*3)
        print(user.shares_amount())
    

