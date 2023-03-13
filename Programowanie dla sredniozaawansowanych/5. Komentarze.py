#Komentarz jednowierszowy

# Komentarz wielowierszowy
# nie będący dobrym sposobem 
# na komentowanie

"""Komentarz wielowierszowy (ciąg wielowierszowy)
będący dobrym sposobem na komentowanie
wielu linii"""

print("test") # komentarz inline
print("test") # wyświetl informację testową


# Sumuj wiele elementów = <- komentarz podsumowujący
def suma(*args):
    suma = 0
    if len(args) > 0:
        for arg in args:
            suma += arg
        return suma

# Znaczniki
def funkcja(...): # TODO - oznacza , że trzeba to dokończyć
def funkcja(...): # HACK - działa, ale kod warto poprawić
def funkcja(...): # FIXME - kod trzeba naprawić
def funkcja(...): # XXX - ogólne ostrzeżenie dotyczące kawałka kodu

# Docstringi - komentarze dotyczące funkcji lub klasy. Na ich podstawie tworzona jest dokumentacja

from random import randint
help(randint) #wygenerowane na podstawie komentarzy docstring

def suma(*args):
    """ Funkcja służąca do liczenia sumy wielu elementów.
    Pozwala na zdefiniowanie wielu argumentów po przecinku.
    """
    suma = 0
    if len(args) > 0:
        for arg in args:
            suma += arg
        return suma

help(suma)

import random
help(random) # q zeby wyjsc z opisu

