from Tkinter import *
from random import randint

class Fighter(object):
        def __init__(self, name, avatar):
                #every charachter has health bar 
        	#moves
        	#name
        	#avatar img
                self.name = name
                self.avatar = avatar
                self.health = None
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

        def setHealth(self, health):
                self._health = health
                
        #base attack function
        def attack(self):
                self._health -= 10

        #potion adds 10 hp	
        def potion(self):
                if potion == True:
                        self._health += 10
	
        #key = move/ value= health
        def addMove(self, move, dmg):
                self._moves[move] = dmg
                
        #add item to the inventory
        def addDrop(self, items):
                self.items = ["sword", "gun", "healthkit"]
                self.inventory.append(items[randint(0, len(items))])

        def __str__(self):
                s = "{} vs {}\n\n".format(self.name, self.name)

                s += "Your move set: "
                for move in self.moves.keys():
                        s += move + " - "
                s += "\n\n"

                s += "Current health: {}\n\n".format(self.health)

                s += "Enemy health: {}\n\n".format(self.health)

                return s
                
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
                c1 = Fighter("Gunsmith" , "gunsmith.gif")
                c2 = Fighter("Magician" , "magician.gif")
                c3 = Fighter("Brawler" , "brawler.gif")
                c4 = Fighter("Demolitionist", "demo.gif")
                
                #Gunsmith stats
                c1.setHealth(50)
                c1.addMove("Buckshot" , 25)
                c1.addMove("Pistol Whip" , 50)

                #Magician stats
                c2.setHealth(60)
                c2.addMove("Ace of Spades", 20)
                #Brawler stats
                c3.setHealth(100)
                c3.addMove("Flying Knee", 30)
                #Demolitionist stats
                c4.setHealth(150)
                c4.addMove("Shell Shock", 20) #20 damage but -15 health to self 
                #set character choice
                Main.character = c1

        #enemy function who you will fight 
        def enemy(self):
                pass
        	
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

                img = PhotoImage(file ="gunsmith.gif")
                imgScreen = Label(fight, image=img)
                imgScreen.pack(side=BOTTOM)
                imgScreen.pack_propagate(False)
                buttonPanel = Frame(fight)
                buttonPanel.pack(side=LEFT)
                
                attackButton = Button(buttonPanel, text="Attack", command=Fighter.attack, pady=25, width=50)
                attackButton.pack()

                potionButton = Button(buttonPanel, text="Potion", command=Fighter.potion, pady=25, width=50)
                potionButton.pack()

                statPanel = Frame(fight)
                statPanel.pack(side=RIGHT)

                statsList = Text(statPanel, bg="white")
                statsList.pack()
                statsList.insert(END, str(self.character))
                statsList.config(state=DISABLED)

                self.exit = Button(window, text="Exit", command=exit, pady=2, width=10)
                self.exit.pack(side=BOTTOM)
                
                fight.mainloop()
                
        #button commands
        #choose gunsmith
        def chooseGunsmith(self):
                self.character()
                self.fightWindow()
        
        #choose magician
        def chooseMagician(self):
                self.character()
                self.fightWindow()
        
        #choose brawler
        def chooseBrawler(self):
                self.character()
                self.fightWindow()
        
        
        #choose demolitionist
        def chooseDemo(self):
                self.character()
                self.fightWindow()
        

        		
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

                
                     
