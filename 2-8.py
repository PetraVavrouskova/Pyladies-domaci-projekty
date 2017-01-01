import random


seznam_tahu = ["kamen", "nuzky", "papir"]

tah_pocitace = random.choice(seznam_tahu)
tah_hrace = random.choice(seznam_tahu)

print("Tah pocitace: {} \nTah hrace: {}".format(tah_pocitace, tah_hrace))

if tah_pocitace == tah_hrace:
    print("pluchta")
elif (tah_pocitace == "kamen" and tah_hrace == "papir") or (tah_pocitace == "nuzky" and tah_hrace == "kamen") or (tah_pocitace == "papir" and tah_hrace == "nuzky"):
    print("Hrac vyhral!")
elif (tah_pocitace == "kamen" and tah_hrace == "nuzky") or (tah_pocitace == "nuzky" and tah_hrace == "papir") or (tah_pocitace == "papir" and tah_hrace == "kamen"):
    print("Pocitac vyhral!")
