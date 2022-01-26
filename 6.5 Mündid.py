def pronksikarva_summa(järjend):
    summa = 0
    for element in järjend:
        if element == 1 or element == 2 or element ==5:
            summa = summa + element
            return summa
failinimi=input("Sisestage faili nimi")

faili = open(failinimi)
mündid = []
for row in fail:
    mündi.append(int(row))
    
fail.close()

print(pronksikarva_summa(mündid))
print ("Hoiupõrsasse läheb " str(summa) + )