import sys
import tkinter as tk
sys.path.append('C:\\users\\mrssp\\appdata\\local\\programs\\python\\python37-32\\lib\\site-packages')
import python_weather
import asyncio
import os




root= tk.Tk()
root.title('Weather Application')
canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Find the Temperature of Any City')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Type Your City:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)


    


async def getweather():
    async with python_weather.Client(format=python_weather.IMPERIAL) as client:
        x1 = entry1.get()
        weather = await client.get(x1)
        x2=weather.current.temperature
        label4 = tk.Label(root, text=x2,font=('helvetica', 10, 'bold'))
        canvas1.create_window(200, 230, window=label4)

def functionPass():
    asyncio.run(getweather())

button1 = tk.Button(text='Get The Temperature', command=lambda:asyncio.run(getweather()), bg='blue', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()
