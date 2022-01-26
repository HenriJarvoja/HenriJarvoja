ringide_arv = int(input("Sisesta ringide arv: "))
porgandid_kokku = 0
for ring in range(1, ringide_arv+1, 1):
    if ring % 2 == 0:
        porgandid_kokku =   porgandid_kokku + ring
print("Porgandite koguarv on " + str(porgandid_kokku))
