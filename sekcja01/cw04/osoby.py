"""
Skrypt tworzy listę słowników opisujących osoby, a następnie wykonuje operacje na tych danych.
"""


def utworz_osobe(imie, nazwisko, adres, plec, wiek):
    """
    Funkcja tworzy słownik opisujący osobę.

    :param imie: imię osoby
    :param nazwisko: nazwisko osoby
    :param adres: miejscowość, z której pochodzi dana osoba
    :param plec: płeć osoby (True - mężczyzna, False - kobieta)
    :param wiek: wiek osoby
    :return: słownik zawierający dane osoby
    """
    return {
        'imie': imie,
        'nazwisko': nazwisko,
        'adres': adres,
        'plec': plec,
        'wiek': wiek
    }

if __name__ == '__main__':

    # Dane wejściowe
    osoba1 = utworz_osobe('Jan', 'Kowalski', 'Poznań', True, 22)
    osoba2 = utworz_osobe('Anna', 'Jabłońska', 'Szczecin', False, 18)
    osoba3 = utworz_osobe('Tomasz', 'Nowak', 'Wrocław', True, 30)
    osoba4 = utworz_osobe('Alicja', 'Młynarska', 'Poznań', False, 25)

    lista_osob = [osoba1, osoba2, osoba3, osoba4]

    # Przykład 1: Lista mężczyzn mieszkających w Poznaniu
    poznaniacy = filter(lambda osoba: osoba['plec'] and osoba['adres'] == 'Poznań', lista_osob)
    print('1. Lista poznaniaków:', *poznaniacy, sep='\n', end='\n\n')

    # Przykład 2: Lista dwudziestolatków i dwudziestolatek
    dwudziestoletni = filter(lambda osoba: 20 <= osoba['wiek'] < 30, lista_osob)
    print('2. Lista dwudziestolatków i dwudziestolatek:', *dwudziestoletni, sep='\n', end='\n\n')

    # Przykład 3: Średnia wieku kobiet o imionach rozpoczynających się na 'A'
    lista_kobiet_na_a = list(filter(lambda osoba: not osoba['plec']
                                                  and osoba['imie'].startswith('A'), lista_osob))
    if lista_kobiet_na_a:  # jesli jest choćby 1 osoba spełniająca kryteria
        lista_lat = list(map(lambda osoba: osoba['wiek'], lista_kobiet_na_a))
        srednia_wieku = sum(lista_lat) / len(lista_lat)
        print('3. Średnia wieku kobiet o imionach na \'A\':', srednia_wieku)
