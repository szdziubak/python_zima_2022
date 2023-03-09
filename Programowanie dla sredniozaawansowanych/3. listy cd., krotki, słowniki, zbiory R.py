#Więcej można przeczytać tutaj: Profesjonalne programowanie w Pythonie. Poznaj najlepsze praktyki kodowania i zaawansowane koncepcje programowania. Wydanie IV
# łączenie zmiennych tego samego typu
[1,2,3] + [4,5,6] 
(1,2,3) + (4,5,6)

lista = ['a', 'b', 'c']
lista += ['d', 'e', 'f']
lista

zbior1 = {'a', 'b', 'c', 'd', 'e'}
zbior2 = {'d', 'e', 'f', 'g'}
zbior1 & zbior2 # & to część wspólna zbiorów
zbior1 | zbior2 # | to suma zbiorów
zbior1 - zbior2 # - to różnica zbiorów
zbior1 ^ zbior2 # ^ to zbiór A i B bez części wspólnej

slownik1 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5} 
slownik2 = {'e':5, 'f':6, 'g':7}
slownik1 | slownik2 #od 3.10, suma słowników
slownik1 |= slownik2 #modyfikacja słownika1 o słownik2 - suma
slownik1.update(slownik2) #starszy sposób modyfikacji
{**slownik1, **slownik2} #rozpakowywanie słownika - inna metoda na modyfikacje

from collections import ChainMap
slownik3 = ChainMap(slownik1, slownik2)
print(slownik3)
slownik3['g']
slownik2['g'] = 8
slownik3['g'] #ChainMap tworzy powiązane słowniki

#Typy generyczne - definiowane są typy danych które powinny być użyte w funkcjach
from typing import Any
def calculate_new_price(products: dict, increase: int) -> Any: #products powinien byc slownikiem, increase liczbą a funkcja może zwracać cokolwiek
    for k,v in products.items():
        products[k] = v*(1+increase)
    return products

print(calculate_new_price({'smartphone':1000, 'notebook':3500}, 0.1))
print(calculate_new_price([100,200], 0.1))

#Parametry pozycyjne
def stock_info(name: str, exchange: str, ticker:str, dividend:int):
    info = f'{name.upper()} is listed on {exchange} with ticker {ticker}. Dividend yield is around {str(dividend*100)} %.'
    print(info)
    return 'Status: completed'

stock_info('International Business Machines Corporation', 'NYSE', 'IBM', 0.049)
stock_info(name = 'International Business Machines Corporation', dividend = 0.049, exchange = 'NYSE', ticker = 'IBM')


def stock_info(name: str, exchange: str, /, *, ticker:str, dividend:int): #wszystkie parametry przed / są pozycyjne, po * muszą być definiowane za pomocą nazw 
    info = f'{name.upper()} is listed on {exchange} with ticker {ticker}. Dividend yield is around {str(dividend*100)} %.'
    print(info)
    return 'Status: completed'

stock_info('International Business Machines Corporation', 'NYSE', 'IBM', 0.049) #błąd
stock_info('International Business Machines Corporation', 'NYSE', ticker = 'IBM', dividend = 0.049) #poprawne wywołanie


#Liczby - podkreślenia
100000 == 100_000
100 == 1_0_0

#moduł secrets - najlepsze żródło losowości (https://docs.python.org/3/library/secrets.html)
#moduł random nie zapewnia losowości
import secrets
secrets.token_bytes(nbytes = 5) #zwraca ileś losowych bajtów
secrets.choice(seq = 'abcdefghijklmnoprstuwxyz') #zwraca losowy znak z sekwencji
secrets.randbelow(10) #zwraca losową cyfre od 0 do 9

#instrukcja dopasowywania - case match
i = 0
while i<20:
    match i%2:
        case 0:
            print(f"{i} jest podzielne przez 2")
        case other:
            print(f"{i} nie jest podzielne ani przez 2")
    i += 1

i = 0
while i<20:
    match (i%2, i%3, i%5):
        case (0, _, _): #_ oznacza dowolny znak
            print(f"{i} jest podzielne przez 2")
        case (0, 0, _):
            print(f"{i} jest podzielne przez 2 i 3")
        case (0, 0, 0):
            print(f"{i} jest podzielne przez 2, 3 i 5")
        case (_, 0, _):
            print(f"{i} jest podzielne przez 3")
        case (_, 0, 0):
            print(f"{i} jest podzielne przez 3 i 5")
        case (_, _, 0):
            print(f"{i} jest podzielne przez 5")
        case other:
            print(f"{i} nie jest podzielne przez ani 2, 3 i 5")
    i += 1

