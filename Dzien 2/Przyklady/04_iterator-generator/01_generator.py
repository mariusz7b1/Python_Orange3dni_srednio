"""
generatory 
"""


def nieskonczona():
    num = 0
    while True:
        yield num
        num += 1


pass
for i in nieskonczona():
    print(i, end=" ")
