# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 01:56:45 2025

@author: Administrator
"""
from temp import *


def create_db_connection (host_name, user_name, user_password, db_name):
    connection = None;
    
    try:
        connection = mysql.connector.connect(
            
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name
            
            )
        print ("MySQL Database connection successful");
        
    except Error as err:
        
        print( f"Error:  '{err}'");
        
    return connection


def create_server_connection(host_name, user_name, user_password):
    connection = None;
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password
            )
        print ("MySQL Database connection successful");
        
    except Error as err:
        
        print(f"Error : '{err}'");
    
    return connection


def execute_query(connection, query):
    cursor = connection.cursor();
    
    try:
        cursor.execute(query);
        connection.commit();
        print ("Query successful");
    except Error as err:
        print (f"Error: '{err}'");
        
#-------------------------------------------------------------

#New windows

def Output_performance():
    Output = Toplevel()
    Output.geometry("1280x720");
    Output.title("FA System Database and Output Performance");
    icon = PhotoImage(file = 'pics\\kinpologo2.png');
    Output.iconphoto(True, icon);
    Output.config(background="#0f32f7");
    Output.resizable(False, False)
    
    cal = DateEntry(Output, date_pattern="yyyy--mm--dd", state = 'readonly')
    cal.place(x = 400, y = 400)
    cal.delete(0, "end")
    #cal.get()
    
    cal2 = DateEntry(Output, date_pattern="yyyy--mm--dd", state = 'readonly')
    cal2.place(x = 600, y = 400)
    cal2.delete(0, "end")
    #cal2.get()

"""from tkinter import Tk,Button
from tkcalendar import DateEntry
def get_date():
    selected_date = cal.get()
    print(f"Selected date: {selected_date}")
root = Tk()
cal = DateEntry(root, date_pattern="yyyy-mm-dd")
cal.pack()
cal.delete(0, "end")

btn = Button(root, text="Click Here To Return a Date ", command=get_date)
btn.pack()
root.mainloop()"""
#------------------------------------------------------------