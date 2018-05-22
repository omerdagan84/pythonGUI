#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import tkinter
class boiler(tkinter.Frame):
	def __init__(self, parent, label, default=""):
		tkinter.Frame.__init__(self, parent, borderwidth=3, relief="groove")

		self.timeSetText = tkinter.StringVar()
		self.timeSet = tkinter.Entry(self, textvariable=self.timeSetText, width=20)
		self.timeSet.bind("<Return>", self.OnPressEnter)
		self.timeSetText.set(u"120 min")

		self.timerVal = 3
		self.TimerDraw = tkinter.Canvas(self, bg="blue", height=parent.winfo_width(), width=parent.winfo_height())
		coord = 5, 5, (parent.winfo_width() - 5), (parent.winfo_height() - 5)
		self.timerArc = self.TimerDraw.create_arc(coord, start=0, extent=self.timerVal, fill="red")

		self.grid()
		self.timeSet.grid(column=0, row=1)
		self.TimerDraw.grid(column=0, row=2, sticky='EW')
		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=1)
		self.grid_rowconfigure(0, weight=1)
		self.grid_rowconfigure(1, weight=3)

		self.update()

	def OnPressEnter(self, event):
		print ("Enterr was pressed")
		self.timeSet.focus_set()
		self.timeSet.selection_range(0, tkinter.END)
