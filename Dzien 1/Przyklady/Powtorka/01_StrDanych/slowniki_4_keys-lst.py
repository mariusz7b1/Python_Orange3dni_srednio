"""taki test struktur"""
dct = {}
dct["imie"] = "Jan"
dct["nazwisko"] = "Nowak"
dct["wiek"] = 12
dct["adres"] = {"ulica": "Kosciuszki", "nrdomu": 12, "nrmieszkania": 6}
dct["adresy_mail"] = ("jan.nowak@gmail.com",
                      "nowak@gmail.com", "j.nowak@gmail.com")

lst = []
for i in dct:
    lst.append(i)

print(lst)
