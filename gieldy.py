import http.client
import mimetypes

def nazwy_gield():

    conn = http.client.HTTPSConnection("zsutstockserver.azurewebsites.net")
    payload = ''
    headers = {}
    conn.request("GET", "/api/stockexchanges", payload, headers)
    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")

    nazwy = data.replace(chr(34),"")
    nazwy = nazwy.replace("[", "")
    nazwy = nazwy.replace("]", "")
    nazwy = nazwy.split(",")

    return nazwy


if __name__ == "__main__":
    print(nazwy_gield())