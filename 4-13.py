for cislo_radku in range(6):
    for cislo_v_radku in range(7):
        if (cislo_radku == 0) or (cislo_radku == 5) or (cislo_v_radku == 0) or (cislo_v_radku == 6):
            print("X ", end = "")
        else:
            print("  ", end = "")
    print()
