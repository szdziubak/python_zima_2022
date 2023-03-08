#Moduł collections
#Pozwala na prace z kontenerami - obiektami takimi jak krotki, listy, słowniki

# Counter - zlicza ilość wystąpień
from collections import Counter
Counter(['a', 'b', 'c', 'a', 'a', 'c', 'a', 'b', 'c', 'a', 'a', 'c'])
Counter({'a':1, 'b':3, 'c':'2'})

#DefaultDict - dostawia jakąś wartość dla nieistniejącego klucza, aby nie zwrócić błędy KeyError
from collections import defaultdict 
dictionary  = defaultdict(str)
dictionary['a'] = 'aaa'
dictionary['b'] = 'bbb'
dictionary['c']

def default_value():
    return "Nie istnieje"

dictionary2  = defaultdict(default_value)
dictionary2['d']

#ChainMap -powiązane kolekcje słowników
from collections import ChainMap
dict1 = {'imie':'Jan', 'nazwisko':'Kowalski'}
dict2 = {'wiek':39, 'wzrost':182}
dict_full = ChainMap(dict1, dict2)
dict_full

#NamedTuple - pozwala na nadawanie nazw elementom krotki
from collections import namedtuple
Auto = namedtuple("Auto", ['marka', 'model', 'rocznik'])
a = Auto("Audi", "S6", 2017)
a.marka
a.rocznik
  #konwersja ze słownika
d_auta = {'marka':'Audi', 'model':'S6', 'rocznik':2017}
print(Auto._make(d_auta))

#Deque - lista zoptymalizowana pod kątem dodawania i usuwania elementów
from collections import deque
queue = deque(['aaa', 'bbb', 'ccc'])
print(queue)
queue.append('ddd') #dodanie elementów z prawej
queue.appendleft('zzz') #dodanie elementów z lewej
print(queue)
queue.pop() #usuwanie jednego z prawej
queue.popleft() #usuwanie jednego z lewej
print(queue)

#UserDict, UserList, UserString - kontener pozwalajcy na tworzenie wlasnych obiektow ze zmienioną funkcjonalnością
from collections import UserDict , UserList, UserString

class NowySlownik(UserDict):
    def iterate(self, s):
        for k,v in s.items(): print(f'klucz {k} ma wartość {v}')

slownik = NowySlownik({'1122':'aaa', '1133':'bbb'})
slownik.iterate(slownik)

class NowaLista(UserList):
    def remove(self, s = None):
        raise RuntimeError("Nie można usuwać elementów z listy")
lista = NowaLista([1,2,3,4,5,6])
lista.remove(3)
lista2 = [1,2,3,4,5,6]
lista2.remove(3)
lista2

class NowyTekst(UserString):
    def delimite(self, s, delimiter = ' '):
        return s.split(delimiter)
tekst = NowyTekst('Jakiś testowy tekst')
tekst.delimite(tekst, ' ')

#defaultdict - tworzenie słownika z wartościami domyślnymi
from collections import defaultdict
auta = defaultdict(str)
auta['Renault'] #nie istnieje więc wyświetla pusty ciąg tekstowy
auta['Citroen'] = 'Francja'
print(auta)