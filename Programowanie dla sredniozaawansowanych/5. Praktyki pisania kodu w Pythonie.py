#Używanie enumerate()
metale = ['stal', 'srebro', 'miedz']
for i, metal in enumerate(metale):
    print(f'{i}. {metal}')
    #Zamiast:
for i in range(len(metale)):
    print(f'{i}. {metale[i]}')

#używanie bloków with - block with automatycznie zamyka otworzony plik bez potrzeby uzywania funkcji close()
from pathlib import Path
import os
path_cwd = Path.cwd()
with open(os.path.join(path_cwd,path_cwd,'6. Pliki\liczba_pi.txt'), 'r') as file:
    a = file.read()
print(a)

#wartość None - wartość pusta
a = None
a == "None" # False - a jest wartością None a nie tekstem
a is None # True
a is not None #False

# Formatowanie testów - najlepszym sposobem jest użycie f-string ale inne są również dostępne
zm1 = 1
zm2 = 2

tekst_f_string = f"Zmienna 1 to {zm1} a zmienna 2 to {zm2}"
print(tekst_f_string)

tekst_operator_plus = "Zmienna 1 to " +str(zm1) + " a zmienna 2 to " + str(zm2)
print(tekst_operator_plus)

tekst_operator_konwersji_procent_s = "Zmienna 1 to %s a zmienna 2 to %s"%(zm1, zm2)
print(tekst_operator_konwersji_procent_s)

tekst_format = "Zmienna 1 to {0} a zmienna 2 to {1}".format(zm1, zm2)
print(tekst_format)

# Kopiowanie obiektów
import copy
metale = ['stal', 'srebro', 'platyna', 'miedz', 'aluminium', 'ołów']
metale_do_skupu = metale # referencja do listy
metale_do_skupu_2 = metale[:] # kopia płytka
metale_do_skupu_3 = copy.copy(metale) #kopia płytka - inny sposób
metale[-1] = "lit"
print(metale, metale_do_skupu, metale_do_skupu_2, metale_do_skupu_3)

# Słowniki
auta_marki = {'Audi':'Niemcy', 'Toyota':'Japonia', 'Ferrari':'Włochy'}
print(f'Citroen pochodzi z '+auta_marki.get('Citroen', 'inne'))
auta_marki.setdefault('Citroen','inne') #jeżeli nie istnieje dodaj do słownika
auta_marki.setdefault('Toyota','inne') #jeżeli istnieje nie zmieniaj w słowniku
print(auta_marki)

# Słowniki zamiast if-ów
auta = {'Audi':'Niemcy', 'Toyota':'Japonia', 'Ferrari':'Włochy'}
auta.get('Audi', 'inne')
#Zamiast:
auto = 'Audi'
if auto == 'Audi': 
    kraj_pochodzenia = 'Niemcy'
elif auto == 'Toyota': 
    kraj_pochodzenia = 'Japonia'
elif auto == 'Ferrari': 
    kraj_pochodzenia = 'Włochy'
else: 
    kraj_pochodzenia = 'inne'
print(kraj_pochodzenia)

#wyrażenia warunkowe / trójargumentowe wyrażenia wyboru 
#standardowo wygląda to tak
if auto == 'Audi': 
    kraj_pochodzenia = 'Niemcy'
elif auto == 'Toyota': 
    kraj_pochodzenia = 'Japonia'
elif auto == 'Ferrari': 
    kraj_pochodzenia = 'Włochy'
else: 
    kraj_pochodzenia = 'inne'
#tak to może wyglądać (ale tego unikamy)
'Niemcy' if auto == 'Audi' else 'Japonia' if auto == 'Toyota' else 'Włochy' if auto == 'Ferrari' else 'inne'

#porównania
a = 18
b = 24
a < 20 < b #sprawdzamy 2 nierówności równocześnie

2-1 == 3-2 == 4-3 == 1 #porównujemy wiele napisów ze sobą 

a = 'aaa'
a in ('aaa', 'bbb', 'ccc') #sprawdzamy jednocześnie wiele opcji