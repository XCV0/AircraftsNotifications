from sys import argv, exit
from tabnanny import check
import requests

filename, name_dump, notifi_type, ip_addres, port = argv

def check_connection(url, method):
    try:
        if method == "get":
            requests.get(url)
        if method == "post":
            requests.post(url)
        
        return True
    except requests.ConnectionError:
        return False


def dump1090():
    req_link = f"http://{ip_addres}:{port}/data.json"
    if False == check_connection(req_link, "get"):
        print(f"Site {req_link} is now available")    


def Virtualradar():
    req_link = f"http://{ip_addres}/VirtualRadar/AircraftList.json"
    if False == check_connection(req_link, "post"):
        print(f"Site {req_link} is now available")    


if __name__ == "__main__":
    if name_dump == "dump1090":
        dump1090()
    if name_dump == "virtualradar":
        Virtualradar()