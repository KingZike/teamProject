from Tkinter import *
from random import randint

class Fighter(object):
        def __init__(self, health, power):
                self.health = health
                self.power = power
                self.inventory = []
                
        #setters and getters
        @property
        def health(self):
                return self._health
        
        @health.setter
        def health(self, value):
                self._health = value
                
        @property
        def power(self):
                return self._power
        
        @power.setter
        def power(self, value):
                self._power = value
                
        @property
        def inventory(self):
                return self._inventory
        
        @inventory.setter
        def inventory(self, value):
                self._inventory = value

        def __str__(self):
                #health
                h = "Health: {} \n".format(self.health)
                #damage
                h += "You dealt: {} \n".format(self.power)
                return h

class Main(Frame):
        def __init__(self, parent):
                Frame.__init__(self, parent)

                #layout of the main menu
                self.title = Label(parent, text="Welcome to Fighthon!", font=("Comic Sans", 30, "bold"), pady=30, bg="white", fg="black")
                self.title.pack()

                #starts the game
                self.start = Button(parent, text="Start Game", command=self.start, pady=20, width=100)
                self.start.pack()

                #exits the game
                self.exit = Button(parent, text="Exit", command=exit, pady=2, width=10)
                self.exit.pack(side=BOTTOM)

        #starts the game, changing the window
        def start(self):
                menu.destroy()
                window = Tk()
                window.title("Fighthon - Now Playing")
                window.configure(background = "white", cursor = "dot")
                window.attributes("-fullscreen", True)

                #exits the game
                self.exit = Button(window, text="Exit", command=exit, pady=2, width=10)
                self.exit.pack(side=BOTTOM)



        ###################
        # put all game elements below here


        
        #add item to the inventory
        def addDrop(self, items):
                self.items = ["sword", "gun", "healthkit"]
                Fighter.inventory.append(items[randint(0, len(items))])

        



                window.mainloop()
#########################################################################
# create the window
menu = Tk()
menu.title("Fighthon")
menu.geometry("800x500")
menu.configure(background="white", cursor="dot")

# create the GUI as a Tkinter canvas inside the window
g = Main(menu)

# wait for the window to close
menu.mainloop()

                
                     
