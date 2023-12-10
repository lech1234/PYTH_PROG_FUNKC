"""
Moduł tworzy listę słowników opisujących osoby, a następnie je sortuje wg zadanych kryteriów.
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

    # Przykład 1: lista nieposortowana
    print('1. Lista osób nieposortowana:')
    print(*lista_osob, sep='\n')

    # Przykład 2: sortowanie wg nazwisk
    def klucz_wg_nazwisk(osoba):
        return osoba['nazwisko']


    lista_osob_wg_nazwisk = sorted(lista_osob, key=klucz_wg_nazwisk)
    print('\n2. Lista osób posortowana wg nazwisk:')
    print(*lista_osob_wg_nazwisk, sep='\n')

    # Przykład 3: sortowanie wg płci i wieku
    def klucz_wg_plci_i_wieku(osoba):
        return osoba['plec'], osoba['wiek']


    lista_osob_wg_plci_i_wieku = sorted(lista_osob, key=klucz_wg_plci_i_wieku)
    print('\n3. Lista osób posortowana wg płci i wieku:')
    print(*lista_osob_wg_plci_i_wieku, sep='\n')
