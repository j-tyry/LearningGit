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
    def __init__(self,parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        
    def initialize(self):
        pass

# Now we have a class, let's use it !
# We create a main which is executed when the program is run from the command-line.

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('My new app')
    # Now, we tell each program to loop with .mainloop()
    # This is call event-driven programming
    #  Because the program will do nothing but wait for events, and only react when it receives an event.
    app.mainloop()
