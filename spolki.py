import http.client
import mimetypes

def nazwy_spolek(gielda):

    conn = http.client.HTTPSConnection("zsutstockserver.azurewebsites.net")
    payload = ''
    headers = {}
    conn.request("GET", "/api/shareslist/" + str(gielda), payload, headers)
    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")

    spolki = data.replace(chr(34),"")
    spolki = spolki.replace("[", "")
    spolki = spolki.replace("]", "")
    spolki = spolki.split(",")

    return spolki


if __name__ == "__main__":
    print(nazwy_spolek("Warszawa"))
