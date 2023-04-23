import tkinter as tk
from tkinter import ttk

#Values
screen_width=300
screen_height=750

class Interface:
    def __init__(self,width,height):
        self.width=width
        self.height=height
        #Window
        self.window=tk.Tk()
        self.window.geometry('{h}x{w}'.format(h=self.height,w=self.width))
        #Widgets
        self.title=ttk.Label(self.window,text='Miles to km Conversion',font='Garamond 26 bold')
        self.entry_int=tk.IntVar()
        self.frame=ttk.Frame(self.window)
        self.entry=ttk.Entry(self.frame,textvariable=self.entry_int)
        self.button=ttk.Button(self.frame,text='Convert',command=self.convert)
        ##Output
        self.output_string=tk.StringVar()
        self.output=tk.Label(self.window,text='output', font='Garamond 10',textvariable=self.output_string)
        #packmethod
        self.pack()

    def convert(self):
        miles_input=self.entry_int.get()
        miles_input=miles_input*1.6
        self.output_string.set(str(int(miles_input))+' Km approx')

    def pack(self):
        
        self.title.pack()
        self.frame.pack(pady=20)
        self.entry.pack(side='left')
        self.button.pack(side='left')
        self.output.pack()
        self.window.mainloop()


App=Interface(screen_width,screen_height)