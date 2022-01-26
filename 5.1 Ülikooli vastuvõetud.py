aasta = int(input("Sisesta millise aasta andmeid vajate: "))

fail = open("rebased.txt", encoding="UTF-8")

vastuvõetud = []

for rida in fail:
    vastuvõetud.append(int(rida))
fail.close()


#print(vastuvõetud)

print (str(aasta) + " aastal oli vastu võetuid " + str(vastuvõetud[aasta - 2011]))