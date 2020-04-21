from tkinter import *
class Fighter(object):
        def __init__(self,health,power):
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

        #add item to inventory
        def addDrop(self, inventory):
                self._inventory.append(drop)

        def __str__(self):
                #health
                h = "Health: {} \n".format(self.health)
                #damage
                h += "You dealt: {} \n".format(self.power)
                #item drop
                h += "{} was added to your inventory".format(self.inventory)
                return h

class Game(Frame):
        def __init__(self, parent):
                Fram.__init__(self,parent):
