import easygui
import getIcon

def Mbox(imgName,msg):
     image = "WeatherImages//"+imgName+".gif"
     easygui.msgbox(msg, image=image,ok_button="OK" )

'''import Tkinter as tk
def Mbox(msg):
    root = tk.Tk()
    root.title("Weather Condition")
    label = tk.Label(root, text=msg)
    label.pack(side="top", fill="both", expand=True, padx=30, pady=30)
    button = tk.Button(root, text="OK", command=lambda: root.destroy())
    button.pack(side="bottom", fill="none", expand=True)
    root.mainloop()'''

'''from Tkinter import *
def Mbox(msg):
    root=Tk()
    b=Button(root,justify = LEFT)
    photo=PhotoImage(file="02d.png")
    b.config(image=photo,width="100",height="100")
    b.pack(side=LEFT)
    root.mainloop()'''
