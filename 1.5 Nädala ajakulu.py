ainepunktide_arv = int(input("Sisestage ainepunktide arv: "))
nadalate_arv = int(input("Sisestage nädalate arv: "))
tunnid = ainepunktide_arv * 26
nadalate_ajakulu = tunnid / nadalate_arv
print(round(nadalate_ajakulu))