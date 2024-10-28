import os
os.system("cls")


def main() -> None:
    lst = [1, 2, 2, 3, 4, 4, 9]
    print(set(lst))

    print("\ncześć wpólna (przecięcie)")
    zb1 = {1, 2, 9, 3, 4}
    zb2 = {3, 4, 5, 6}
    print(zb1.intersection(zb2))
    print(zb2.intersection(zb1))

    print("\nsuma")
    print(zb1.union(zb2))
    print(zb2.union(zb1))
    print()

    print("\nróżnica")
    print(zb1.difference(zb2))
    print(zb2.difference(zb1))


if __name__ == "__main__":
    main()
