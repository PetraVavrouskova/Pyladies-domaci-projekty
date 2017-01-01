#strana_krychle = 2852

def povrch_krychle(strana):
    return 6*strana**2

def objem_krychle(strana):
    return strana**3

while True:
    try:
        strana_krychle = int(float(input("Zadej delku strany krychle: ")))
    except ValueError:
        continue
    else:
        break

print("S = {} \nV = {}".format(povrch_krychle(strana_krychle), objem_krychle(strana_krychle)))
