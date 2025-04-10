import tkinter as tk
from tkinter import messagebox
import urllib.request
import urllib.parse
import json
import ssl

SABLONA_API_URL = "https://wttr.in/{}?format=j1"
NAZEV_OKNA = "Počasí Appka"
VYCHOZI_MESTO = "Praha"

ssl_kontext = ssl._create_unverified_context()

def stahni_pocasí(mesto):
    url = SABLONA_API_URL.format(urllib.parse.quote(mesto))
    with urllib.request.urlopen(url, context=ssl_kontext, timeout=10) as odpoved:
        if odpoved.getcode() == 200:
            data = odpoved.read()
            return json.loads(data.decode('utf-8'))
        else:
            return None

def zobraz_pocasí(data_pocasí):
    if not data_pocasí or 'current_condition' not in data_pocasí or not data_pocasí['current_condition']:
        popisek_lokalita.config(text="Lokalita: --")
        popisek_teplota.config(text="Teplota: --")
        popisek_popis.config(text="Popis: --")
        popisek_vlhkost.config(text="Vlhkost: --")
        popisek_vitr.config(text="Vítr: --")
        return

    aktualni = data_pocasí['current_condition'][0]
    nejblizsi_oblast = data_pocasí.get('nearest_area', [{}])[0]
    stat = nejblizsi_oblast.get('country', [{}])[0].get('value', 'N/A')
    region = nejblizsi_oblast.get('region', [{}])[0].get('value', 'N/A')
    nazev_oblasti = nejblizsi_oblast.get('areaName', [{}])[0].get('value', 'N/A')

    retezec_lokality = f"{nazev_oblasti}, {region}, {stat}"
    teplota_c = aktualni.get('temp_C', 'N/A')
    pocitova_teplota_c = aktualni.get('FeelsLikeC', 'N/A')
    popis = aktualni.get('weatherDesc', [{}])[0].get('value', 'N/A')
    vlhkost = aktualni.get('humidity', 'N/A')
    rychlost_vetru = aktualni.get('windspeedKmph', 'N/A')
    smer_vetru = aktualni.get('winddir16Point', 'N/A')

    popisek_lokalita.config(text=f"Lokalita: {retezec_lokality}")
    popisek_teplota.config(text=f"Teplota: {teplota_c}°C (Pocitová: {pocitova_teplota_c}°C)")
    popisek_popis.config(text=f"Popis: {popis}")
    popisek_vlhkost.config(text=f"Vlhkost: {vlhkost}%")
    popisek_vitr.config(text=f"Vítr: {rychlost_vetru} km/h ({smer_vetru})")

def po_kliknuti_na_tlacitko():
    mesto = vstup_mesto.get()
    if not mesto:
        messagebox.showwarning("Chyba vstupu", "Prosím, zadejte název města.")
        return
    data_pocasí = stahni_pocasí(mesto)
    if data_pocasí:
        zobraz_pocasí(data_pocasí)

okno = tk.Tk()
okno.title(NAZEV_OKNA)
okno.geometry("450x250")

vstupni_ramecek = tk.Frame(okno)
vstupni_ramecek.pack(pady=10)

tk.Label(vstupni_ramecek, text="Město:").pack(side=tk.LEFT, padx=5)
vstup_mesto = tk.Entry(vstupni_ramecek, width=20)
vstup_mesto.pack(side=tk.LEFT, padx=5)
vstup_mesto.insert(0, VYCHOZI_MESTO)

tlacitko_stahnout = tk.Button(vstupni_ramecek, text="Zjistit počasí", command=po_kliknuti_na_tlacitko)
tlacitko_stahnout.pack(side=tk.LEFT, padx=5)

ramecek_vysledku = tk.Frame(okno, pady=10)
ramecek_vysledku.pack(fill=tk.X, padx=20)

popisek_lokalita = tk.Label(ramecek_vysledku, text="Lokalita: --", anchor="w")
popisek_lokalita.pack(fill=tk.X)
popisek_teplota = tk.Label(ramecek_vysledku, text="Teplota: --", anchor="w")
popisek_teplota.pack(fill=tk.X)
popisek_popis = tk.Label(ramecek_vysledku, text="Popis: --", anchor="w")
popisek_popis.pack(fill=tk.X)
popisek_vlhkost = tk.Label(ramecek_vysledku, text="Vlhkost: --", anchor="w")
popisek_vlhkost.pack(fill=tk.X)
popisek_vitr = tk.Label(ramecek_vysledku, text="Vítr: --", anchor="w")
popisek_vitr.pack(fill=tk.X)

if __name__ == "__main__":
    po_kliknuti_na_tlacitko()
    okno.mainloop()