from tkinter import *
from tkinter import ttk
from imp import API_KEY
import requests

FONT = ("Times New Roman", 30, "bold")
FONT2 = ("Times New Roman", 10)


def data_get():
    city_name = StringVar()
    city = city_name.get()
    data = requests.get(url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}").json()
    w_label1.config(text=data['weather'][0]['main'])
    wb_label1.config(text=data['weather'][0]['description'])
    temp_label1.config(text=str(data['main']['temp'] - 273.15))


win = Tk()
win.title("My Weather App")
win.config(bg="grey")
win.geometry("500x570")

name = Label(text="Weather App", font=FONT)
name.place(x=25, y=50, height=50, width=450)

state_names = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
               "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
               "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
               "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh",
               "Dadra and Nagar Haveli and Daman and Diu", "Delhi", "Lakshadweep", "Puducherry"]

city_name = StringVar
com = ttk.Combobox(values=state_names, font=FONT, textvariable=city_name)
com.place(x=25, y=120, height=50, width=450)

w_label = Label(text="Weather Climate", font=FONT2)
w_label.place(x=25, y=260, height=50, width=210)
w_label1 = Label(text="", font=FONT2)
w_label1.place(x=250, y=260, height=50, width=210)

wb_label = Label(text="Weather Description", font=FONT2)
wb_label.place(x=25, y=330, height=50, width=210)
wb_label1 = Label(text="", font=FONT2)
wb_label1.place(x=250, y=330, height=50, width=210)

temp_label = Label(text="Temperature", font=FONT2)
temp_label.place(x=25, y=400, height=50, width=210)
temp_label1 = Label(text="", font=FONT2)
temp_label1.place(x=250, y=400, height=50, width=210)


button = Button(text="Done", font=FONT, command=data_get)
button.place(x=200, y=190, height=50, width=100)

win.mainloop()
