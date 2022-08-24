from sys import argv, exit
import json
import requests
from playsound import playsound
import time

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


def dump1090(notifi_type):
    req_link = f"http://{ip_addres}:{port}/data.json"
    if False == check_connection(req_link, "get"):
        print(f"Site {req_link} is now available")


def Virtualradar(notifi_type):
    last_aircrafts = []
    req_link = f"http://{ip_addres}/VirtualRadar/AircraftList.json"
    if False == check_connection(req_link, "post"):
        print(f"Site {req_link} is now available")
        exit()

    while True:
        try:
            request = requests.post(req_link)

            json_aircrafts_list = json.loads(request.text)["acList"]

            if last_aircrafts != json_aircrafts_list:
                if json_aircrafts_list != []:
                    last_aircrafts = json_aircrafts_list
                    if notifi_type == "sound":
                        playsound("1.mp3")
                    else:
                        print("! AIRCRAFT FIND")
                        
            time.sleep(2)

        except:
            print("ERROR, CONTINUE")
            time.sleep(5)


def check_args(dump, notifi_type):
    if dump == "dump1090" or dump == "virtualradar":
        if notifi_type == "sound" or notifi_type == "text":
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    if check_args(name_dump, notifi_type):
        if name_dump == "dump1090":
            dump1090(notifi_type)
        if name_dump == "virtualradar":
            Virtualradar(notifi_type)
    else:
        print("Invalid arguments!")