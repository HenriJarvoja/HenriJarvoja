sisseränne = open("sisseränne.txt" , encoding="UTF-8")
väljaränne = open("väljaränne.txt" , encoding="UTF-8")
sisse = []
välja = []
loend = 0
for rida in väljaränne:
    välja.append(int(rida))
for rida2 in sisseränne:
    sisse.append(int(rida2))

sisseränne.close()
väljaränne.close()

for i in range(len(sisse)):
    sisse[i] = sisse[i] - välja[i]
print(sisse)
