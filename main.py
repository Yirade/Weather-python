
from tkinter import *

import requests, json, pytemperature

from PIL import ImageTk, Image

from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo

#VARIABLE

title = "Weather "
city = ''
phrase = ['Enter a city:', 'The weather in ', " is:", 4, 'C', ' ']

theme = ["White", "Black", "#2B2930", "#6B6A62", "#FF66C0"]
palette = ["White",#n.0 White
           "Black",#n.1 Black
           "#2B2930",#n.2 Dark gray
           "#6B6A62",#n.3 Ligth gray
           "#FF66C0",#n.4 Pink
           2]

api_key = "blank"
api_key_personal = 'cb7b8cefa88b491b91f37100d83e51d4'
base_url = "http://api.openweathermap.org/data/2.5/weather?"

file_data = ""
file_data_temp = "api_key: " + api_key + " theme: " + str(palette[5])

stored = ""
splitted_stored = []

#Start defs

def file_cond():
    global f
    global stored
    global file_data
    global splitted_stored
    global api_key
    f = open("config.txt","a")
    f.close()
    f = open("config.txt","r")
    #f.seek(0)    
    stored = f.read()
    print(stored)
    f.close()
    f = open("config.txt","w")
    splitted_stored = stored.split()
    print(splitted_stored)
    if "api_key:" in stored:
        print("api_key is in stored")
        api_key = splitted_stored[1]
        print("api key allocated", api_key)
        print(file_data)
        palette[5] = int(splitted_stored[3])
        print(file_data)
        file_data = "api_key: " + api_key + " theme: " + str(palette[5])
        print(file_data)
        f.write(file_data)
        print("new file data is: ", file_data)
        f.close()
    else:
        f.write(file_data_temp)
        f.close()        
#--------------------------------------------------#    
def th_ch(a):
    global theme
    global file_data
    global palette
    palette[5] = a
    print("Current theme is", palette[5])
    print(palette[5])
    f = open("config.txt","w")
    file_data = "api_key: " + api_key + " theme: " + str(palette[5])
    f.write(file_data)
    f.close()
    showwarning(title="Success!", message="Theme susseffuly applied, restart for see changes!")
#--------------------------------------------------#    
def th():
    global theme
    global palette
    if palette[5] == 0:
        #Dark
        theme[0] = palette[0]
        theme[1] = palette[1]
        theme[2] = palette[2]
        theme[3] = palette[3]
        theme[4] = palette[1]
    elif palette[5] == 1:
        #White
        theme[0] = palette[1]
        theme[1] = palette[0]
        theme[2] = palette[0]
        theme[3] = palette[0]
        theme[4] = palette[0]
    elif palette[5] == 2:
        #Pink
        theme = palette      
#--------------------------------------------------#    
#Api Allocation
def btn_ok(link):
    global api_key
    api_key=link
    print("Your api key is:", api_key)
    if len(api_key) == 32:
        f = open("config.txt","w")
        file_data = "api_key: " + api_key + " theme: " + str(palette[5])
        f.write(file_data)
        f.close()
        showinfo(title="Sucess!", message="api key sussefully allocated!")
        settings.destroy()
    else:
        showwarning(title="Invalid api key!", message="The api key format is incorrect!")
        txt_sett1.delete(0, len(api_key)+1)
#--------------------------------------------------#

#Ini
file_cond()
th()

#Root Window
root = Tk()
root.title(title + city)
root.geometry('250x190')
root.configure(bg=theme[2])
#Components
lbl1  = Label(root, text = phrase[0], fg=theme[0], bg=theme[2])
lbl1.grid(column =2, row = 2, pady=(0,8))

lbl0  = Label(root, text = '\t   ', bg=theme[2])
lbl0.grid(column =1, row = 0)

lbl01  = Label(root, text = '\t   ', bg=theme[2])
lbl01.grid(column =1, row = 4)

txt = Entry(root, width=10, bg=theme[3], fg=theme[0])
txt.grid(column =2, row =3)

    
#Windows

def result_screen():#work in progress...
     
    result = Tk()
    result.title(title + "in " + city)
    result.geometry('300x150')
    result.configure(bg=theme[2])
    img = PhotoImage(file=r"sc.png")
    w = Label(result, image=img).grid()
    
