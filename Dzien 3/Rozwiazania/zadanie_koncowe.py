
# importowanie modułow
import sys
import json
from os import system
from datetime import datetime

"""Funckja nie jest związana z zadaniem slyży mi tylko do pomiaru czasu wykonania kodu"""


def mierz_czas_zapisz_log(func):
    def opakowujaca(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        stop = datetime.now()
        tekst = start.strftime("%Y-%m-%d %H:%M:%S\n")
        tekst += f"Argumenty wywołania: {args}\n"
        tekst += f"Czas wykonania {func.__name__}: {str(stop-start)} \n"

        with open("logi.txt", 'a', encoding="utf-8") as f:
            f.write(tekst)
        return result
    return opakowujaca

# zwraca miasto z adresu


def get_miasto(adres):
    lst_adres = adres.split(",")
    miasto = lst_adres[1]
    miasto = miasto[7:]

    return miasto

# zwraca dostawce @ z adresu mail


def get_mail(mail):
    adres_mail = mail.split("@")[1]
    return adres_mail

# pobiera dane z liku zwraca listę ktorej elementami jest słownik


def get_data_fromfile(pelna_nazwa_pliku):
    try:
        f_in = open(pelna_nazwa_pliku, 'rt', encoding='utf-8')
    except IOError:
        print('Brak pliku z danymi zrodłowymi')
        sys.exit()

    dane = []
    anomalie = ["Te linie są niezgodne z formatem:\n"]
    linia = f_in.readline()
    # traktuję pierwszą linię jako wzorcową jeśli chodzi o ilość danych
    # rozdzielonych separatorem, jesli trafi się jakaś linia o innej dlugości
    # bedzie ignorowana
    dane_linia = linia.split(";")
    ilosc_danych = len(dane_linia)

    while linia != '':
        linia = linia.strip()
        dane_linia = linia.split(";")
        if len(dane_linia) == ilosc_danych:  # tylko wlasciwe linie
            imie = dane_linia[0]
            nazwisko = dane_linia[1]
            miasto = get_miasto(dane_linia[4])
            dostawca_mail = get_mail(dane_linia[8])
            dane_wrazliwe = {"pesel": dane_linia[2], "nip": dane_linia[3]}
            # Tworzenie słownika i dodanie do tablicy
            dane.append({"imie": imie,
                        "nazwisko": nazwisko,
                         "miasto": miasto,
                         "dostawca_mail": dostawca_mail,
                         "dane_wrazliwe": dane_wrazliwe})
        else:
            # Anomalie
            anomalie.append(linia + "\n")

        linia = f_in.readline()

    f_in.close()
    with open("d:\\dane\\raport_anomali.txt", "wt", encoding="utf-8") as f_out:
        f_out.writelines(anomalie)   # zapisuje liste do pliku

    return dane

# zwraca słownik wystapienia danej wartosci wraz z ilością wystąpien


def save_date_to_file(sciezka_do_pliku, nazwa_pliku, slownik):
    nazwa_pliku = sciezka_do_pliku + "\\" + nazwa_pliku + ".txt"
    with open(nazwa_pliku, "wt", encoding="utf-8") as f_out:
        for wartosc in slownik.keys():
            f_out.write(wartosc + "\n")


def get_dic_unique_data(dane, pole):
    slownik = {}
    for ele in dane:
        war = ele[pole]
        if war not in slownik.keys():
            slownik[war] = 1
        else:
            slownik[war] += 1
    return slownik

# zwraca liste z najbardziej popoularna wartoscia
# jesli parametr minmax > 0 to najmniej popularna wartosć


def get_most_popolar(slownik, minmax=0):
    if minmax == 0:
        wartosc_maks = max(slownik.values())
    else:
        wartosc_maks = min(slownik.values())
    # przewiduje sytuacje ze moze być kilka najmniej/najbardziej popularnych
    # dlatego roboczo tworze liste lst
    lst = []
    for klucz in slownik.keys():
        if slownik[klucz] == wartosc_maks:
            lst.append({klucz: slownik[klucz]})
    return lst

# zwraca ilość wystapien danej wartości


def count_var_in_dic(slownik, var):

    if var in slownik.keys():
        return slownik[var]
    else:
        return 0


def zapisz_json(plik, dane):

    with open(plik, "w", encoding="utf-8") as plik_json:
        json.dump(dane, plik_json, ensure_ascii=False, indent=4)


# czyszczenie ekranu
@mierz_czas_zapisz_log
def main(ile_danych='10K'):
    system("cls")

    nazwa_pliku = "dane" + ile_danych + ".txt"
    sciezka_do_pliku = "d:\\dane\\"

    # pełna nazwa pliku wraz ze scieżką
    pelna_nazwa_pliku = sciezka_do_pliku + nazwa_pliku

    # pobranie danych do tablicy
    lst_dane = get_data_fromfile(pelna_nazwa_pliku)
    zapisz_json(sciezka_do_pliku + "dane_wybrane.json", lst_dane)

    # utworzenie slownika z imionami i czestością ich
    dic_imion = get_dic_unique_data(lst_dane, 'imie')
    save_date_to_file(sciezka_do_pliku, "imiona", dic_imion)

    dic_nazwisk = get_dic_unique_data(lst_dane, 'nazwisko')
    save_date_to_file(sciezka_do_pliku, "nazwisko", dic_nazwisk)

    dic_miasto = get_dic_unique_data(lst_dane, 'miasto')
    save_date_to_file(sciezka_do_pliku, "miasto", dic_miasto)

    dic_mail = get_dic_unique_data(lst_dane, 'dostawca_mail')
    save_date_to_file(sciezka_do_pliku, "mail", dic_mail)

    print("Liczba różnych imion to  ", len(dic_imion))
    print("Liczba różnych nazwisk to", len(dic_nazwisk))
    print("Liczba różnych miast   to", len(dic_miasto))
    print("Liczba różnych dostawców @ to", len(dic_mail))

    polularne_imie = get_most_popolar(dic_imion)
    polularne_nazwisko = get_most_popolar(dic_nazwisk)
    polularne_miasto = get_most_popolar(dic_miasto)
    polularny_dostawca = get_most_popolar(dic_mail)

    print("najbardziej popularne imie/imiona to:", polularne_imie)
    print("najbardziej popularne nazwisko/nazwiska to:", polularne_nazwisko)
    print("najbardziej popularne miasto/miasta to:", polularne_miasto)
    print("najbardziej popularny dostawca @ to :", polularny_dostawca)

    polularne_imie = get_most_popolar(dic_imion, 1)
    polularne_miasto = get_most_popolar(dic_miasto, 1)

    print("najmniej popularne imie/imiona to:", polularne_imie)
    print("najmniej popularne miasto/miasta to:", polularne_miasto)

    print("w Opolu mieszka {} mieszkancow".format(
        count_var_in_dic(dic_miasto, "Opole")))


if __name__ == '__main__':
    for i in ("1K", "10K", "100K"):
        main(i)
    print(" !!!!!!!!!!!! KONIEC")
