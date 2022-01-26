from tkinter import *
 
raam = Tk()
raam.title("maja")
tahvel = Canvas(raam, width=1000, height = 600)
tahvel.create_rectangle(250,100,450,300, fill="grey", outline="black")
tahvel.create_rectangle(390,200,440,300, fill="white", outline="black")
tahvel.create_rectangle(360,200,310,250, fill="skyblue", outline="black")
tahvel.create_rectangle(220,90,482,120, fill="red", outline="black")
tahvel.create_rectangle(260,72,450,120, fill="red", outline="black")
tahvel.create_rectangle(260,30,300,120, fill="black", outline="black")
tahvel.pack()
raam.mainloop()