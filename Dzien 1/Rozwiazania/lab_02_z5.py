def czysc_slowo_all(tekst):
    slowo = ""
    for zn in tekst:
        if zn.isalpha():
            slowo += zn
    return slowo.lower()


def czysc_slowo(slowo):
    """
    Czyści poczatek i koniec słowa
    """
    # Usuwamy spacje na początku i na końcu słowa
    slowo = slowo.strip()

    # Usuwamy znaki nie będące literami na początku słowa
    while len(slowo) > 0 and not slowo[0].isalpha():
        slowo = slowo[1:]

    # Usuwamy znaki nie będące literami na końcu słowa
    while len(slowo) > 0 and not slowo[-1].isalpha():
        slowo = slowo[:-1]

    # Zamieniamy słowo na małe litery
    slowo = slowo.lower()

    return slowo


print(czysc_slowo("66#Ok#no5%"))
print(czysc_slowo("okno12"))
