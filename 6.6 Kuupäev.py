def kuu(jarjekord):
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    return kuud[int(jarjekord) - 1]
def kuupäev_sõnena(kuupäev):
    kuupaevad = kuupäev.split(".")
    kuupaev = kuupaevad[0] + ". " + kuu(int(kuupaevad[1])) + " " + kuupaevad[2] + ". a"
    return kuupaev

kuupäev = input("Sisesta kuupäev kujul DD.MM.YYYY: ")
print(kuupäev_sõnena(kuupäev))