#--------------------------------------------------#
    
def about():#work in progress...
    
    ab = Tk()
    ab.title("Settings")
    ab.geometry("200x100")
    ab.configure(bg=theme[2])
    
#--------------------------------------------------#
    
def setting():        
    
    global settings
    
    settings = Tk()
    settings.title("Settings")
    settings.geometry("420x200")
    settings.configure(bg=theme[2])
        #Content - api
    lbl_sett1 = Label(settings, text="api key", bg=theme[2], fg=theme[0])
    lbl_sett1.grid(column=0, row=0, padx=(0), pady=(15))
    
    global txt_sett1
    txt_sett1 = Entry(settings, width=30, bg=theme[3], fg=theme[0])
    txt_sett1.insert(0, api_key)
    txt_sett1.grid(column =1, row =0)
    
    btn_sett1 = Button(settings, text = "ok", fg = theme[0], bg=theme[3], command=lambda:btn_ok(txt_sett1.get()))
    btn_sett1.grid(column=2, row=0, padx=(5))
        #Content - theme
    lbl_th0 = Label(settings, text="Select a theme:", fg=theme[0], bg=theme[2])
    lbl_th0.grid(column=0, row=3, padx=(5,0), pady=(25,15))
    
    btn_th_dark = Button(settings, text="Dark", fg= palette[0], bg=palette[2], command=lambda:th_ch(0))
    btn_th_dark.grid(column=0, row=4)
    
    btn_th_white = Button(settings, text="White", fg= palette[1], bg=palette[0], command=lambda:th_ch(1))
    btn_th_white.grid(column=1, row=4, padx=(25,25))
    
    btn_th_pink = Button(settings, text="Pink", fg= palette[1], bg=palette[4], command=lambda:th_ch(2))
    btn_th_pink.grid(column=2, row=4)
    
    btn_about = Button(settings, text="About", fg= theme[0], bg=theme[2], command=lambda:about())
    btn_about.grid(column=1, row=5, pady=(25))

#--------------------------------------------------#
    
    
    

#Definition

def clicked():
 
    res = txt.get()
    city = res
    
    if api_key == '' or api_key == "blank":
        showerror(title="Error!", message="Insert an api key in settings!")
        txt.delete(0, len(city)+1)
    elif len(api_key) != 32:
        showwarning(title="Invalid api key!", message="The api key format is incorrect!")
    elif city == '':
        showerror(title="Error!", message="You need to enter a city!")
    else:
        degrees = '°' #chr(248)
        
        
        complete_url = base_url + "appid=" + api_key + "&q=" + city
        
        response = requests.get(complete_url)
        
        x = response.json()
        
        #Invalid City - Error message
        if x["cod"] == "404":
            showerror(title="Error!", message= city + " doesen't exist!")
            txt.delete(0, len(city)+1)
       
        else:
        #Allocation values
            y = x["main"]
            current_temperature = y["temp"]
            z = x["weather"]
            weather_description = z[0]["description"]
            phrase[3] = str(current_temperature)
            
            phrase[3] = round(pytemperature.k2c(float(phrase[3])),2)
            print(phrase[3])
            
            
            
            rez = phrase[1] + res + phrase[2] + phrase[5] + str(phrase[3]) + degrees + phrase[4]
            print(rez)
            print(city)
            label = Message(root, text= rez)

            showinfo(title= city, message= rez)
            txt.delete(0, len(city)+1)
        


    
    

#Top menu
    
menu = Menu(root, bg=theme[2], fg=theme[0], bd = 0)
root.config(menu=menu, bg=theme[2])
filemenu = Menu(menu, bg=theme[2])
menu.add_command (label="Settings", command=setting, activebackground=theme[3])
                              
#Main Button

btn = Button(root, text = "Click me" , fg = theme[0], bg=theme[4], command=clicked)
btn.grid(column=2, row=5)

lbl2 = Label(root, text = "made by Yirade", fg = palette[3], bg = theme[2])
lbl2.grid(column=2, row=6, pady=(50))

root.mainloop()