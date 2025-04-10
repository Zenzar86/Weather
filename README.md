# Aplikace Počasí

Jednoduchá GUI aplikace v Pythonu pro zjištění počasí.

## Popis

Tato aplikace využívá knihovnu Tkinter k vytvoření grafického uživatelského rozhraní (GUI). Umožňuje uživateli zadat název města a načte aktuální údaje o počasí pro danou lokalitu ze služby [wttr.in](https://wttr.in/) pomocí jejího JSON API (`https://wttr.in/{mesto}?format=j1`).

Aplikace zobrazuje následující informace:
*   Lokalita (Město, Region, Stát)
*   Teplota (Aktuální a Pocitová ve °C)
*   Popis počasí (např. Slunečno, Zataženo)
*   Vlhkost (%)
*   Rychlost (km/h) a směr větru

## Jak spustit

1.  Ujistěte se, že máte nainstalovaný Python.
2.  Spusťte skript z vašeho terminálu:
    ```bash
    python pocasi.py
    ```
3.  Objeví se okno aplikace. Zadejte název města do vstupního pole a klikněte na tlačítko "Zjistit počasí".

## Závislosti

*   Python 3.x
*   Tkinter (obvykle je součástí standardní instalace Pythonu)

## Poznámky

*   Aplikace používá `ssl._create_unverified_context()` k obejití ověření SSL certifikátu při stahování dat. To může být v některých prostředích nutné, ale obecně se z bezpečnostních důvodů nedoporučuje pro produkční aplikace.
*   Výchozí město je nastaveno na "Praha".
