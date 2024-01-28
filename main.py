from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


root = Tk()
root.title('Weather App')
root.geometry('900x500+300+200')
root.resizable(False,False)

#searchbox
search_img = PhotoImage(file='img/search.png')
insert_search_img = Label(image=search_img)
insert_search_img.place(x=20, y=20)

text_box = tk.Entry(root, justify='center', width=17, font=('poppins', 24, 'bold'), bg='black', 
                    bd=0, fg='white', insertbackground='white', highlightthickness=0, highlightcolor="black")
text_box.place(x=50, y=40)
text_box.focus()

search_icon = PhotoImage(file='img/search_icon.png')
insert_search_icon = Button(image=search_icon, borderwidth=0, bg='black', cursor='hand2',  
                            activebackground='black', highlightthickness=0, highlightcolor="black", takefocus=True)
insert_search_icon.place(x=400, y=34)

#logo

log_img = PhotoImage(file='img/logo.png')
insert_logo_img = Label(image=log_img)
insert_logo_img.place(x=150, y=100)

#labelbar

#labels

root.mainloop()