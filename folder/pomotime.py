#############################################################
# pomotime.py
#   The goal is to encourage students and others to start working 
#       by keeping them focused throughout several sessions of 
#       working and breaks while inspiring quotes are displayed to 
#       keep them encouraged.
#############################################################

####### CITATIONS ########
# Import of Random library citation: 
# https://docs.python.org/3/library/random.html © Copyright 2001-2022, Python Software Foundation. 

# Import of Time library citation: 
# https://docs.python.org/3/library/time.html © Copyright 2001-2022, Python Software Foundation. 

# Import of Tkinter library citation:
# https://docs.python.org/3/library/tkinter.html © Copyright 2001-2022, Python Software Foundation. 

# Import of Tkinter Messagebox library citation:
# https://docs.python.org/3/library/tkinter.messagebox.html © Copyright 2001-2022, Python Software Foundation. 

# Import of PIL Tools Image Module citation:
# https://pillow.readthedocs.io/en/stable/reference/Image.html © Copyright 1995-2011 Fredrik Lundh, 2010-2022 Alex Clark and Contributors.

# Import of PIL Tools ImageTK Module citation:
# https://pillow.readthedocs.io/en/stable/reference/ImageTk.html © Copyright 1995-2011 Fredrik Lundh, 2010-2022 Alex Clark and Contributors.

# Import of Textwrap library citation:
# https://docs.python.org/3/library/textwrap.html © Copyright 2001-2022, Python Software Foundation.

# Background Image Citation:
# Created by code creater through canva

# Inspirational quotes data source citation:
# Bright Culture. “202 Motivational Quotes for Students - Get Motivated While Studying.” Bright Culture, 16 Jan. 
#   2021, https://bright-culture.com/exam-tips-for-students/202-motivational-quotes-for-students-studying/. 
##########################

# imports
import random
import time
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk 
import textwrap # used for textwrapping the quote in label

# takes random quote from list(quotes.txt)
def RandomQuote(n):
    mylines = []
    random_line = random.randint(1,202) # picks random number from 1 to 202            
    # Open quotes.txt and read in quotes
    with open ('quotes.txt', encoding='utf-8') as myfile: 
        for myline in myfile:                
            mylines.append(myline)  
        global quote_choice  
        quote_choice = str(mylines[random_line])
        quote_choice = textwrap.fill(quote_choice, 18) # sets limit of 18 charcters for quote
        # call the display function
        displayQuotes(quote_choice, n)

# quotes display function
def displayQuotes(quote_choice, n):
    for i in range (n): # n is used to limit it from looping more than 1 time(since thats all that is needed)
        Quo.set(quote_choice)
        # update screen now
        window.update()
        time.sleep(1)
    
# display timer function
def displayTime(timer):
    # displays minutes and seconds       
    minutes, seconds = divmod(timer, 60)
    Min.set(f"{minutes:02d}") # sets to only 2 decimals places diplayed
    Sec.set(f"{seconds:02d}") # sets to only 2 decimals places diplayed
    # update screen now
    window.update()
    time.sleep(1)
        
# Work function --> 25 minutes
def work():
    timer = 25 * 60 # 25 minutes --> seconds
    quote_timer = 25 * 60
    n = 1 # only displays the quote once
    while timer >= 0:
        displayTime(timer)
        if timer == 0:
            messagebox.showinfo("Pomodoro Timer Alert", "Work Done\nGreat job, break time!\nClick Break Button")
        # subtract second from timer while true
        timer -= 1

        while quote_timer >= 0:
            if quote_timer == 25*60:
                RandomQuote(n)
            quote_timer -= 1

# short break function --> 5 minutes
def short_break():
    timer = 5*60 # 5 minutes --> seconds
    n = 1 # only displays the quote once
    quote_timer = 5*60
    while timer >= 0:
        displayTime(timer)
        if timer == 0:
            messagebox.showinfo("Pomodoro Timer Alert", "Short break Done \nTime to get to work!\nClick Work Button")
        # subtract second from timer while true
        timer -= 1

        while quote_timer >= 0:
            if quote_timer == 5*60:
                RandomQuote(n)
            # subtract second from timer while true
            quote_timer -= 1

