"""
Tworzenie pustego repozytorium bazując na template.
Cookiecutter to narzedzie służące do tworzenia repozytoriów.
"""
pip install cookiecutter
cd "Programowanie dla sredniozaawansowanych\git"

cookiecutter https://github.com/audreyfeldroy/cookiecutter-pypackage #tworzy nowy projekt bazując na podanym template

"""
Git - narzędzie do kontroli wersji.
Pliki mogą być śledzone (tracked) lub nie (untracked).
Pliki śledzone mogą mieć status:
- staged - zmodyfikowany, czeka aby być commited (czeka w poczekalni)
- modified - plik różni się od tego w stanie commited
- commited - plik zapisany (zatwierdzony)
"""

mkdir python_project_git
cd python_project_git

git init # inicjalizacja repozytorium, tworzy plik .git zawierajacy metadane repozytorium
git status # sprawdza ststus plików (zmian)

echo "test readme" > readme.md # tworzymy nowy plik
git add . # dodajemy wszystkie pliki do śledzenia
git add readme.md #dodajemy tylko ten 1 plik do śledzenia
git status
git commit -m "Dodano plik readme" # zatwierdzenie zmian
git status

echo "print('Nowy plik')" > test.py
git status
git add test.py
git status
git commit -m "Dodano plik pythona" test.py # -a pozwala na dodanie konkretnego pliku i commit (git add i commit w jednym)
git status

echo "print('Nadpisany plik')" > test.py
git diff #wyświetla zmiany pomiędzy obecną kopią roboczą a najnowszym commicie

echo "plik do usunięcia" > delete.py # tworzymy plik do usunięcia
git add delete.py # dodajemy plik do śledzenia
git commit -m "Dodajemy plik, który następnie usuniemy" delete.py
git status
git rm delete.py #usuwamy plik z kopii roboczej
git commit -m "Zatwierdzamy usunięcie pliku delete.py" delete.py

echo "print('Nowy plik')" > test.py
mkdir nowy_folder
git mv test.py nowy_folder/test_2.py # przenosimy i zmienioamy nazwe pliku
git status
git commit -m "Zmieniono lokalizacje i nazwe pliku" nowy_folder/test_2.py

git log # wyswietlanie logów
git log --oneline -n 3 # oneline - 1 commit jedna linia, -n 3 - 3 ostatnie commity

echo "print('Nowy plik zmieniony')" > test.py
git status
git restore test.py #cofa niezatwierdzone zmiany
git status

echo "print('Nowy plik zmieniony')" > test_staged.py
git add test_staged.py
git status
git restore --staged test_staged.py #usuwamy z poczekalni (ze sledzenia, cofamy git add)
git status

echo "print('Nowy plik zmieniony')" > test_staged.py
git add .
git commit -m "Kolejny commit"
git log --oneline
git status
git revert -n HEAD
git status
git add .
git commit -m "Cofniety 1 commit"

# cofniecie do konkretnego commita
git show 394118a # wyswietla zawartosc commita
git show 394118a:readme.md # wyswietla zawartosc plikow w tym commicie

git checkout e5d65c3 #cofamy HEAD do danego commita
git checkout e5d65c3:readme.md # bierzemy plik z danego commita
git add .
git commit -m "Cofnięto do commita e5d65c3"

git push https://github.com/szdziubak/... # wysłanie do remote repo

