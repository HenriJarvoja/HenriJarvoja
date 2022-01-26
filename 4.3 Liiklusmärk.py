from tkinter import *
 
raam = Tk()
raam.title("liiklusmärk 311a")
tahvel = Canvas(raam, width=1000, height = 400)
tahvel.create_oval(250,0,450,200, fill="red", outline="red")
tahvel.create_oval(265,18,438,180, fill="white", outline="white")
tahvel.pack()
raam.mainloop()