# long break function --> 10 minutes
def long_break():
    timer = 10 * 60 # 10 minutes --> seconds
    n = 1 # only displays the quote once
    quote_timer = 10*60
    while timer >= 0:
        displayTime(timer)
        if timer == 0:
            messagebox.showinfo("Pomodoro Timer Alert", "Long break done \nTime to get to work!\nClick Work Button")
        # subtract second from timer while true
        timer -= 1

        # display a quote at the beginning of this cycle 
        while quote_timer >= 0:
            if quote_timer == 10*60: # when this timer is at 10 minutes... display quote
                RandomQuote(n) # makes new random quote and displays it
            # subtract second from timer while true
            quote_timer -= 1

# display of users name they inputed
name_input = input("Hello! What is your name?")
name = "Welcome " + name_input + "!"

######################################
######################################
# directions printed in console below 
for i in range(4):
    print("-------READ BELOW THIS-------")
print("-------WELCOME TO POMOTIME!-------")
print("Here you can use the pomodoro method for a more focused studying or work session!")
print("-------HOW DOES IT WORK-------")
print("The pomodoro method set up is to do work session then short break and repeat twice and then after one final work session a longer break")
print("-------POMODORO METHOD SCHEDULE-------\n--\nWORK: 25 mins\n--\nBREAK: 5 mins\n--\nWORK:25 mins\n--\nBREAK: 5 mins\n--\nWORK: 25 mins\n--\nBREAK: 10 mins\n--\nREPEAT FROM START(do however many times)")
print("--\nHopefully you find some success or enjoyment in this process :) \nHave fun!!!!")
for i in range(4):
    print("-------READ ABOVE THIS-------")
######################################
######################################

# GUI using tk/tkinter
# this will be the tkinter set up
window = Tk()
window.geometry("1000x500")
window.resizable(False, False)
window.title("Pomodoro Timer")

# setting up canvas
canvas = tk.Canvas(window)
canvas.pack(expand=True, fill="both")
img = Image.open('blue_bg.png') # setting image as background
bg = ImageTk.PhotoImage(img)
canvas.create_image(0, 0, image=bg, anchor="nw")

# Variables to keep track and display (also setting them to strs to)
Min=StringVar()
Sec=StringVar()
Quo=StringVar()
Name=StringVar()

# set default time/ quote/ name
Min.set("25")
Sec.set("00")
Quo.set("")
Name.set(name)

# label to tell user to read terminal with the instructions
canvas.create_text(500, 75, text = "Read your terminal before starting!!!")

# minutes title
canvas.create_text(465, 300, text = "Minutes(s)")

# where minutes will be displayed
min_label = tk.Label(window,textvariable=Min, font=("arial", 22))
min_label.place(x=445,y=240)

# used as divider between mins and secs
divider_label = tk.Label(window,text="::", font=("arial", 22))
divider_label.place(x=490,y=240)

# seconds title
canvas.create_text(545, 300, text = "Second(s)")

# where secs will be displayed
sec_label = tk.Label(window,textvariable=Sec, font=("arial", 22))
sec_label.place(x=520,y=240)

#name title/ where welcome 'your name' will be displayed
name_label = tk.Label(window, textvariable=Name, font=("Fixedsys", 30), width=20, height=1, borderwidth=3, relief="groove")
name_label.place(x=295,y=20)

# where quote will be displayed 
quote_label = tk.Label(window, textvariable=Quo, font=("arial", 16), width=16, height=14, borderwidth=3, relief="ridge")
quote_label.place(x=735,y=80)

# Buttons
# work button
work_button = Button(window, text='Work', font=("Fixedsys", 15),command= work, width=20, height=3, borderwidth=3, relief="ridge")
work_button.place(x = 60, y = 85)

# short break button
shortb_button = Button(window, text='Short Break', font=("Fixedsys", 15), command= short_break, width=20, height=3, borderwidth=3, relief="ridge")
shortb_button.place(x = 60, y = 210)

# long break button
longb_button = Button(window, text='Long Break', font=("Fixedsys", 15),command= long_break, width=20, height=3, borderwidth=3, relief="ridge")
longb_button.place(x = 60, y = 335)

# end main loop
window.mainloop()