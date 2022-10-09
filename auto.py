def utworz_auto_kwargs(marka, model, rok_produkcji, **info_auto):
    """Tworzy auto ze zdefiniowanym wposażeniem jako słowa kluczowe"""
    info_auto['marka'] = marka
    info_auto['model'] = model
    info_auto['rok_produkcji'] = rok_produkcji
    print(f"Utworzono auto {marka} {model} wyprodukowane w {rok_produkcji} roku")
    print("Inne informacje znajdują się w słowniku info_auto:")
    print(info_auto)


def utworz_auto_args(marka, model, rok_produkcji, *wyposażenie):
    """Tworzy auto ze zdefiniowanym wposażeniem jako argumenty pozycyjne"""
    print(f"Utworzono auto {marka} {model} wyprodukowane w {rok_produkcji} roku")
    print("Wyposażenie auta:")
    for element in wyposażenie:
        print(f"\t-{element}")
