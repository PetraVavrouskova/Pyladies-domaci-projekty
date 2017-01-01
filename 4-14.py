pocet_radku = int(input("Zadej pocet radku: "))
pocet_sloupecku = int(input("zadej pocet sloupecku: "))

for cislo_radku in range(pocet_radku):
    for cislo_v_radku in range(pocet_sloupecku):
        if cislo_radku == 0 or cislo_v_radku == 0 or cislo_radku == pocet_radku - 1 or cislo_v_radku == pocet_sloupecku  - 1:
            print("X ", end = "")
        else:
            print("  ", end = "")
    print()
