"""
Moduł tworzy listę słowników opisujących osoby, a następnie wybiera osoby spełniające zadane kryteria.
Jest to kontynuacja ćwiczenia 2.11 z projektu PYTH_DANE.
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
    def predykat_poznaniakow(osoba):
        """
        Funkcja weryfikuje, czy dana osoba jest mężczyzną z Poznania

        :param osoba: słownik opisujący osobę
        :return: True - jeśli osoba jest mężczyzną z Poznania, False - w pozostałych przypadkach
        """
        return osoba['plec'] and osoba['adres'] == 'Poznań'


    poznaniacy = filter(predykat_poznaniakow, lista_osob)
    print('1. Lista poznaniaków:', *poznaniacy, sep='\n', end='\n\n')

    # Przykład 2: Lista dwudziestolatków i dwudziestolatek
    def predykat_wieku(osoba):
        """
        Funkcja weryfikuje, czy wiek danej osoby mieści się przedziale: co najmniej 20 lat, ale mniej niż 30

        :param osoba: słownik opisujący osobę
        :return: True - jeśli osoba jest 20-latkiem (lub 20-latką)
        """
        return 20 <= osoba['wiek'] < 30


    dwudziestoletni = filter(predykat_wieku, lista_osob)
    print('2. Lista 20-latków i 20-latek:', *dwudziestoletni, sep='\n', end='\n\n')

    # Przykład 3: Średnia wieku kobiet o imionach rozpoczynających się na 'A'
    def predykat_kobiet_o_imieniu_na_a(osoba):
        """
        Funkcja weryfikuje, czy dana osoba jest kobietą o imieniu zaczynającym się na literę 'A'

        :param osoba: słownik opisujący osobę
        :return: True - jeśli to kobieta o imieniu na literę 'A', False - w przeciwnym razie
        """
        return not osoba['plec'] and osoba['imie'].startswith('A')
        # ewentualnie:
        # return not osoba['plec'] and osoba['imie'][0]=='A'


    def wiek_osoby(osoba):
        """
        Funkcja konwertuje osobę na jej wiek.

        :param osoba: słownik opisujący osobę
        :return: wiek osoby
        """
        return osoba['wiek']


    lista_kobiet_na_a = filter(predykat_kobiet_o_imieniu_na_a, lista_osob)
    if lista_kobiet_na_a:  # jesli jest choćby 1 osoba spełniająca kryteria
        lista_wieku_kobiet_na_a = list(map(wiek_osoby, lista_kobiet_na_a))
        srednia_wieku = sum(lista_wieku_kobiet_na_a) / len(lista_wieku_kobiet_na_a)
        print('3. Średnia wieku kobiet o imionach na \'A\':', srednia_wieku)
