ringide_arv = int(input("Sisesta ringide arv: "))
porgandid_kokku = 0
porgandite_arv_karbis = 0
ring = 1
while ring <= ringide_arv:
    porgandite_arv_karbis = porgandite_arv_karbis + ring
    porgandid_kokku =   porgandid_kokku + porgandite_arv_karbis
    ring = ring + 1
print("Porgandite koguarv on " + str(porgandid_kokku))
