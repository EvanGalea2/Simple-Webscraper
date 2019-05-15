from tkinter import *
from TorontoWeather import Weather
import os

global temperature, feelslike, tempText, feelsText
global weatherObject
weatherObject = Weather()
screen = Tk()
tempText = StringVar()#declaring stringvar must be
feelsText = StringVar()#done after screen = tk()
def main_screen():
    screen.geometry('300x250')
    screen.title('weather forecast')
    Label(text = "temperature", bg = 'grey', width = 300, height = '2').pack()
    temperature = Entry(screen, textvariable = tempText)
    temperature.pack()
    Label(text = "feels like", bg = 'grey', width = 300, height = '2').pack()
    feelslike = Entry(screen, textvariable = feelsText)
    feelslike.pack()
    Button(text = "refresh", height = "2", width = "30", command = refreshPage).pack()
    #refreshPage()
    screen.mainloop()

def refreshPage():
    print(weatherObject.myURL)
    tempText.set(weatherObject.getTemperature())
    feelsText.set(weatherObject.getFeelsLike())


main_screen()
