from tkinter import *
from tkinter import ttk
import requests
def data_get():
    city=city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=fec83c57af49257d808bd45215200bd8").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    p_label1.config(text=data["main"]["pressure"])
    hum_label1.config(text=data["main"]["humidity"])
win=Tk()
win.title("weather app")
bg=PhotoImage(file="project.png")
background_label=Label(win,image=bg)
background_label.place(x=0,y=0,relwidth=1,relheight=1)
win.geometry("1000x1000")

name_label= Label(win,text="Today's weather",
                 font=("Time New Roman",30 ,"bold"),
                  bg=("AntiqueWhite3"))
name_label.place(x=300,y=50,height=50,width=450)
city_name=StringVar()
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com=ttk.Combobox(win,text="Today's weather",values=list_name,
                 font=("Time New Roman",20),textvariable=city_name)
com.place(x=350,y=120,height=40,width=350)
w_label=Label(win,text="weather climate",
              font=("Arial",15),bg=("AntiqueWhite3"))
w_label.place(x=350,y=260,height=50,width=150)
w_label1=Label(win,text="",
              font=("Arial",15),bg=("AntiqueWhite3"))
w_label1.place(x=575,y=260,height=50,width=150)

wb_label=Label(win,text="weather description",
              font=("Arial",15),bg=("AntiqueWhite3"))
wb_label.place(x=320,y=330,height=50,width=200)
wb_label1=Label(win,text="",
              font=("Arial",15),bg=("AntiqueWhite3"))
wb_label1.place(x=575,y=330,height=50,width=150)
temp_label=Label(win,text="temperature",
              font=("Arial",15),bg=("AntiqueWhite3"))
temp_label.place(x=350,y=400,height=50,width=150)
temp_label1=Label(win,text="",
              font=("Arial",15),bg=("AntiqueWhite3"))
temp_label1.place(x=575,y=400,height=50,width=150)
p_label=Label(win,text="pressure",
              font=("Arial",15),bg=("AntiqueWhite3"))
p_label.place(x=350,y=470,height=50,width=150)
p_label1=Label(win,text="",
              font=("Arial",15),bg=("AntiqueWhite3"))
p_label1.place(x=575,y=470,height=50,width=150)
hum_label=Label(win,text="humidity",
              font=("Arial",15),bg=("AntiqueWhite3"))
hum_label.place(x=350,y=550,height=50,width=150)
hum_label1=Label(win,text="",
              font=("Arial",15),bg=("AntiqueWhite3"))
hum_label1.place(x=575,y=550,height=50,width=150)
done_button=Button(win,text="Done",
                 font=("Time New Roman",20),command=data_get,bg=("AntiqueWhite3"))
done_button.place(x=475,y=190,height=50,width=100)
win.mainloop()