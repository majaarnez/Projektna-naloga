import csv

import requests
from bs4 import BeautifulSoup

def zajem_julijske_alpe():
    url = "https://www.hribi.net/gorovje/julijske_alpe/1"
    
    #pridobim vsebino iz spletne strani
    odgovor = requests.get(url)
    soup = BeautifulSoup(odgovor.text, "html.parser")

    #poiščem vrstice s podatki o vrhovih
    vrstice = soup.find_all("tr", class_=["vr0", "vr1"])
    
    hribi = []
    
    for vrstica in vrstice:
        povezava = vrstica.find_all("a")

        if len(povezava) >= 2:
            ime = povezava[0]
            visina = povezava[1]

            url_vrha = "https://www.hribi.net" + ime["href"]

            stevilo_poti = zajem_stevilo_poti(url_vrha)

            #shranim podatke o vrhu
            hribi.append(
                {
                "ime": ime.text.strip(),
                "visina": visina.text.replace("m", "").strip(),
                "stevilo_poti": stevilo_poti
            }
            )

            #print(hribi[-1])
    
    return hribi

def zajem_stevilo_poti(url):
    odgovor = requests.get(url)

    soup = BeautifulSoup(odgovor.text, "html.parser")

    #poiščem podatek o številu poti
    besedilo_poti = soup.find(
        string=lambda besedilo: besedilo and "Število poti:" in besedilo
    )

    stevilo_poti = None

    if besedilo_poti:
        povezava_poti = besedilo_poti.parent.find_next("a")

        if povezava_poti:
            stevilo_poti = povezava_poti.text.strip()

    return stevilo_poti

def shrani_v_csv(hribi):
    with open(
        "hribi.csv", 
        "w", 
        newline = "", 
        encoding="utf-8"
    ) as datoteka:
        writer = csv.DictWriter(
            datoteka,
            fieldnames=["ime", "visina", "stevilo_poti"]
        )

        #zapišem podatke v scv
        writer.writeheader()
        writer.writerows(hribi)
        

print("Zajem podatkov se je začel")
podatki = zajem_julijske_alpe()
shrani_v_csv(podatki)
print("Podatki so shranjeni")
    #print(odgovor.status_code) #ce zazenem program mi da 200 to pomeni da koda dela, karkol drucga ne bi delal
    #print(odgovor.text[:500])