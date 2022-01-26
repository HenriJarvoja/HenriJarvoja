fail = open("konto.txt", encoding="UTF-8")

vastuvõetud = []
kokku = 0

for rida in fail:
    vastuvõetud.append(float(rida))
fail.close()

for element in vastuvõetud:
    if element > 0:
        print(element)
