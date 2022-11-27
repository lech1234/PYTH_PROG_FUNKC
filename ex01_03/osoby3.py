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

# --------------- przykład 1 ----------------
# lista nieposortowana
# -------------------------------------------
print('1. Lista osób nieposortowana:')
lista_osob = [osoba1, osoba2, osoba3, osoba4]
print(*lista_osob, sep='\n')


# --------------- przykład 2 ----------------
# sortowanie wg nazwisk
# -------------------------------------------
def predykat_wg_nazwisk(osoba):
    return osoba['nazwisko']


lista_osob_wg_nazwisk = sorted(lista_osob, key=predykat_wg_nazwisk)
print('\n2. Lista osób posortowana wg nazwisk:')
print(*lista_osob_wg_nazwisk, sep='\n')


# --------------- przykład 3 ----------------
# sortowanie wg płci i wieku
# -------------------------------------------
def predykat_wg_plci_i_wieku(osoba):
    return osoba['plec'], osoba['wiek']


lista_osob_wg_plci_i_wieku = sorted(lista_osob, key=predykat_wg_plci_i_wieku)
print('\n3. Lista osób posortowana wg płci i wieku:')
print(*lista_osob_wg_plci_i_wieku, sep='\n')
