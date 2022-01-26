from tkinter import *
raam = Tk()
raam.title("Kuressaare lipp")
tahvel = Canvas(raam, width=600, height = 300)
kõrgus = 100
i = 0
while i < 3:
    if i == 0 or i == 2:
        tahvel.create_rectangle(0, i * kõrgus, 600, (i + 1) * kõrgus, fill="dodgerblue", outline="black")
    else:
        tahvel.create_rectangle(0, i * kõrgus, 600, (i + 1) * kõrgus, fill="white", outline="black")
        tahvel.create_oval(220, i * kõrgus, 350, (i + 1) * kõrgus, fill="yellow", outline="black")
    i += 1
tahvel.pack()
raam.mainloop()
