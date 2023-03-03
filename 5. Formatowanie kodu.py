# Zasady formatowania kodu opisane są w dokumencie PEP8 (https://peps.python.org/pep-0008/)
# Oto kilka z nich:
# Zamiana \t na 4 lub 8 spacji
# spacje pomiędzy obiektami: a = b + c (NIE: a=b+c)
# spacje po separatorach: lista = [a, b, c] (NIE: lista = [a, b ,c ])
# brak spacji między atrybutem/nazwą zmiennej: 'tekst'.title() (NIE: 'tekst . title())
# puste linie pomiędzy wierszami kodu:
# def f1():
#     ...
#
# def f2():
#     ... 
# ZAMIAST:
# def f1():
#     ...
# def f2():
#     ...
#Nie za dużo znaków w linii:
#if a == 'y':
#    print('Tak')
#ZAMIAST:
#if a == 'y': print('Tak')

# Black to narzędzie do formatowania kodu
python -m pip install black # m oznacza wywołanie pip (albo innej formuły) jak aplikacji
python -m black "python_zima_2022\\5. Plik do formatowania kopia.py"# tu wywołujemy black jak aplikacje
python -m black -l 20 "python_zima_2022\\5. Plik do formatowania kopia.py" #-l to maksymalna dlugosc linii
del "python_zima_2022\\5. Plik do formatowania kopia.py"; cp "python_zima_2022\\5. Plik do formatowania.py" "python_zima_2022\\5. Plik do formatowania kopia.py"
python -m black -l 80 -S "python_zima_2022\\5. Plik do formatowania kopia.py" #-S oznacza nieformatowanie apostrofów/znaków cytowania 
del "python_zima_2022\\5. Plik do formatowania kopia.py"; cp "python_zima_2022\\5. Plik do formatowania.py" "python_zima_2022\\5. Plik do formatowania kopia.py"
python -m black -l 80 --diff "python_zima_2022\\5. Plik do formatowania kopia.py" #--diff pokazuje zmiany które może dokonać
python -m black -l 30 "python_zima_2022\\5. Plik do formatowania częsciowego kopia.py" # dzięki fmt:on i fmt:off zformatowano część pliku 