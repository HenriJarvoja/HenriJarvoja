vanus = int(input("Sisesta oma vanus: "))
sugu = input("Sisesta oma sugu: ")
tingimus = sugu == "N" or sugu == "m"
if sugu == "M" or sugu == "m":
    max_puls_sagedus = 220 - vanus
tingimus = sugu == "N" or sugu == "n"
if sugu == "N" or sugu == "n":
    max_puls_sagedus = 206 - vanus * 0.88
treening = int(input("Sisesta treeningu tüüp: "))
if treening == 1:
    min_puls = 0.5 * max_puls_sagedus
    max_puls = 0.7 * max_puls_sagedus
elif treening == 2:
    min_puls = 0.7 * max_puls_sagedus
    max_puls = 0.8 * max_puls_sagedus
elif treening == 3:
    min_pulss = 0.8 * max_puls_sagedus
    max_pulss = 0.87 * max_puls_sagedus
min_puls = round(min_puls)
max_puls = round(max_puls)
print("pulsisagedus peab olema vahemikus " + str(min_puls) + " ja "  + str(max_puls) + " vahel. ")