import random

hraci = [0, 0, 0, 0]
hod_kostkou = 0
for hrac in range(len(hraci)):
    print("Hody hrace cislo ", hrac + 1, ":", sep = "")
    while hod_kostkou != 6:
        hraci[hrac] += 1
        hod_kostkou = random.randint(1,6)
        print(hod_kostkou, end = " ")
    print()
    hod_kostkou = 0

print("Vyhral hrac cislo {}, s poctem hodu {}.".format(hraci.index(max(hraci)) + 1, max(hraci)))
