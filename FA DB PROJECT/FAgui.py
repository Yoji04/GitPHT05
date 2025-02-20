# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 01:58:45 2025

@author: Administrator
"""
from temp import *
from FAdefine import *
#WINDOW SETTINGS

window = Tk();
window.geometry("1280x720");
window.title("FA System Database and Output Performance");
icon = PhotoImage(file = 'pics\\kinpologo2.png');
window.iconphoto(True, icon);
window.config(background="#0f32f7");
window.resizable(False, False)


# BUTTON FOR ENDORSEMENT

imageEN = PhotoImage(file = 'pics\\endorsement.png');
imageEN.zoom(25)
imageEN.subsample(32)

button = Button(window, text = 'Product Endorsement');
#button.config(command = );


button.config(font = ('Ink Free', 20, 'bold'), height=200, width= 300);
button.config(bg = '#fafafc');
button.config(image = imageEN, compound = "bottom");
button.place(x = 50, y = 400);

# BUTTON FOR DATA OUTPUT

imagevis = PhotoImage(file = 'pics\\datavis.png');
button = Button(window, text = 'Output Performance');
button.config(command = Output_performance );


button.config(font = ('Ink Free', 20, 'bold'));
button.config(bg = '#fafafc');
button.config(image = imagevis, compound = "bottom");
button.place(x = 400, y = 400);

# BUTTON FOR DATabase config

imagedb = PhotoImage(file = 'pics\\\database.png');

button = Button(window, text = 'Database Config');
#button.config(command = );


button.config(font = ('Ink Free', 20, 'bold'));
button.config(bg = '#fafafc');
button.config(image = imagedb, compound = "bottom");
button.place(x = 720, y = 400);


# BUTTON FOR About

#imagedb = PhotoImage(file = 'C:\\Users\\Administrator\\Downloads\\database.png');

button = Button(window, text = 'About');
#button.config(command = );
button.config(font = ('Ink Free', 20, 'bold'));
button.config(bg = '#fafafc');
#button.config(image = imagedb, compound = "bottom");
button.place(x = 1100, y = 600);

window.mainloop();