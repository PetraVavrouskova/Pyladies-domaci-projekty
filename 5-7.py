text_pisne = "Můj čas, je pouhopouhé prozatím, můj čas, může říct já už neplatím. Rád, tak rád bych žil a mám jen zbytek sil, a času míň, než se mi zdálo před půl hodinou Příteli chvátej SOS, ať jsem i zítra čím jsem dnes, zbav mě tíhy mé rány mé co nejdřív, příteli chvátej píšu vzkaz, dej mi co ztrácim dej mi čas, vrať mi víru mou, lásku mou a té nejvíc. Z vlastního spánku můžeš krást jen času svého dej mi část, boj s časem toužím tentokrát neprohrát. Můj čas, to jsou jen chvílky takové, můj čas, se ocit v tísni časové. Rád bych zůstal živ, chci dýchat jako dřív, a čekám dál, že přece ustrneš se nade mnou.  Příteli chvátej SOS, ať jsem i zítra čím jsem dnes, zbav mě tísně mé, strasti mé co nejdřív. Příteli chvátej píšu vzkaz, dej mi co ztrácim dej mi čas, vrať mi víru mou, lásku mou, a té nejvíc. Z vlastního spánku můžeš krást jen času svého dej mi část, společně můžem tentokrát neprohrát. Až budeš příště v tísni sám, kus času svého já ti dám, a pomoc tvou ti zítra tím, oplatím ...."

count = 0

for znak in text_pisne:
    if znak == "k" or znak == "K":
        count += 1

print("V textu jest {} pismenek \"k\".".format(count))
