'''
author jean-thierry roy
date 2014-06-15
'''

import Tkinter

# creating a simple Tkinter window.
# tutorial from http://sebsauvage.net/python/gui/
# It's best to put our application in a class. 
# In Tkinter, we inherit from Tkinter.Tk, which is the base class for standard windows.

class simpleapp_tk(Tkinter.Tk):
    '''Tkinter class for a simple UI'''
    def __init__(self,parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        # layout
        self.grid()
        # add some text entry
        self.entry = Tkinter.Entry(self)
        self.entry.grid(column=0,row=0,sticky='EW')
        # add an event handler to the text entry, using the bind method and assigning a self.def(method)
        self.entry.bind("<Return>", self.on_press_enter)
        
        # add a button
        button = Tkinter.Button(self,text=u"I'm a button!",command=self.on_button_click)
        button.grid(column=1,row=0)
        
        # add a label
        self.labelVariable = Tkinter.StringVar()
        self.labelVariable.set("Enter a text and return or press the button...")
        label = Tkinter.Label(self, textvariable=self.labelVariable, anchor="w", fg="white", bg="blue")
        label.grid(column=0,row=1,columnspan=2,sticky="EW")
                
        # enable resizing
        self.grid_columnconfigure(0,weight=1)
        self.resizable(True, False)

    def on_press_enter(self,event):
        print "Pressed enter!"
        self.labelVariable.set("Pressed enter!")

    def on_button_click(self):
        print "Button's clicked!"
        self.labelVariable.set("Button's clicked!")

# Now we have a class, let's use it !
# We create a main which is executed when the program is run from the command-line.

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('My new app')
    # Now, we tell each program to loop with .mainloop()
    # This is call event-driven programming
    #  Because the program will do nothing but wait for events, and only react when it receives an event.
    app.mainloop()
