from Tkinter import *
from random import randint

class Fighter(object):
    def __init__(self, name, avatar):
        # every character has health bar
        # moves
        # name
        # avatar img
        self.name = name
        self.avatar = avatar
        self.health = None
        self.moves = {}
        self.inventory = []
        self.enemy = None

    # decorators
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
    def avatar(self, value):
        self._avatar = value

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = value

    @property
    def moves(self):
        return self._moves

    @moves.setter
    def moves(self, value):
        self._moves = value

    @property
    def inventory(self):
        return self._inventory

    @inventory.setter
    def inventory(self, value):
        self._inventory = value

    def setHealth(self, health):
        self._health = health

    # base attack function
    def attack(self):
        self.enemy.health -= 10

    # potion adds 10 hp
    def potion(self):
        if potion == True:
            self.health += 10

    # key = move/ value= health
    def addMove(self, move, dmg):
        self._moves[move] = dmg

    # add item to the inventory
    def addDrop(self, items):
        self.items = ["sword", "gun", "healthkit"]
        self.inventory.append(items[randint(0, len(items))])


    def __str__(self):
        s = ""
        if self.name != "Barbarian":
           s = "{} vs {}\n\n".format(self.name, "Barbarian")
           s += "Your move set: "
           for move in self.moves.keys():
               s += move + " - "
           s += "\n\n"

           s += "Current health: {}\n\n".format(self.health)

        else:
            s += "Their move set: "
            for move in self.moves.keys():
                s += move + " - "
            s += "\n\n"

            s += "Enemy health: {}\n\n".format(self.health)


        return s


##########################################################################################################
# the GUI and main gameplay mechanics
class Main(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.mainCharacter = None
        self.enemyChar = None

        # layout of the main menu
        self.title = Label(parent, text="Welcome to Fighthon!", font=("Comic Sans", 30, "bold"), pady=40, bg="white", fg="black")
        self.title.pack()

        # starts the game
        self.start = Button(parent, text="Start Game", command=self.start, pady=20, width=60)
        self.start.pack()

        # exits the game
        self.exit = Button(parent, text="Exit", command=exit, pady=2, width=10)
        self.exit.pack(side=BOTTOM)

    # enemy function who you will fight
    def enemy(self):
        # x = rindint(0,10)
        enemy1 = Fighter("Barbarian", "barbarian.gif")
        enemy1.setHealth(randint(50, 100))
        enemy1.addMove("Charge", 35)
        enemy1.addMove("Quick Slash", 20)
        self.enemyChar = enemy1

    def attackMove(self):
        self.enemyChar.health -= 10
        self.mainCharacter.health -= randint(1, 20)
        statsList.delete("1.0", "end")

        if self.mainCharacter.health <= 0:
            statsList.insert(END, "You lost!")
            buttonPanel.destroy()
        elif self.enemyChar.health <= 0:
            statsList.insert(END, "You Won!")
            window.destroy
        else:
            statsList.insert(END, self.mainCharacter)
            statsList.insert(END, self.enemyChar)

    # starts the game, changing the window
    # the gameplay window
    def start(self):
        global window
        menu.destroy()
        window = Tk()
        window.title("Fighthon - Now Playing")
        window.configure(background="white", cursor="arrow")
        window.attributes("-fullscreen", True)

        # blank space followed by choose your fighter text
        self.blank = Label(window, text="", pady=50, bg="white")
        self.blank.pack()

        self.choice = Label(window, text="CHOOSE YOUR FIGHTER", font=("Comic Sans", 45, "bold", "italic"), pady=75, bg="white", fg="black")
        self.choice.pack()

        # choose your fighter buttons: gunsmith, magician, brawler, or demolitionist
        self.gunsmith = Button(window, text="Gunsmith", command=self.chooseGunsmith, pady=25, width=60)
        self.gunsmith.pack()

        self.magician = Button(window, text="Magician", command=self.chooseMagician, pady=25, width=60)
        self.magician.pack()

        self.brawler = Button(window, text="Brawler", command=self.chooseBrawler, pady=25, width=60)
        self.brawler.pack()

        self.demo = Button(window, text="Demolitionist", command=self.chooseDemo, pady=25, width=60)
        self.demo.pack()

        # exits the game
        self.exit = Button(window, text="Exit", command=exit, pady=2, width=10)
        self.exit.pack(side=BOTTOM)

        window.mainloop()

    def fightWindow(self):
        global window
        window.destroy()
        fight = Tk()
        fight.title("Fighthon - In Game")
        fight.configure(background="white")
        fight.attributes("-fullscreen", True)
        self.window = window

        self.exit = Button(fight, text="Exit", command=exit, pady=2, width=10)
        self.exit.pack(side=BOTTOM)

        img = PhotoImage(file=self.mainCharacter.avatar)
        imgScreen = Label(fight, image=img)
        imgScreen.pack(side=BOTTOM)
        imgScreen.pack_propagate(False)

        img1 = PhotoImage(file=self.enemyChar.avatar)
        imgScreen1 = Label(fight, image=img1)
        imgScreen1.pack(side=RIGHT)
        imgScreen1.pack_propagate(False)

        statPanel = Frame(fight)
        statPanel.pack(side=RIGHT)

        global statsList
        statsList = Text(statPanel, bg="white")
        statsList.pack()
        statsList.insert(END, self.mainCharacter)
        statsList.insert(END, self.enemyChar)
        statsList.config(state=DISABLED)

        global buttonPanel
        buttonPanel = Frame(fight)
        buttonPanel.pack(side=LEFT)

        attackButton = Button(buttonPanel, text="Attack", command=self.attackMove, pady=25, width=50, state=ACTIVE)
        attackButton.pack()

        potionButton = Button(buttonPanel, text="Potion", command=self.mainCharacter.potion, pady=25, width=50)
        potionButton.pack()

        statPanel = Frame(fight)
        statPanel.pack(side=RIGHT)

        fight.mainloop()

    # button commands
    # choose gunsmith
    def chooseGunsmith(self):
        c1 = Fighter("Gunsmith", "gunsmith.gif")

        # Gunsmith stats
        c1.setHealth(50)
        c1.addMove("Buckshot", 25)
        c1.addMove("Pistol Whip", 50)

        self.enemy()
        c1.enemy = self.enemyChar
        self.mainCharacter = c1
        self.fightWindow()

    # choose magician
    def chooseMagician(self):
        c2 = Fighter("Magician", "magician.gif")
        Main.character = c2

        # Magician stats
        c2.setHealth(75)
        c2.addMove("Ace of Spades", 20)

        self.enemy()
        self.mainCharacter = c2
        self.fightWindow()

    # choose brawler
    def chooseBrawler(self):
        c3 = Fighter("Brawler", "brawler.GIF")

        # Brawler stats
        c3.setHealth(100)
        c3.addMove("Flying Knee", 30)

        self.enemy()
        self.mainCharacter = c3
        self.fightWindow()

    # choose demolitionist
    def chooseDemo(self):
        c4 = Fighter("Demolitionist", "demo.gif")

        # Demolitionist stats
        c4.setHealth(150)
        c4.addMove("Shell Shock", 20)  # 20 damage but -15 health to self

        self.enemy()
        self.mainCharacter = c4
        self.fightWindow()

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
