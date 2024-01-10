tabelle = {
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

def umwandeln_2(zahl, basis):
    zahl = zahl.upper()                 # Eingabe zu uppercase
    dec = 0
    fail = 0                            # Variable für Fehlercode
    
    for i in range(len(zahl)):
        if zahl[i] not in tabelle:        
            fail = 3
        elif tabelle[zahl[i]]>basis-1:
            fail = 3
            break
        dec += basis**(len(zahl)-i-1)*(tabelle[zahl[i]])
    if fail == 0:                       # Ausgabe je nach Fehlercode (0 = Ausgabe Ergebnis)
        print(dec)
    else:
        print("Ungültige Eingabe für Basis " + str(basis))

umwandeln_2("28ff", 16)
umwandeln_2("10110110", 2)
umwandeln_2("100121", 2)
umwandeln_2("12212", 3)
umwandeln_2("823", 8)
print(int("FF06", 16))