import requests  #knjiznica da pobira iz spletnih strani
from bs4 import BeautifulSoup

def zajem_julijske_alpe():
    url = "https://www.hribi.net/gorovje/julijske_alpe/1"

    odgovor = requests.get(url)
    soup = BeautifulSoup(odgovor.text, "html.parser")
    vrstice = soup.find_all("tr", class_=["vr0", "vr1"])
    
    hribi = []
    
    for vrstica in vrstice:
        povezava = vrstica.find_all("a")

        if len(povezava) >= 2:
            ime = povezava[0]
            visina = povezava[1]

            hribi.append({
                "ime": ime.text.strip(),
                "visina": visina.text.replace("m", "").strip()
            })
    return hribi

podatki = zajem_julijske_alpe()

for hrib in podatki:
    print(hrib)

    #print(odgovor.status_code) #ce zazenem program mi da 200 to pomeni da koda dela, karkol drucga ne bi delal
    #print(odgovor.text[:500])