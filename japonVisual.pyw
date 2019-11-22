# -*- coding: utf-8 -*-
from Tkinter  import *
import ttk

root = Tk()
root.title("Metro Japón")

frame= Frame(root)
frame.pack()
frame.config(width=600,height = 600)

labelOrigen = Label(frame, text = "Origen:")
labelOrigen.grid(row=0, column=0, sticky=W ,padx=5, pady=5)

seleccionOrigen = ttk.Combobox(frame)
seleccionOrigen.grid(row=1, column =0,padx=5, pady=5)
seleccionOrigen["values"] = ("Shinagawa","Osaki","Gotanda","Meguro","Ebisu","Shibuya","Harajuku","Yoyogi",
                            "Shinjuku","Shin-Okubo","Takadanobaba","Mejiro","Ikebukuro","Otsuka","Sugamo",
                            "Komagome","Tabata","Nishi-Nippori","Nippori","Uguisudani","Ueno","Okachimachi",
                            "Akihabara","Kanda","Tokyo","Yurakucho","Shimbashi","Hamamatsucho","Tamachi",
                            "Ochanomizu","Suidobashi","Iidabashi","Ichigaya","Yotsuya","Shinanomachi","Sendagaya")

labelDestino = Label(frame, text = "Destino:")
labelDestino.grid(row=2, column=0, sticky=W ,padx=5, pady=5)

seleccionDestino = ttk.Combobox(frame)
seleccionDestino.grid(row=3, column =0,padx=5, pady=5)
seleccionDestino["values"] = ("Shinagawa","Osaki","Gotanda","Meguro","Ebisu","Shibuya","Harajuku","Yoyogi",
                            "Shinjuku","Shin-Okubo","Takadanobaba","Mejiro","Ikebukuro","Otsuka","Sugamo",
                            "Komagome","Tabata","Nishi-Nippori","Nippori","Uguisudani","Ueno","Okachimachi",
                            "Akihabara","Kanda","Tokyo","Yurakucho","Shimbashi","Hamamatsucho","Tamachi",
                            "Ochanomizu","Suidobashi","Iidabashi","Ichigaya","Yotsuya","Shinanomachi","Sendagaya")

botonCalcular  = Button (frame, text = "Calcular ruta")
botonCalcular.grid(row=4, column=0 ,padx=5, pady=5)


labelResultado = Label(frame, text = "Resultado:")
labelResultado.grid(row=0, column=1, sticky=W ,padx=5, pady=5)

 

root.mainloop()