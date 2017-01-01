from random import randint
def vyhodnot(pole):
    #Funkce na vyhodnoceni pole, samopopisna
    if ("x" * 3) in pole:
        return "x"
    elif ("o" * 3) in pole:
        return "o"
    elif "-" not in pole:
        return "!"
    else:
        return "-"

def tah(pole, pozice, symbol):
    #Nezabezpecena funkce, ktera jen vraci pole se zaznamenanym tahem
    #Dle zadanych parametru
    return pole[:pozice] + symbol + pole[pozice + 1:]

def tah_hrace(pole, symbol):
    #Zabezpecena funkce na volbu tahu hrace
    if "-" not in pole:
        return pole
        #At se nesnazim hrat do plneho pole
    while True:
        try:
            #Tady se ujistuji, ze vysledny input bude int nebo int :-)
            pozice = int(float(input("Zadej pozici, kam chces hrat: ")))
        except ValueError:
            continue
        if (pozice > len(pole) - 1) or (pozice < 0) or (pole[pozice] != "-"):
            #Ujisteni, ze nebudu hrat mimo pole nebo na jiz hranou pozici
            print("Trochu se snaz a zadej validni pozici!")
            continue
        else:
            return tah(pole, pozice, symbol)

def tah_pocitace(pole, symbol):
    #FUnkce na nahodne generovani volnych pozic
    if "-" not in pole:
        return pole
        #At se nesnazim hrat do plneho pole
    pozice = -1
    #nejslusnejsi reseni, ktere jsem vymyslel, jde to lepe?
    while pole[pozice] != "-" or pozice < 0:
        #Dokud zvolena pozice neni volna, volim dale
        pozice = randint(0,len(pole) - 1)
    return tah(pole, pozice, symbol)

def piskvorky1d():
    #Hlavni herni funkce, ktera vola ostatni funkce, dokud neni rozhodnuto o vitezi
    herni_pole = "-" * 20
    stridaci_prvek = 1
    #vytvoreni hernho pole
    while vyhodnot(herni_pole) == "-":
        #Dokud neni rozhodnuto o vitezi, stridaji se tahy
        if stridaci_prvek % 2 == 1:
            print(herni_pole)
            #Print zde mi zajisti, ze se mi pole bude vypisovat jen
            #Kdyz to bude davat smysl
            herni_pole = tah_hrace(herni_pole, "x")
        else:
            herni_pole = tah_pocitace(herni_pole, "o")
        stridaci_prvek += 1
        #Takhle si zajistim, ze se budou stridat a nikdo nebude hrat do jiz rozhodnute partie
    print("Vysledek: ", vyhodnot(herni_pole))

piskvorky1d()
#Volani hlavni herni funkce...
