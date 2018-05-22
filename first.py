#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import tkinter
from lightswitch import lightswitch
from boiler import boiler
from irrigation import irregation

class simpleapp_tk(tkinter.Tk):     #app defined as a class
    def __init__(self,parent):          #define the init function of the class
        tkinter.Tk.__init__(self,parent)    #call the tkinter initializer
        self.initialize()                   #call the app initializer

    def initialize(self):   #the app initializer function           
#        w = 900 
#        h = 900
#        sw = self.winfo_screenwidth()
#        sh = self.winfo_screenheight()
#        x = (sw - w)/2
#        y = (sh - h)/2
#        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

        #call the grid layout manager
        #this enables us to arrange the objects on a grid 
        self.grid()

#        self.C = tkinter.Canvas(self, bg="blue", height=250, width=300)

        #create a text box 'Entry' set parent as self
        #create a string variable
        self.barframe = tkinter.Frame(self)
        self.entryVariable = tkinter.StringVar()
        #note that we keep a referance of it - bind the string variable
        self.entry = tkinter.Entry(self.barframe,textvariable=self.entryVariable)
        #place the item on the grid at location 0,0 stick to left and right
        self.entry.grid(column=0,row=0,columnspan=2,sticky='EW')
        #bind a <return> press to the function OnPressEnter
        self.entry.bind("<Return>", self.OnPressEnter)
        #set the initial string variable value
        self.entryVariable.set(u"Enter text here.")

        #create a button
        #set parent to self and set the text - bind click to function
        self.button = tkinter.Button(self.barframe,text=u"Click me !", command=self.OnButtonClick)
        #place the item on the grid at location 0,1 
        self.button.grid(column=1,row=0)

        #create a label 
        self.labelVariable = tkinter.StringVar()
        #anchor - sets text alignment to left
        #fg - foreground color bg - background color
        label = tkinter.Label(self.barframe,textvariable=self.labelVariable,anchor="w",fg="white",bg="blue")
        #place the item on the grid at location 1,0 spanning on two columns 
        label.grid(column=0,row=1,columnspan=3,sticky='EW')
        self.labelVariable.set(u"Hello !")

        #allow resizing on the columns
        self.grid_rowconfigure(1,weight=1)
        self.grid_rowconfigure(1,weight=3)
        self.grid_rowconfigure(2,weight=3)
        #restrict resizing only on the horizontal axes
        self.resizable(True,True)
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)

 #       self.C.grid(column=0, rows=2, columnspan=3)
        self.barframe.grid(row=0, sticky='EW')

        self.lightsframe = tkinter.Frame(self)
        self.lightsframe.grid(row=1, sticky='EW')
        #self.lightsframe.grid_rowconfigure(0, weight=1)
        #self.lightsframe.grid_columnconfigure(0, weight=1)
        self.custom1 = lightswitch(self.lightsframe, "Living room", "test")
        self.custom1.grid(column=0, row=1)
        self.custom2 = lightswitch(self.lightsframe, "Kitchen", "test")
        self.custom2.grid(column=1, row=1)
        self.custom3 = lightswitch(self.lightsframe, "Balcony", "test")
        self.custom3.grid(column=2, row=1)

        self.boilerirrframe = tkinter.Frame(self)
        self.boilerirrframe.grid(row=2, sticky='EW')
        self.boiler = boiler(self.boilerirrframe, "test", "test")
        self.boiler.grid(column=0, row=1, sticky='E')
        self.irr1 = irregation(self.boilerirrframe, "balcony1", "balcony1")
        self.irr1.grid(column=1, row=1, sticky='E')
        self.irr2 = irregation(self.boilerirrframe, "balcony1", "balcony1")
        self.irr2.grid(column=2, row=1, sticky='E')
        #set the windows geometry to the geometry set by its widgets
        #this fixes a resizing glitch where the window will keep resizing
        #for example if you enter a very long text
        self.update()
        self.geometry(self.geometry())       
        self.count = 5
        self.arc = 0

    def OnButtonClick(self):
        print ("You clicked the button !")
        self.labelVariable.set( self.entryVariable.get()+" (You clicked the button)" )
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)
        self.C.delete(self.arc)
        coord = 10, 50, 240, 240
        self.arc = self.C.create_arc(coord, start=0, extent=self.count, fill="red")
        self.count += 15
        if (self.count > 180):
            self.count = 5
        self.C.update_idletasks
        self.button.configure(state='disabled')
        self.update()


    def OnPressEnter(self,event):
        print ("You pressed enter ")
        self.labelVariable.set( self.entryVariable.get()+" (You pressed ENTER)" )
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)
        self.button.configure(state='active')


if __name__ == "__main__":
    app = simpleapp_tk(None)    #start the app
    app.title('my application') #set the window lable
#    app.wm_geometry("600x600")
    app.mainloop()              #call mainloop
