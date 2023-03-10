# Pętla nie powinna modyfikować elementów po któych iteruje
lista = [1, 2, 3, 4, 5, 6]
for element in lista:
    if element%2 == 0:
        lista.append(element) #pętla nieskończona

lista = [1, 2, 3, 4, 5, 6]
for i in range(len(lista)-1, -1, -1):
    if lista[i]%2==0:
        lista.append(lista[i]) #iterujemy od tyłu, elementy dołączone nie będą iterowane

# Obiekty zmienne (mutable) powinny być kopiowane a nie powinna być tworzona referencja
lista = [1, 2, 3, 4, 5, 6]
lista2 = lista
id(lista) == id(lista2)
lista2.append(7)
print(lista, lista2)
id(lista) == id(lista2)
lista.append(8)
print(lista, lista2)
id(lista) == id(lista2)

import copy
lista = [[1,2,3], [4,5,6], 9, 0]
lista2 = copy.copy(lista) #kopia płytka, kopiuje tylko liste, bez list zagnieżdzonych
lista3 = copy.deepcopy(lista) #kopia głęboka, kopiuje liste i listy zagnieżdzone
lista[0][1] = 7 # zmieniamy jeden element w liście zagnieżdzonej
print(lista2, lista3) #kopia płytka ma zmieniony element, głęboka nie 
lista[0] = [7,8,9] #zmieniay cały wyraz list
print(lista2, lista3) #kopia płytka i głęboka nie mają zmienionych elementów

# Pobranie ilości bajtów poświęconych na zmienną
import sys
sys.getsizeof(['1234345678934567834567'])
sys.getsizeof('1234345678934567834567')

# Obiekty zmienne (mutable) nie powinny być używane w w argumentach domyślnych funkcji
def dodaj_elementy(lista = ['a', 'b', 'c']):
    for i in range(len(lista)-1, -1, -1):
        lista.append(lista[i])
    return lista

lista_1 = dodaj_elementy()
print(lista_1)
lista_2 = dodaj_elementy() #pracuje na lista = ['a','b','c','c','b','a'] czyli na edytowanej przez poprzednie wywołanie funkcji
print(lista_2)

    # Zamiast tego można zastosować:
def dodaj_elementy(lista = None): # lista jest domyślnie pustym obiektem
    if lista is None: # tworzymy listę z elementami jak wcześniej w argumentach domyślnych
        lista = ['a', 'b', 'c']
    for i in range(len(lista)-1, -1, -1):
        lista.append(lista[i])
    return lista

lista_1 = dodaj_elementy()
print(lista_1)
lista_2 = dodaj_elementy() #lista jest tworzona na nowo w definicji funkcji
print(lista_2)

# Konkatencja może być kosztowna obliczeniowo
import time

string = ''
start = time.time()
for i in range(10000):
    string += 'aaa ' #obiekt jest każdorazowo nadpisywany, bo iest inmutable
stop = time.time()
print(f"Minęło {stop-start} sekund")

    #to będzie działało szybciej
lista = []
for i in range(10000):
    lista.append('aaa ')
string = ''.join(lista) 

# Sortowanie funkcji sort jest nieintuicyjne bo wykorzystuje standard ASCII
lista = ['A', 'C', 'f', 'a']
lista.sort()
print(lista) #sortuje najpierw duże a potem małe litery
ord('a') #97
ord('A') #65 #najpierw w kolejności jest 'A' a potem 'a'
chr(65) #65-te w kolejnosci jest 'A'
lista.sort(key = str.lower) #sortuje traktując wszystkie litery jak małe
lista.sort(key = str.upper) #sortuje traktując wszystkie litery jak wielkie
print(lista)

# Liczby zmiennoprzecinkowe mogą być niedokładne
0.2*6 # 1.2000000000000002
1.1+1.1+1.1 # 3.3000000000000003
    #Liczby trzeba tłumaczyć na ciąg liczb binarnych - 1 i 0. Błędy zaokrąglenia powodują niewielkie różnice pomiędzy liczbami np 1.2 != 0.2*6
    #Maksymalna wartość liczbowa przechowywana przez pythona to 2^53, wartości powyżej będą równe 2^53
import decimal #pozwala na dokładniejszą prace z liczbami zmiennoprzecinkowymi
liczba = decimal.Decimal(0.2) #niedokładne jak float
liczba_z_tekstu = decimal.Decimal('0.2') #dokładne
liczba*6
liczba_z_tekstu*6

# Operatory nierówności działają nieintuicyjnie - najlepiej używać nawiasy i AND/OR
zmienna1 = 'a'
zmienna2 = 'b'
zmienna3 = 'c'
zmienna1 != zmienna2 != zmienna3 # To jest ok
zmienna1 != zmienna2 != zmienna1 #działa to jak (zmienna1 != zmienna2) AND (zmienna2 != zmienna3)
