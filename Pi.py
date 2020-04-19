from tkinter import * 
import random 

#Main menu
start = open("start.txt", "r")
global sys
sys=int(start.read())
print(sys)
start.close


def menu():
	global menu 
	menu=tkinter.Tk()
	menu.title("Final Pi Project")
	menu.geometry("600x600")
	# config background and cursor
	menu.configure(background="black", cursor = "dot")

	print ("Game init. \n")



class Fighter(object):
	def __init__(self, health ,strength, ult):
		self.health = health
		self.strength = strength
		self.ult = ult
#choose your fighter 


class ninja(Fighter):
	def __init__(self, health, strength, ult)
		Fighter.__init__(self)
		self.health = 150
		self.strength = 100
	def ult(self):

	


class gunsmith(Fighter):
pass


class mage(Fighter):
pass

class tank(Fighter):
pass
#TODO: make fighter classes with unique hp power and ults 
#use tkinter GUI
