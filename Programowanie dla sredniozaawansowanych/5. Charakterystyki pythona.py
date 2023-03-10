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


# Sortowanie funkcji sort jest nieintuicyjne bo wykorzystuje standard ASCII

# Liczby zmiennoprzecinkowe mogą być niedokładne

# Operatory nierówności działają nieintuicyjnie

