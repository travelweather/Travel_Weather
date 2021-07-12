import requests
from tkinter import *
from tkcalendar import *
import tkinter.font as tkFont


# initialization
root = Tk()
root.title("Travel Weather")
root.geometry("800x700")
root.resizable(False, False)
title = Label(root, text="Travel Weather")
weatherlist = []

def page1():

    # UI for first page
    page1 = PhotoImage(file="page1.png")
    background = Label(root, image=page1)
    background.place(x=0,y=0, relwidth=1, relheight=1)

    # creating a button
    continue_image = PhotoImage(file="Continue.png")
    button = Button(root, height=30, width=200, image = continue_image ,command=lambda: input())
    button.pack()
    button.place(x=305, y=621)

    # Outputting textbox
    textbox = Entry(bd=0, bg="#FFFFFF")
    textbox.pack()
    textbox.place(x=455, y=140, width=270, height=20)


    # Calendar for start date
    calstart = Calendar(root, locale='en_US', date_pattern='yyyy-mm-dd')
    calstart.pack(pady=20)
    calstart.place(x=300, y=200)

    # Calendar for end date
    calend = Calendar(root, locale='en_US', date_pattern='yyyy-mm-dd')
    calend.pack(pady=20)
    calend.place(x=300, y=400)

    # determines if the inputted city exists
    def identify():
        api_key = "BDSBW3NQQGYYF3VTR2R2PQ8G3"
        url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/" + city + "/" + calstart.get_date() + "/" + calend.get_date() + "?key=" + api_key
        data = requests.get(url).json()
        #print(url)
        for i in range(len(data['days'])):
            weather_condition = data['days'][i]['description']
            weatherlist.append(weather_condition)
            print(weather_condition)

    def page2():
        # initialize
        textbox.destroy()
        button.destroy()
        calstart.destroy()
        calend.destroy()
        background.destroy()
        fontStyle =tkFont.Font(family="Open Sans", size=16)


        # UI for first page
        page2 = PhotoImage(file="page2.png")
        background2 = Label(root, image=page2)
        background2.place(x=0, y=0, relwidth=1, relheight=1)


        # determining weather via api
        for i in range(len(weatherlist)):
            daynum = i + 1
            label1 = Label(root, text = "The weather on day "+ str(daynum) + " of your trip will be " + weatherlist[i], font = fontStyle, wraplength=750, bg ="#008FEE")
            label1.pack()
            label1.place(x=25, y=75 + i*75)
        root.mainloop()



    # takes input
    def input():
        global city
        city = textbox.get()
        print(city)
        identify()
        page2()



    root.mainloop()

page1()
