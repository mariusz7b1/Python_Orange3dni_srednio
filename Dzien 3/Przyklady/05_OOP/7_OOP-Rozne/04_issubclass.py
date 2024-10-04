class Klasa_A:
    pass


class Klasa_B:
    pass


class Klasa_CA(Klasa_A):
    pass


class Klasa_CAB(Klasa_A, Klasa_B):
    pass


print(issubclass(Klasa_CA, Klasa_A))
print(issubclass(Klasa_CA, Klasa_B))


print(issubclass(Klasa_CAB, Klasa_A))
print(issubclass(Klasa_CAB, Klasa_B))
