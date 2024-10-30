"""
Opakowanie - wrappery 
"""

from os import system
system('cls')


def fun_glowna(fun_opakowywana):
    def opakowujaca():
        print(f"start opakowania '{fun_opakowywana.__name__}'")
        fun_opakowywana()
        print("opakowujaca stop")
        # input("naciśnij coś aby kontynuować ")
    return opakowujaca

# fun1 i fun2 maj swoj funkcionalność i nie mogę ich ruszać
# mogą być np w module


def fun1():
    print(f"!! Funkcja {fun1.__name__} ktora jest opakowywana !!")


def fun2():
    print(f"** Funkcja {fun2.__name__} ktora jest opakowywana **")


fun1_z_opakowaniem = fun_glowna(fun1)
fun2_z_opakowaniem = fun_glowna(fun2)

# wywołanie

fun1_z_opakowaniem()
fun2_z_opakowaniem()
