def banner(lause):
    return lause.upper()

bannerlause = str(input("Sisestage reklaamlause: "))
kordamine = int(input("Sisestage mitu korda soovite reklaamlauset kuulda: "))
for i in range(kordamine):
    print(banner(bannerlause))
