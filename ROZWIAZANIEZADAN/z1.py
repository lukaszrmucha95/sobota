#Zadanie 1 Napisz program umożliwiający obliczenie ile paliwa spala samochód na 100 km. Dane wczytane z klawiatury. Podajemy ilość zużytego paliwa w litrach i pokonaną odległośćto zużyte paliwo 22 litry i przejechana trasa 600 km.



#wczytujemy dane

zuzyte_paliwo = int(input("Podaj ilosc zuzytego paliwa w litrach: "))
dystans = int(input("Podaj przejechana trase w kilometrach: "))

#jeśli samochód spala na 600km 22 litry paliwa, to na sto kilometrów spali: 

dystans/100 == (zuzyte_paliwo/(dystans/100))

#wyswieylamy wynik
print("Samochód na sto kilometrów spali:", round(zuzyte_paliwo / (dystans / 100), 4),"litrów benzyny")
