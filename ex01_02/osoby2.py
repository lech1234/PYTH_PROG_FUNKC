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
def predykat_warszawiakow(osoba):
    return osoba['plec'] and osoba['adres'] == 'Warszawa'


warszawiacy = filter(predykat_warszawiakow, lista_osob)
print('1. Lista warszawiaków:', *warszawiacy, sep='\n', end='\n\n')


# -------------------- przykład 2 --------------------------
# lista dwudziestolatków
# ----------------------------------------------------------
def predykat_wieku(osoba):
    return 20 <= osoba['wiek'] < 30


dwudziestoletni = filter(predykat_wieku, lista_osob)
print('2. Lista 20-latków i 20-latek:', *dwudziestoletni, sep='\n', end='\n\n')


# -------------------- przykład 3 --------------------------
# średnia wieku kobiet o imionach rozpoczynających się na 'A'
# ----------------------------------------------------------
def predykat_kobiet_o_imieniu_na_a(osoba):
    return not osoba['plec'] and osoba['imie'].startswith('A')
    # ewentualnie:
    # return not osoba['plec'] and osoba['imie'][0]=='A'


def funkcja_konwersji_na_wiek(osoba):
    return osoba['wiek']


lista_kobiet_na_A = filter(predykat_kobiet_o_imieniu_na_a, lista_osob)
lista_lat = list(map(funkcja_konwersji_na_wiek, lista_kobiet_na_A))
srednia_wieku = sum(lista_lat) / len(lista_lat)
print('3. Średnia wieku kobiet o imionach na A...:', srednia_wieku)
