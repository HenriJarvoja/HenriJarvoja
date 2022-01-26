def pronksikarva_summa(fail):
    arv = 0
    for münt in fail:
        if int(münt) <= 5:
            arv += int(münt)
    return arv
failinimi = input("Sisesta failinimi: ")
fail = open(failinimi, encoding="UTF-8")
print("Hoiupõrsasse läheb " + str(pronksikarva_summa(fail)) + (" senti."))