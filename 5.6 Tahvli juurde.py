from datetime import *

failinimi = str(input("Sisestage failinimi: "))
fail = open(failinimi, encoding="UTF-8")

õpilased = []
for rida in fail:
    õpilased.append((rida.strip()))
fail.close()

kuupaev = datetime.now().day

print(str("täna tuleb vastama: " + õpilased[kuupaev - 1]))

