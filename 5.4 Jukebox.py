failinimi = str(input("Sisestage failinimi: "))
fail = open(failinimi, encoding="UTF-8")

palad = []
loend = 0

for rida in fail:
    loend += 1
    palad.append((rida.strip()))
    print(str(round(loend))+ ". " + rida)


failirida = int(input("Valige järkjekorranumber: "))
print(str(palad[-1 + failirida]))
fail.close