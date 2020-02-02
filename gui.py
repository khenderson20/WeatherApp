import tkinter as tk
import requests
from tkinter import font
HEIGHT = 500
WIDTH = 600

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperature (F): %s' % (name, desc, temp)
    except:
        final_str = 'There was a problem retrieving the weather data.'
    return final_str

def get_weather(city):
    weather_key = 'b6290511f2db959f61743c66883baa4d'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)
# API KEY: b6290511f2db959f61743c66883baa4d
# api.openweathermap.org/data/2.5/weather?q={city name}

window = tk.Tk()

canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH, bg='white')
canvas.pack()

background_image = tk.PhotoImage(file='clouds.png')
background_label = tk.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(window, bg='#5b8c85', bd=10)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather!", font=40, command=lambda: get_weather(entry.get()), fg='#5b8c85')
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(window, bg='#5b8c85', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 18))
label.place(relwidth=1, relheight=1)

window.mainloop()
