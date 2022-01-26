inimeste_arv = int(input("Sisestage inimeste arv: "))
kohtade_arv = int(input("Sisestage kohtade arv ühes bussis: ")) 
busside_arv = inimeste_arv // kohtade_arv
mahajaanud = inimeste_arv % kohtade_arv
if mahajaanud > 0:
    busside_arv = busside_arv + 1
print("Tuleb tellida " + str(busside_arv) + " bussi.")