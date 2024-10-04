class TestKlasa:
    a = 1

    def __init__(self):
        self.b = 2


ob1 = TestKlasa()

print(hasattr(ob1, 'b'))
print(hasattr(ob1, 'a'))
print(hasattr(TestKlasa, 'b'))
print(hasattr(TestKlasa, 'a'))
