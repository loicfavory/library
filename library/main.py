#!/usr/bin/python

import Tkinter as Tkt


class libraryAppTk(Tkt.Tk):
    def __init__(self, parent):
        Tkt.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self['bg'] = 'white'
        self.grid()

        # frame 1
        self.firstFrame = Tkt.Frame(self, borderwidth=2, relief=Tkt.GROOVE)
        self.firstFrame.pack(side=Tkt.LEFT, padx=30, pady=30)
        # frame 2
        self.secondFrame = Tkt.Frame(self, borderwidth=2, relief=Tkt.GROOVE)
        self.secondFrame.pack(side=Tkt.LEFT, padx=30, pady=30)
        self.definitionScroll = Tkt.Scrollbar(self.secondFrame)

        self.entryVariable = Tkt.StringVar()
        self.entry = Tkt.Entry(self.firstFrame, textvariable=self.entryVariable)
        self.entry.grid(column=0, row=0, sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entry.bind("<FocusIn>", self.OnEntryClick)
        self.entryVariable.set(u"Enter text here.")

        button = Tkt.Button(self.secondFrame, text=u"Click me !", command=self.OnButtonClick)
        button.grid(column=0, row=0)

        self.label = Tkt.Text(self.secondFrame, width=30, height=4,
                             fg="white", bg="blue", yscrollcommand=self.definitionScroll.set)
        self.label.grid(column=0, row=1, sticky='EW')
        self.setText(u"Hello !")

        self.grid_columnconfigure(0, weight=1)

        self.resizable(True, False)
        self.update()
        self.geometry(self.geometry())
        self.firstFrame.grid_propagate(False)
        self.secondFrame.grid_propagate(False)
        self.FocusInEntry()

    def setText(self, text):
        self.label.delete("1.0", Tkt.END)   # an example of how to delete all current text
        self.label.insert("1.0", text) # an example o

    def FocusInEntry(self):
        self.entry.focus_set()
        self.entry.selection_range(0, Tkt.END)

    def OnButtonClick(self):
        self.setText(self.entryVariable.get() + " (You clicked the button)")
        self.FocusInEntry()

    def OnPressEnter(self, event):
        self.setText(self.entryVariable.get() + " (You pressed enter)")
        self.FocusInEntry()

    def OnEntryClick(self, event):
        self.FocusInEntry()


if __name__ == "__main__":
    app = libraryAppTk(None)
    app.title('My library')
    app.mainloop()
