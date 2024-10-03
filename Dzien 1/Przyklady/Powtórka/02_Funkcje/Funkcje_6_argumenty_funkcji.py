# args kwargs

def show_parameters(id, nazwisko='X', *args, **kwargs):
    print(id, nazwisko)
    print(f"Parametrów pozycyjnych {
          len(args)}, parametrów nazwanych {len(kwargs)}")
    print('args=', args)
    print('kwargs=', kwargs)
    print('-'*30)


show_parameters(1)
show_parameters(2, 'Kowalski')
show_parameters(3, 'Kowalski', 'Jan')
show_parameters(4, 'Kowalski', 'testujemy', imie='Jan', nip=24324)

posiadane_samochody = ['Ford', 'Ferrari,', 'Fiat']
dane_osobiste = {'pesel': 23645234, 'nip': 3245432}
show_parameters(5, 'Kowalski', posiadane_samochody, dane_osobiste)
show_parameters(6, 'Nowak', *posiadane_samochody, **dane_osobiste)
