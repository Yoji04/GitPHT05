# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:31:56 2025

@author: Administrator
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from tkinter import *

root = Tk()
root.geometry("1280x720")

df = pd.DataFrame({'country': [177.0, 7.0, 4.0, 2.0, 2.0, 1.0, 1.0, 1.0]})
df.index = ['USA', 'Canada', 'Russia', 'UK', 'Belgium', 'Mexico', 'Germany', 'Denmark']
df = df.sort_values(by='country',ascending=False)
df["cumpercentage"] = df["country"].cumsum()/df["country"].sum()*100


fig, ax = plt.subplots()
ax.bar(df.index, df["country"], color="C0")
ax2 = ax.twinx()
ax2.plot(df.index, df["cumpercentage"], color="C1", marker="D", ms=7)
ax2.yaxis.set_major_formatter(PercentFormatter())

ax.tick_params(axis="y", colors="C0")
ax2.tick_params(axis="y", colors="C1")
#plt.show()

mybutton = Button(root, command= plt.show())
mybutton.pack()
root.mainloop()