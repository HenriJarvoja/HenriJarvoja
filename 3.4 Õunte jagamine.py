from random import randint
pöialpoiste_arv = int(input("Sisesta pöialpoiste arv kes soovivad õunu: "))
lumivalgekese_õunad = 14
i = 1
while i <= pöialpoiste_arv:
    õunade_arv = randint(1, 2)
    print(str(õunade_arv))
    lumivalgekese_õunad = lumivalgekese_õunad - õunade_arv
    i = i + 1
print("lumivalgekesele jäi " + str(lumivalgekese_õunad)  + " õuna. ")