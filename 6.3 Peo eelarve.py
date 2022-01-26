def budget(külalised):
    budget1 = külalised * 10 + 55
    return (budget1)

inv = []

filename = input("Failinimi: ")

for row in filename:
    inv.append(row)
print(inv)
print(len(inv))

kindlad_külalised = 0
for inimene in inv:
    if inimene[0] == '+':
        kindlad_külalised += 1
        
print(kindlad_külalised)

kutsutud = int(len(inv))
tuleb = int(kindlad_külalised)

print("Maksimaalne eelarve on: ")
