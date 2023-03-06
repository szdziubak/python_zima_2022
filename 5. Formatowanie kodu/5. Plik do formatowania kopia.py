from random import randint

lista = ['a', "bbb", "ccc"]


def losowanie(n, start, stop):
    lista = []
    for i in range(n):
        element = randint(start, stop)
        lista = [element] + lista
    return lista


def przestaw(lista):
    for i in range(len(lista) - 1):
        if lista[i] > t[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
    return lista


def sortuj(lista):
    for i in range(len(lista)):
        przestaw(lista)
    return lista
