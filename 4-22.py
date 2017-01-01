def fakt(cislo):
    #funkce na vypocitani faktorialu, bohuzel s rekurzi,
    #Kdyz se mi bude chtit, casem to prepisu bez rekurze, schvalne, jak to bude vypadat :-)
    if cislo == 1:
        return 1
        #fakt jednicky je samozrejme jednicka
    else:
        return cislo + fakt(cislo - 1)
        #TO je snad samopopisne, ne?

def prvok(cislo):
    #Overeni toho, ze je cislo prvocislo
    #jiste existuje cistsi zpusob, ale toto bylo krasne jednoduche
    for i in range(2, cislo):
        #Pro vsechny cisla od dvojky do cisla-1 zkusim,
        #Jestli zbytek po deleni bude nula
        #Pokud se najde nenulovy vysledek, cyklus konci
        if cislo % i == 0:
            return False
    return True

def fib(cislo):
    #Tahle prasarnicka potrebuje trochu vysvetleni
    cleny = [0, 0, 1]
    #Taakze - na zacatku si nadefinuji seznam o trech clenech, 0,0,1
    if cislo == 0:
        return "Nulte misto? Kde to jsme, v Pythonu?"
    elif cislo == 1:
        print("0")
    else:
        for i in range(1, cislo+1):
            if i == 1:
                print("0 ", end = "")
            if i == 2:
                print("1 ", end = "")
            if i > 2 :
                print(sum(cleny) - min(cleny), "", end = "")
                #A potom pokazde vytisknou sumu hodnot v seznamu, minus prvni nejmensi hodotu
                cleny[cleny.index(min(cleny))] = sum(cleny) - min(cleny)
                #nasledne prvni nejmensi hodnotu nahradim souctem dvou vyssich hodnotu
                #Krasne :-)
def fib2(cislo):
    #cistsi verze, vraci seznam fib cisel az do "cislo"
    a = 0
    b = 1
    cleny = []
    #zalozim si prazdny seznam na cleny
    if cislo > 0:
        cleny.append(0)
    if cislo > 1:
        cleny.append(1)
    if cislo > 1:
        for i in range(1, cislo + 1):
            cleny.append(a + b)
            a, b = b, a + b
            #Tento krasny zapis udela to, ze do a ulozi b a do b ulozi a+b - nadhera
    return cleny

zjistovane_cislo = int(input("Zadej cislo, jehoz faktorial touzis mit: "))
print("Vytouzeny faktorial jest ", fakt(zjistovane_cislo))
print("Je {} prvocislo? Odpoved zni - {}".format(zjistovane_cislo, prvok(zjistovane_cislo)))
print("Prvnich {} pozic Fibonaciho posloupnosti jest:".format(zjistovane_cislo))
fib(zjistovane_cislo)
print()
print(fib2(zjistovane_cislo))
