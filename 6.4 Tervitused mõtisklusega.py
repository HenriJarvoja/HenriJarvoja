def tervitus(arv):
    print(<"Võõrustaja: \"tere!\"")
    print("Täna" + (arv) "kord tervitada, mõtiskleb võõrustaja. ")
    print("Külaline: \"Tere, suur tänu kutse eest!\"")
    
külalistearv = int(input("Külaliste arv: "))

kord = 1
while kord <= külalistearv:
    tervitus(kord)
    kord = kord + 1