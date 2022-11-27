"""
Skrypt tworzy listę słowników opisujących osoby, a następnie wykonuje operacje na tych danych.
"""


def utworz_osobe(imie, nazwisko, adres, plec, wiek):
    return {
        'imie': imie,
        'nazwisko': nazwisko,
        'adres': adres,
        'plec': plec,
        'wiek': wiek
    }


# Dane wejściowe
osoba1 = utworz_osobe('Jan', 'Kowalski', 'Warszawa', True, 22)
osoba2 = utworz_osobe('Anna', 'Jabłońska', 'Poznań', False, 18)
osoba3 = utworz_osobe('Tomasz', 'Nowak', 'Wrocław', True, 30)
osoba4 = utworz_osobe('Alicja', 'Młynarska', 'Warszawa', False, 25)

lista_osob = [osoba1, osoba2, osoba3, osoba4]

# -------------------- przykład 1 --------------------------
# lista mężczyzn mieszkających w Warszawie
# ----------------------------------------------------------
warszawiacy = filter(lambda osoba: osoba['plec'] and osoba['adres'] == 'Warszawa', lista_osob)
print('1. Lista warszawiaków:', *warszawiacy, sep='\n', end='\n\n')

# -------------------- przykład 2 --------------------------
# lista dwudziestolatków
# ----------------------------------------------------------
dwudziestoletni = filter(lambda osoba: 20 <= osoba['wiek'] < 30, lista_osob)
print('2. Lista dwudziestolatków i dwudziestolatek:', *dwudziestoletni, sep='\n', end='\n\n')

# -------------------- przykład 3 --------------------------
# średnia wieku kobiet o imionach rozpoczynających się na 'A'
# ----------------------------------------------------------
lista_kobiet_na_A = list(filter(lambda osoba: not osoba['plec']
                                              and osoba['imie'].startswith('A'), lista_osob))
lista_lat = list(map(lambda osoba: osoba['wiek'], lista_kobiet_na_A))
srednia_wieku = sum(lista_lat) / len(lista_lat)
print('3. Średnia wieku kobiet o imionach na A...:', srednia_wieku)
