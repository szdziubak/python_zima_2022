#Programowanie funkcyjne

#Funkcja lambda - funkcje anonimowe, nie musi być powiązana ze zmienną

def pole_prostokata(a,b):
    return a*b
pole_prostokata(5,3)
pole_prostokata.__name__ #nazwa funkcji

pole_prostokata_lambda = lambda a,b: a*b
pole_prostokata_lambda(5,3)
pole_prostokata_lambda.__name__ #brak nazwy funkcji

#Funkcja map
map_results = map(lambda a,b: a*b, range(3,5), [1,2])
list(map_results)

#Funkcja filter
lista = [1,2,3,5,7,10,11,17,19]
list(filter(lambda _: _%2 == 0, lista))

#Reduce - sprowadza obiekty do jednej wartości
from functools import reduce

from pyrsistent import b
reduce(lambda a,b: a*b, range(1,15,3))

#Funkcje częściowe - pozwalają na utworzenie nowej funkcji bazując na innej z predefiniowanymi argumentami
from functools import partial
pow(2, exp = 3)
potega_3 = partial(pow,3)
potega_3(2)

#Generatory - zwracają sekwencje elementów
def ciag_fibonacciego():
    x,y = 0,1
    while 1 == 1:
        yield y
        x,y = y, x+y
fibonacci = ciag_fibonacciego()
next(fibonacci) #next pobiera następny element generatora

wyrazenie_generatora = (i for i in fibonacci)
for i in wyrazenie_generatora:
    print(i)
