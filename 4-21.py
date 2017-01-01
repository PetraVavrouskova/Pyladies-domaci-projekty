for cislo in range(101):
    if cislo % 3 == 0 and cislo % 5 == 0:
        print("bum-bac")
    elif cislo % 3 == 0:
        print("bum")
    elif cislo % 5 == 0:
        print("bac")
    else:
        print(cislo)
