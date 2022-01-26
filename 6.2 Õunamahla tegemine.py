def mahlapakkide_arv(õunad):
    return õunad.upper()

õunad = int(input("Mitu kilogrammi on õunu: "))
mahlapakkide_arv = õunad*0,4/3
pakkide_arv = 1
while pakkide_arv <= õunad:
    tulemus = mahlapakkide_arv
    print(tulemus)
    pakkide_arv = pakkide_arv + 1
    

