"""
Moduł definiuje funkcje określenie nazwy dnia tygodnia na podstawie podanej daty.
"""
def __numer_dnia_tygodnia(data, separator):
    """
    Funkcja konwertuje datę na numer dnia tygodnia.

    :param data: data w postaci tekstu, w kolejności: dzień, miesiąc, rok
    :param separator: separator oddzielający dzień od miesiąca i miesiąc od roku
    :return: numer dnia tygodnia (0 - niedziela, 1 - poniedziałek, ..., 6 - sobota)
    """
    dzien, miesiac, rok = data.split(sep=separator)

    dzien = int(dzien)
    miesiac = int(miesiac)
    rok = int(rok)

    if miesiac < 3:
        z = rok - 1
        c = 0
    else:
        z = rok
        c = 2
    return (23 * miesiac // 9 + dzien + 4 + rok + z // 4 - z // 100 + z // 400 - c) % 7


def __nazwa_dnia_tygodnia(numer_dnia):
    """
    Funkcja konwertuje numer dnia tygodnia na jego nazwę.

    :param numer_dnia: numer dnia tygodnia (0, 1, ..., 6)
    :return: nazwa dnia tygodnia
    """
    nazwa_dnia = 'niedziela', 'poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota'
    return nazwa_dnia[numer_dnia]


def jaki_to_dzien(data, *, sep='-'):
    """
    Funkcja wypisuje podaną datę i nazwę dnia tygodnia odpowiadającą tej dacie.

    :param data: data w postaci tekstu, w kolejności: dzień, miesiąc, rok
    :param sep: separator oddzielający dzień od miesiąca i miesiąc od roku
    :return: None
    """
    numer = __numer_dnia_tygodnia(data, sep)
    nazwa = __nazwa_dnia_tygodnia(numer)
    print(f'W dniu {data} wypada {nazwa}')


if __name__ == '__main__':
    jaki_to_dzien('24/12/2023', sep='/')
    jaki_to_dzien('25-12-2023', sep='-')
    jaki_to_dzien('26-12-2023')
