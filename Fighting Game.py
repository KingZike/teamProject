import pygame 
pygame.init()
#pygame window 

backgroud_color = (0,0,0)
(width, height) = (800, 800)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Py')
screen.fill(backgroud_color)

pygame.display.flip()


x = 50
y = 50
width = 40
height = 60
vel = 5

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	key = pygame.key.get_pressed()

	if key[pygame.K_LEFT]:
		x -= vel

	if key[pygame.K_RIGHT]:
		x += vel

	if key[pygame.K_UP]:
		y -= vel

	if key[pygame.K_DOWN]:
		y += vel	
#superclass Player 

'''class Player(object):
	def __init__(self, health, power):
		self.health = health
		self.power = power

	# Decorators

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
		self._power = value'''
''' TODO: stock image battle ground
	main character/ enemy design
	weapon design
	maybe a lil anime??? with a dable of -tion
	maybe some voice adlibs  
'''










pygame.quit()