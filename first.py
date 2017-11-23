#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import tkinter

class simpleapp_tk(tkinter.Tk):     #app defined as a class
    def __init__(self,parent):          #define the init function of the class
        tkinter.Tk.__init__(self,parent)    #call the tkinter initializer
        self.initialize()                   #call the app initializer

    def initialize(self):   #the app initializer function           

        #call the grid layout manager
        #this enables us to arrange the objects on a grid 
        self.grid()

        #create a text box 'Entry' set parent as self
        #note that we keep a referance of it
        self.entry = tkinter.Entry(self)
        #place the item on the grid at location 0,0 stick to left and right
        self.entry.grid(column=0,row=0,sticky='EW')

        #create a button
        #set parent to self and set the text
        button = tkinter.Button(self,text=u"Click me !")
        #place the item on the grid at location 0,1 
        button.grid(column=1,row=0)

        #create a label 
        #anchor - sets text alignment to left
        #fg - foreground color bg - background color
        label = tkinter.Label(self,anchor="w",fg="white",bg="blue")
        #place the item on the grid at location 1,0 spanning on two columns 
        label.grid(column=0,row=1,columnspan=2,sticky='EW')

if __name__ == "__main__":
    app = simpleapp_tk(None)    #start the app
    app.title('my application') #set the window lable
    app.mainloop()              #call mainloop
