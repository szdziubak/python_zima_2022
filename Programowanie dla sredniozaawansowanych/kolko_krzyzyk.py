import sys
pola =[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
gracz_X = 'X'
gracz_O = 'O'
plansza_pusta = f"""
0|1|2
_____
3|4|5
_____
6|7|8
"""
def rysuj_plansze_wypelniana(pola = pola):
    plansza_wypelniona = f"""
    {pola[0]}|{pola[1]}|{pola[2]}
    _____
    {pola[3]}|{pola[4]}|{pola[5]}
    _____
    {pola[6]}|{pola[7]}|{pola[8]}
    """
    return plansza_wypelniona

def sprawdz_rezultaty(pola = pola, gracz_X = gracz_X, gracz_O = gracz_O):
    if pola[0] == pola[1] == pola[2] and pola[0] != ' ':
        znak_zwycieski = pola[0]
    elif pola[3] == pola[4] == pola[5] and pola[3] != ' ':
        znak_zwycieski = pola[3]
    elif pola[6] == pola[7] == pola[8] and pola[6] != ' ':
        znak_zwycieski = pola[6]
    elif pola[0] == pola[4] == pola[8] and pola[0] != ' ':
        znak_zwycieski = pola[0]
    elif pola[2] == pola[4] == pola[6] and pola[2] != ' ':
        znak_zwycieski = pola[2]
    else:
        znak_zwycieski = None
    if znak_zwycieski is not None:
        'gracz_X' if znak_zwycieski == gracz_X else gracz_O
    return znak_zwycieski

def dodaj_ruch(pole, aktualny_gracz = None, pola = pola, gracz_X = gracz_X, gracz_O = gracz_O):
    if aktualny_gracz is None:
        aktualny_gracz = gracz_X
    if pole not in [0,1,2,3,4,5,6,7,8]:
        print("Nieprawidowe pole")
    pola[pole] = aktualny_gracz
    if  aktualny_gracz == gracz_X:
        aktualny_gracz = gracz_O
    else:
        aktualny_gracz = gracz_X
    if ' ' not in pola:
        print("Remis!!!")
        sys.exit()
    print(f"Pora na gracza {aktualny_gracz}")
    return aktualny_gracz, pola

def main(pola = pola, gracz_X = gracz_X, gracz_O = gracz_O, plansza_pusta = plansza_pusta):
    aktualny_gracz = gracz_X
    print(f"""Rozpoczynamy gre w kółko i krzyzyk
    Wpisz QUIT aby zakonczyc gre.
    Plansza z polami wygląda następująco:
    {plansza_pusta}
    Rozpoczyna gracz {aktualny_gracz}""")
    while True:
        pole = input("Wpisz pole na którym chcesz postawić swój znak:   ")
        if pole in ['q', 'Q', 'QUIT', 'quit', 'Quit', 'exit', 'EXIT', 'Exit']:
            print("Zakończono grę. Dziękuje :)")
            sys.exit()
        while pola[int(pole)] in [gracz_X, gracz_O]:
            pole = int(input("Pole zajęte. Wpisz pole na którym chcesz postawić swój znak:   "))
            if pole in ['q', 'Q', 'QUIT', 'quit', 'Quit', 'exit', 'EXIT', 'Exit']:
                print("Zakończono grę. Dziękuje :)")
                sys.exit()
        pole = int(pole)
        # while pola[pole] in [gracz_X, gracz_O]:
        #     pole = int(input("Wpisz pole na którym chcesz postawić swój znak:   "))
        aktualny_gracz, pola = dodaj_ruch(pole = pole, aktualny_gracz = aktualny_gracz, pola = pola, gracz_X = gracz_X, gracz_O = gracz_O)
        plansza_wypelniona = rysuj_plansze_wypelniana(pola = pola)
        print(f"""Plansza po ruchu wygląda następująco:
        {plansza_wypelniona}""")
        #print(pola)
        znak_zwyciezki = sprawdz_rezultaty(pola = pola, gracz_X = gracz_X, gracz_O = gracz_O)
        if znak_zwyciezki is None:
            print("Gramy dalej")
        else:
            print(f"Wygrał gracz {znak_zwyciezki}")
            sys.exit()
        

main()