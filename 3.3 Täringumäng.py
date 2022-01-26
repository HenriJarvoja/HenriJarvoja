from random import randint
täringute_arv = int(input("Sisesta täringute arv: "))
i = 1
while i <= täringute_arv:
    täringute_arvud = randint(1, 6)
    print(str(täringute_arvud))
    i = i + 1
