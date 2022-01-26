def banner(lause):
    return lause.upper()

kordamine = int(input("Mitu korda tuleb korrata: "))
reklaamlause = input("Milline on reklaamlause: ")
kord = 1
while kord <= kordamine:
    tulemus = banner(reklaamlause)
    print(tulemus)
    kord = kord + 1
    