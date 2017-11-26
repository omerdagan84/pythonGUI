#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import tkinter
class lightswitch(tkinter.Frame):
	def __init__(self, parent, label, default=""):
		tkinter.Frame.__init__(self, parent, borderwidth=3, relief="groove")

		self.buttonOn = tkinter.Button(self,text=u"ON", command=self.OnButtonClick, width=20)
		self.buttonOff = tkinter.Button(self,text=u"OFF", state='disabled', command=self.OffButtonClick, width=20)
		self.labelVar = tkinter.StringVar()
		self.label = tkinter.Label(self, textvariable=self.labelVar, width=20)
		self.labelVar.set(label)

		self.grid()
		self.label.grid(column=1,row=1)
		self.buttonOn.grid(column=1,row=2)
		self.buttonOff.grid(column=1,row=3)

		self.update()

	def OnButtonClick(self):
		self.buttonOn.configure(state='disabled')
		self.buttonOff.configure(state='normal')

	def OffButtonClick(self):
		self.buttonOff.configure(state='disabled')
		self.buttonOn.configure(state='normal')
