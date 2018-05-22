#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import tkinter
class irregation(tkinter.Frame):
	def __init__(self, parent, label, default=""):
		tkinter.Frame.__init__(self, parent, borderwidth=3, relief="groove")

		self.labelVar = tkinter.StringVar()
		self.label = tkinter.Label(self, textvariable=self.labelVar, width=20)
		self.labelVar.set(label)

		self.value = 3
		self.irrBar = tkinter.Canvas(self, bg="blue")#, height=parent.winfo_width()/4, width=parent.winfo_height()/4)

		self.grid()
		self.label.grid(column=0, row=1)
		self.irrBar.grid(column=0, row=2, sticky='EW')
		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure(0, weight=1)
		self.grid_rowconfigure(1, weight=3)

		self.update()

	def OnPressEnter(self, event):
		print ("Enterr was pressed")
		self.timeSet.focus_set()
		self.timeSet.selection_range(0, tkinter.END)
