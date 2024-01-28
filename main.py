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


def get_weather():
    city=text_box.get()

    geolocator = Nominatim(user_agent='geoapiExercises')
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    home=pytz.timezone(result)
    local_time = datetime.now(home)
    current_time=local_time.strftime('%I:%M %p')
    clock.config(text=current_time)
    name.config(text='CURRENT TIME')




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
                            activebackground='black', highlightthickness=0, highlightcolor="black", 
                            takefocus=True, command=get_weather)
insert_search_icon.place(x=400, y=34)

#logo

log_img = PhotoImage(file='img/logo.png')
insert_logo_img = Label(image=log_img)
insert_logo_img.place(x=150, y=100)


#time
name = Label(root, font=('Arial', 15, 'bold'))
name.place(x=30, y=100)
clock = Label(root, font=('Arial', 15, 'bold'))
clock.place(x=30, y=130)


#labelbar

bar_img = PhotoImage(file='img/box.png')
insert_box_img = Label(image=bar_img)
insert_box_img.pack(padx=5, pady=5, side=BOTTOM)

#labels

label1 = Label(root, text='WIND', font=('Heövetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label1.place(x=120, y=400)

label2 = Label(root, text='HUMIDITY', font=('Heövetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label2.place(x=250, y=400)

label3 = Label(root, text='DESCRIPTION', font=('Heövetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label3.place(x=438, y=400)

label4 = Label(root, text='PRESSURE', font=('Heövetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label4.place(x=650, y=400)


t = Label(font=('arial', 20, 'bold'), fg='black')
t.place(x=400, y=150)
c = Label(font=('arial', 20, 'bold'))
c.place(x=400, y=250)

w = Label(text='...', font=('arial', 20, 'bold'), bg='#1ab5ef')
w.place(x=120, y=430)
w = Label(text='...', font=('arial', 20, 'bold'), bg='#1ab5ef')
w.place(x=280, y=430)
w = Label(text='...', font=('arial', 20, 'bold'), bg='#1ab5ef')
w.place(x=450, y=430)
w = Label(text='...', font=('arial', 20, 'bold'), bg='#1ab5ef')
w.place(x=670, y=430)


root.mainloop()