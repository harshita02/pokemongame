#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 19:03:29 2022

@author: ishitasmacbook
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 06:43:51 2022

@author: ishitasmacbook
"""
from tkinter import *

import random

from PIL import Image, ImageTk

root = Tk()

root.title("ENDLESS POKEMON CARD GAME")
root.geometry("800x600")

root.configure(background = "pink")
pikachu = ImageTk.PhotoImage(Image.open("pikachu.jpeg"))
rainbow = ImageTk.PhotoImage(Image.open("rainbow.png"))
candv = ImageTk.PhotoImage(Image.open("c and v.jpeg"))
greenninja = ImageTk.PhotoImage(Image.open("greinja.jpeg"))
mandw = ImageTk.PhotoImage(Image.open("m and w.png"))
larpras = ImageTk.PhotoImage(Image.open("lapras.jpeg"))
chari = ImageTk.PhotoImage(Image.open("Charizard.jpeg"))
b = ImageTk.PhotoImage(Image.open("b.png"))
vir = ImageTk.PhotoImage(Image.open("vir .png"))
flare = ImageTk.PhotoImage(Image.open("flareon.jpeg"))



player1_label = Label(root,text="Player1",bg="white",fg="red") 
player1_label.place(relx=0.1,rely=0.3,anchor=CENTER)

player2_label = Label(root,text="Player2",bg="white",fg="red")
player2_label.place(relx=0.9,rely=0.3,anchor=CENTER)

player1_score_label = Label(root,text="Player1 Score:", bg="White", fg="red")
player1_score_label.place(relx=0.1,rely=0.4,anchor=CENTER)

player2_score_label = Label(root,text="Player2 Score:", bg="White", fg="red")
player2_score_label.place(relx=0.9,rely=0.4,anchor=CENTER)


pokemon_list = [pikachu, rainbow, candv, greenninja, mandw, larpras, chari, vir, flare]
power_list = [60, 70, 130, 140, 160, 170, 200, 230, 270, 300]

label = Label(root)
label.place(relx=0.5, rely=0.5,width="300", height="400" ,anchor=CENTER)



player1_score = 0 
def player1():
    global player1_score
    random_number = random.randint(0,8)
    random_pokemon = pokemon_list[random_number]
    label["image"] = random_pokemon
    
    random_powerlist = power_list[random_number]
    player1_score = player1_score +  random_powerlist
    player1_score_label["text"]="Player1 Score: " + str(player1_score)
player1_button = Button(root, text="Click Me!!!", command = player1)
player1_button.place(relx=0.1,rely=0.6,anchor=CENTER)

player2_score = 0 
def player2():
    global player2_score
    random_number = random.randint(0,9)
    random_pokemon = pokemon_list[random_number]
    label["image"] = random_pokemon
    
    random_powerlist = power_list[random_number]
    player2_score = player2_score + random_powerlist
    player2_score_label["text"]="Player2 Score: " + str(player2_score)
player2_button = Button(root, text = "Click Me!!!", command = player2)
player2_button.place(relx=0.9,rely=0.6,anchor=CENTER)

root.mainloop()
