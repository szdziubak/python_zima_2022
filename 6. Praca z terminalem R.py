#praca z terminalem
from calendar import c
from pathlib import Path
import os
from re import S
Path('C:\\') / 'Users' / 'Szymon' #tworzenie ścierzek w pythonie
Path.home() #katalog domowy
Path.cwd() #current working directory
os.chdir(Path.home()) #zmiana cwd
exit() #wyjście z wiersza polecen pythona
python3.10 -c "print('program wykonany z konsoli')"
python3.10 -c "import sys;print(sys.version)"
history #historia wykonywanych poleceń powłoki
ls *.sh #wyświetlanie wszystkich programów z rozszerzeniem .sh
ls ???.* #wyświetlanie wszystkich programów z 3-znakową nazwą (? - dowolny 1 znak, * - dowolny ciąg znaków)
cd C:\Users #zmiana ścieżki
cd admin #przejście do konkretnego folderu niżej
cd ./Desktop #jak wyżej, . oznacza obecny folder
cd .. #przejście 1 folder wyżej
ls -s #lista plików z podfolderami

echo "jakiś tekst" > plik.txt #utwórzmy plik tekstowy
mkdir folder_testowy #tworzymy nowy folder
cp plik.txt folder_testowy #kopiujemy plik do folderu folder_testowy
ls folder_testowy 
del folder_testowy/plik.txt #usuwamy skopiowany plik
ls folder_testowy
mv plik.txt folder_testowy #przenosimy (nie kopiujemy) plik
mv folder_testowy/plik.txt folder_testowy/plik_testowy.txt #zmieniamy nazwe pliku
del folder_testowy #usuwa folder testowy z zawartością (bez podfolderów)
mkdir folder_testowy #tworzy folder 
mkdir folder_testowy/podfolder ; echo "jakiś tekst" > folder_testowy/plik.txt ; cp folder_testowy/plik.txt folder_testowy/podfolder #wiele polecen w jednej linii
cls #czyści terminal

