ekap = int(input("Sisestage EKAPide arv : "))
nädalad = int(input("Sisestage nädalate arv : "))
tunnid = ekap * 26
nädalaajakulu = tunnid / nädalad
print(round(nädalaajakulu))
