from Tkinter import *
from random import randint

class Fighter(object):
        def __init__(self, name, health, avatar):
        	#every charachter has health bar 
        	#moves
        	#name
        	#avatar img
			self.name = name
			self.avatar = avatar
			self.health = health
			self.moves = {}
			self.inventory = []
       #decorators
        @property
        def name(self):
        	return self._name
        @name.setter
        def name(self, value):
        	self._name = value
        @property
        def avatar(self):
        	return self._avatar
        @avatar.setter
        def avatar(self,value):
        	self._avatar = value
        @property
        def health(self):
        	return self._health
        @health.setter
        def health(self,value):
        	self._health = value
        @property
        def moves(self):
        	return self._moves
        @moves.setter
        def moves(self,value):
        	self._moves = value
        @property
        def inventory(self):
        	return self._inventory
        @inventory.setter
        def inventory(self,value):
        	self._inventory = value
                
        #base attack function
		def attack(self):
       		self._health -= 10
       	#potion adds 10 hp
        def potion(self):
			self._health += 10
		#key = move/ value= health
		def moveSet(self, moves, health)
			self._moves[moves] = health
		#add item to the inventory
		def addDrop(self, items):
			self.items = ["sword", "gun", "healthkit"]
			Fighter.inventory.append(items[randint(0, len(items))])
#the fighter classes
##########################################################################################################
# we need at least 2 of these done by the demo date
#the GUI and main gameplay mechanics
class Main(Frame):
        def __init__(self, parent):
                Frame.__init__(self, parent)

                #layout of the main menu
                self.title = Label(parent, text="Welcome to Fighthon!", font=("Comic Sans", 30, "bold"), pady=40, bg="white", fg="black")
                self.title.pack()

                #starts the game
                self.start = Button(parent, text="Start Game", command=self.start, pady=20, width=60)
                self.start.pack()

                #exits the game
                self.exit = Button(parent, text="Exit", command=exit, pady=2, width=10)
                self.exit.pack(side=BOTTOM)
        def character(self):
        	c1 = "Gunsmith" , #image
        	c2 = "Magician" , #image
        	c3 = "Brawler" , #image
        	c4 = "Demolitionist", #image
        	#Gunsmith stats
        	c1.health = 50
        	c1.moveSet = "QuickShot" , -25
        	c1.moveSet = "NO SCOPE" , -50
        	#TODO: c2 - c4
        #starts the game, changing the window
        #the gameplay window
        def start(self):
                global window
                menu.destroy()
                window = Tk()
                window.title("Fighthon - Now Playing")
                window.configure(background = "white", cursor = "arrow")
                window.attributes("-fullscreen", True)

                #blank space followed by choose your fighter text
                self.blank = Label(window, text="", pady=50, bg="white")
                self.blank.pack()
                
                self.choice = Label(window, text="CHOOSE YOUR FIGHTER", font=("Comic Sans", 45, "bold", "italic"), pady=75, bg="white", fg="black")
                self.choice.pack()

                #choose your fighter buttons: gunsmith, magician, brawler, or demolitionist
                self.gunsmith = Button(window, text="Gunsmith", command=self.chooseGunsmith, pady=25, width=60)
                self.gunsmith.pack()

                self.magician = Button(window, text="Magician", command=self.chooseMagician, pady=25, width=60)
                self.magician.pack()

                self.brawler = Button(window, text="Brawler", command=self.chooseBrawler, pady=25, width=60)
                self.brawler.pack()

                self.demo = Button(window, text="Demolitionist", command=self.chooseDemo, pady=25, width=60)
                self.demo.pack()

                #exits the game
                self.exit = Button(window, text="Exit", command=exit, pady=2, width=10)
                self.exit.pack(side=BOTTOM)

                window.mainloop()

        def fightWindow(self):
                global window 
                window.destroy()
                fight = Tk()
                fight.title("Fighthon - In Game")
                fight.configure(background = "white")
                fight.attributes("-fullscreen", True)

                img = None
                imgScreen = Label(fight, image=img)
                imgScreen.pack(side=TOP)

                buttonPanel = Frame(fight)
                buttonPanel.pack(side=LEFT)
                
                attackButton = Button(buttonPanel, text="Attack", command=self.attack, pady=25, width=50)
                attackButton.pack()

                defendButton = Button(buttonPanel, text="Defend", command=self.defend, pady=25, width=50)
                defendButton.pack()

                potionButton = Button(buttonPanel, text="Potion", command=self.potion, pady=25, width=50)
                potionButton.pack()

                statPanel = Frame(fight)
                statPanel.pack(side=RIGHT)

                statsList = Text(statPanel, bg="white")
                statsList.pack()
                statsList.insert(END, "big bologna")
                statsList.config(state=DISABLED)

                global character
                
                fight.mainloop()
                
        #button commands
        #choose gunsmith
        def chooseGunsmith(self):
                global character
                character = "Gunsmith"

                self.fightWindow()
        
        #choose magician
        def chooseMagician(self):
                global character
                character = "Magician"

                self.fightWindow()
        
        #choose brawler
        def chooseBrawler(self):
                global character
                character = "Brawler"

                self.fightWindow()
        
        #choose demolitionist
        def chooseDemo(self):
                global character
                character = "Demolitionist"

                self.fightWindow()

        def fighterStatus(self, enemy):
        	#print status
        	#pack to the right 



        	while (self.health > 0) and (enemy.health > 0):
        		#print staus of fighters while both are alive
        		print "{self.name}\t\t\Health\t{self.health}"
        		print "{enemy.name}\t\t\Health\t{enemy.health}"
        ###################
        # put all game elements below here


        


                

        



                
                
#########################################################################
# create the window
menu = Tk()
menu.title("Fighthon")
menu.geometry("800x500")
menu.configure(background="white", cursor="arrow")

# create the GUI as a Tkinter canvas inside the window
g = Main(menu)

# wait for the window to close
menu.mainloop()

                
                     
