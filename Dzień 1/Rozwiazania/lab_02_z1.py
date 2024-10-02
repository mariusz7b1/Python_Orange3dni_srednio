
def check_palimdrom(tekst):
    # wyciananie spacji i zamienianie na małe litery
    tekst = tekst.lower().replace(" ", "")
    # tekst [::-1] daje w odwrotnej  kolejności
    return True if tekst == tekst[::-1] else False


lst_text = ["Akta generała ma mała renegatka",
            " Kobyła ma mały bok", "Malajalam", "mariusz"]
for t1 in lst_text:
    print(f"Czy: {t1:33} jest palimdormem ? :{check_palimdrom(t1)}")
