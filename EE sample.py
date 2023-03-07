import requests,json
import tkinter
from tkinter import *
from tkinter import messagebox
api_key = "c341e3a5ede9998e3438942cb2f27d12"


def proceed():
    city=cit.get()
    if city=='':
        return messagebox.showerror('Error','Enter City Name')
    elif api_key=='your api key':
        return messagebox.showerror('Error','Enter your api key')

    else:
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        cityname = city
        complete_url = base_url + "appid=" + api_key + "&q=" + cityname 
        response = requests.get(complete_url)
        print(response.text)
        x = response.json()
        print(x)
        print(type(x))
        if x["cod"] != "404": 
            y = x["main"]
            #print(y)
            currenttemp = y["temp"]
            temp_min=y["temp_min"]
            temp_max=y["temp_max"]
            currentpressure = y["pressure"] 
            currenthumidiy = y["humidity"]
            z = x["weather"] 
            weather_description = z[0]["description"]

            a=tkinter.Label(m,text='Temperature: ',fg='blue',bg='orange').place(x=2,y=90)
            a1=tkinter.Entry(m)
            a1.place(x=90,y=90)
            a1.insert(15,str(round(currenttemp-272.15))+'°C')
            
            b=tkinter.Label(m,text='Atmospheric Pressure: ',fg='blue',bg='orange').place(x=2,y=120)
            b1=tkinter.Entry(m)
            b1.place(x=150,y=120)
            b1.insert(15,str(currentpressure)+' hPa')

            
            c=tkinter.Label(m,text='Humidity: ',fg='blue',bg='orange').place(x=2,y=150)
            c1=tkinter.Entry(m)
            c1.place(x=90,y=150)
            c1.insert(15,str(currenthumidiy))
            
            d=Label(m,text='Description: ',fg='blue',bg='orange').place(x=2,y=180)
            d1=tkinter.Entry(m)
            d1.place(x=90,y=180)
            d1.insert(15,str(weather_description))
        else: 
            return messagebox.showerror('Error','No City Found')
        d=tkinter.Button(m,text='Team members',fg='blue',bg='orange',command=display).place(x=2,y=210)



def display():
    d1=tkinter.Label(m,text='VIVEK,KOWSHIK,NOOR').place(x=2,y=240)


m=tkinter.Tk()
m.geometry('600x400')
m.title('Weather Report')
m['bg']="yellow"
#bg = PhotoImage(file = "weather_og.png")
cit=StringVar()
ga=tkinter.Label(m,text='Weather Report Application',fg="blue",bg="yellow",font='Helvetica 12 bold').grid(row=1,column=1)
gb=tkinter.Label(m,text='Enter City:',fg="green",bg="orange").grid(row=2,column=1)
gc=tkinter.Entry(m,width=15,textvariable=cit).grid(row=2,column=2)
gd=tkinter.Button(m,text='Proceed',command=proceed).grid(row=4,column=2)
