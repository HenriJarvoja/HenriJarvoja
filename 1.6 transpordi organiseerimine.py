inimestearv = int(input("sisesta inimeste arv"))
kohtadearv = int(input("sisesta kohtade arv ühes bussis"))
bussid = inimestearv // kohtadearv
mahajaanud = inimestearv % kohtadearv
if mahajaanud > 0:
    bussid = bussid + 1
print("Tuleb tellida " + str(bussid) + " bussi.")
