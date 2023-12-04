#Zadanie 11 Napisz program, który oblicza pole całkowite i objętość prostopadłościanu. Dane podane z klawiatury. W przypadku podania liczby ujemnej lub 0, program powinien wypisywać komunikat informujący o błędnej wartości i nic nie liczyć.

a = int(input('Podaj długosc 1 boku: '))

while a <= 0:
    print('Dlugosc boku musi być liczbą dodatnia.')
    a = int(input('Podaj długosc 1 boku: '))

b = int(input('Podaj dlugosc 2 boku: '))

while b <= 0:
    print('Dlugosc boku musi być liczbą dodatnia.')
    b = int(input('Podaj długosc 2 boku: '))

c = int(input('Podaj długgosc 3 boku: '))

while c <= 0:
    print('Dlugosc boku musi być liczbą dodatnia.')
    c = int(input('Podaj dlugosc 3 boku: '))

def pole_calkowite_prostopadloscianu(a,b,c):
    polecalkowite = 2*(a*b + b*c + a*c)
    return polecalkowite

wynik = pole_calkowite_prostopadloscianu(a, b, c)

objetosc= a*b*c
print(f'Pole całkowite prostopadłościanu o bokach {a}, {b}, {c} wynosi: {wynik}')
print(f'objetosc  prostopadłościanu o bokach {a}, {b}, {c} wynosi: {objetosc}')
