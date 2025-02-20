# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 15:58:11 2025

@author: Administrator
"""

from tkinter import *
from tkinter import ttk




root = Tk()
root.geometry("640x720")

notebook = ttk.Notebook(root)

FA_tab1 = Frame(notebook)
FA_tab2 = Frame(notebook)
    


notebook.add(FA_tab1, text = "Failure Analysis")
notebook.add(FA_tab2, text ="Repair")
notebook.place(x=0, y =0)


Label(FA_tab1, text = "HAHAHAHAHAHAHAHA").pack()

imagevis = PhotoImage(file = 'pics\\datavis.png');
button = Button(FA_tab1, text = "AHAHAHAHAHAHAAH")
#utton.config(command = Output_performance );


button.config(font = ('Ink Free', 20, 'bold'));
button.config(bg = '#fafafc');
button.pack()

FAbg = Label(FA_tab2, image = imagevis)
FAbg.pack()

root.mainloop()
