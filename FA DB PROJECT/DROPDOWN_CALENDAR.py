# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:09:14 2025

@author: Administrator
"""

from tkinter import Tk,Button
from tkcalendar import DateEntry
def get_date():
    selected_date = cal.get()
    print(f"Selected date: {selected_date}")
root = Tk()
root.geometry("1280x720");
cal = DateEntry(root, date_pattern="yyyy-mm-dd")
cal.place(x = 400, y = 400)
cal.delete(0, "end")

btn = Button(root, text="Click Here To Return a Date ", command=get_date)
btn.pack()
root.update()
root.mainloop()