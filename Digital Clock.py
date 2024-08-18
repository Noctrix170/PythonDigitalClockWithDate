from tkinter import *
import tkinter

from datetime import datetime

color1 = "black"
color2 = "light green"

root = Tk()
root.title("Nihat Digital Clock")
root.geometry("1920x1080")
root.resizable(width = True, height = True)#to not change the size of the window
root.config(bg = color1)

def clock():
    time = datetime.now()
    hour = time.strftime("%H:%M:%S") #saat
    weekday = time.strftime("%A") #hafta nin ne gunu
    day = time.day #Ay in kaci
    month = time.strftime("%b") #ay
    year = time.strftime("%Y") #yil
    l1.config(text = hour)
    l1.after(200, clock) # 200 Milisaniye sonra bunu bunu yap

    l2.config(text = weekday + " " + str(day) + "/" + str(month) + "/" + str(year))
    
l1 = Label(root, font = (" DS-Digital 250"), bg = color1, fg = color2)
l1.grid(row = 0, column = 0)

l3 = Label(root, text = "    ", bg = color1, fg = color2)
l3.grid(row = 1, column = 0)

l2 = Label(root, font = (" Arial 100 bold"), bg = color1, fg = color2)
l2.grid(row = 2, column = 0)


clock()

root.mainloop()
