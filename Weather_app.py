import tkinter as tk
import requests
from api import app_id

from tkinter import messagebox

def getWeather(canvas):
    try:

        city = textfield.get()
        api = "https://api.openweathermap.org/data/2.5/weather?q="+ city + app_id
        json_data = requests.get(api).json()
        city = json_data['name']
        country = json_data['sys']['country']
        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'] - 273.15)
        min_temp = int(json_data['main']['temp_min'] - 273.15)
        max_temp = int(json_data['main']['temp_max'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
    
        final_info = city +", " + country + "\n" + condition + "\n" + str(temp) + "°C" 
        final_data = "\n" + "Max Temp: " + str(max_temp)+ "°C" + "\n" + "Min Temp: " + str(min_temp) + "°C" + "\n" + "Pressure: " + str(pressure) + "hPa" + "\n" + "Humidity: " + str(humidity) + "%" + "\n" + "Wind Speed: " + str(wind) + "km/h"
    
    except:
        
        final_data = ''
        final_info = ''
        messagebox.showerror('Invalid Input', 'Please Enter a Vaild City/Town name!')

    label1.config(text = final_info)
    label2.config(text = final_data)


canvas = tk.Tk() 
canvas.geometry("650x650")
canvas.title("Weather App")

bg = tk.PhotoImage(file ='Weather App\landscape.png')
bg_label = tk.Label(canvas, image = bg)
bg_label.place(relwidth = 1, relheight = 1)

f = ("Russo One", 22, "bold")
t = ("Georgia", 32, "bold")

label = tk.Label(canvas, font = ("Times New Roman", 24), bg = "Yellow")
label.pack()
label.config(text = "Type the City and Press Enter")

textfield = tk.Entry(canvas, font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font = t)
label1.pack()

label2 = tk.Label(canvas, font = f)
label2.pack()

canvas.mainloop()

