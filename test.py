import tkinter, tkinter.messagebox

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
    "a": 10,
    "b": 11,
    "c": 12,
    "d": 13,
    "e": 14,
    "f": 15,
}

def umwandeln_2():
    zahl = input_z.get()
    basis = int(input_b.get())              
    dec = 0
    fail = 0                                   # Variable für Fehlercode

    for i in range(len(zahl)):
        if zahl[i] not in tabelle or tabelle[zahl[i]]>basis-1:        
            fail = 1
            break
        elif basis <= 2 or basis > 16:
            fail = 2
            break
        dec += basis**(len(zahl)-i-1)*(tabelle[zahl[i]])
    if fail == 0:                       # Ausgabe je nach Fehlercode (0 = Ausgabe Ergebnis)
        lbOutput["text"] = str(dec)
    elif fail == 1:
        lbOutput["text"]=("Ungültige Eingabe für Basis " + str(basis))
    elif fail == 2:
        lbOutput["text"]=("Bitte gültige Basis angeben")        


window = tkinter.Tk()
window.title("Umrechner")
window.resizable(bool(0), bool(0))

lbInput = tkinter.Label(window, text="Bitte Zahl eingeben:")
lbInput.grid(row=0, column=0, sticky="w", padx=5, pady=5)

input_z = tkinter.Entry(window, width=30)
input_z.grid(row=1, column=0, sticky="w",padx=5, pady=5)

input_b = tkinter.Entry(window, width=30)
input_b.grid(row=2, column=0, sticky="w",padx=5, pady=5)

ok = tkinter.Button(window, text="GO", command=umwandeln_2, width=10)
ok.grid(row=3, column=0, sticky="w",padx=5, pady=5)

lbOutput = tkinter.Label(window, text="", bg="yellow", width=30)
lbOutput.grid(row=4, column=0, sticky="w", padx=5, pady=5)

window.mainloop()