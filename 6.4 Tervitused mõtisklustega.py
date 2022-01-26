def tervitus(jk):
    print("võõrustaja: " + "Tere! " + "täna "+ str(jk) +".kord tervitada, mõtiskleb võõrustaja" + "Külaline: Tere, suur tänu kutse eest!" + "Võõrustaja: Tere!" )

külaliste_arv = int(input("Sisestage külaliste arv: "))

for jk in range(1, külaliste_arv+1, 1):
    tervitus(jk)
    

    
