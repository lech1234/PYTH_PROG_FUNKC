def numer_dnia_tygodnia(data_tekstowa, separator):
    dzien, miesiac, rok = data_tekstowa.split(sep=separator)

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


def nazwa_dnia_tygodnia(numer_dnia):
    nazwa_dnia = 'niedziela', 'poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota'
    return nazwa_dnia[numer_dnia]


def jaki_to_dzien(data_tekstowa, *, sep='-'):
    numer = numer_dnia_tygodnia(data_tekstowa, sep)
    nazwa = nazwa_dnia_tygodnia(numer)
    print('Dzień', data_tekstowa, 'to', nazwa)


data = input('Podaj datę (dd-mm-rrrr): ')
jaki_to_dzien(data)
data = input('Podaj datę (dd/mm/rrrr): ')
jaki_to_dzien(data, sep='/')
