hex_tabelle = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
}
bin_tabelle = {
    "0": 0,
    "1": 1,
}

def umwandeln_2(zahl, basis):
    zahl = zahl.upper()                 # Eingabe zu uppercase
    dec = 0
    fail = 0                            # Variable für Fehlercode
    if basis == 2:                      # Wahl des passenden dictionaries
        tab = bin_tabelle
    elif basis == 16:
        tab = hex_tabelle
    elif basis == 8:
        tab = oct_tabelle
    else: fail = 1                      # Fehlercode 1 = keine Tabelle für Basis -> break
    for i in range(len(zahl)):
        if fail == 1:                   
            break
        elif zahl[i] not in tab:        # Fehlercode 2 = Zeichen nicht in Tabelle enthalten -> break
            fail = 2
            break
        dec += basis**(len(zahl)-i-1)*(tab[zahl[i]])
    if fail == 0:                       # Ausgabe je nach Fehlercode (0 = Ausgabe Ergebnis)
        print(dec)
    elif fail == 1:
        print("Basis " + str(basis) + " wird nicht unterstützt")
    else:
        print("Ungültige Zahl für Basis " + str(basis))

umwandeln_2("28ff", 16)
umwandeln_2("10110110", 2)
umwandeln_2("100121", 2)
umwandeln_2("12212", 3)
umwandeln_2("823", 8)