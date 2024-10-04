def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


liczby = list(range(1, 101))
pierwsze_kwadraty = list(map(lambda x: x**2, filter(czy_pierwsza, liczby)))
