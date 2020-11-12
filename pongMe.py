import pygame
import random

# Define some colors as global constants
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

class Player(pygame.sprite.Sprite):
	""" This class represents the bar at the bottom that the player controls """

	# Set speed vector
	change_y = 0

	def __init__(self,x,y):
		""" Constructor function """

        # Call the parent's constructor
		super().__init__()

        # Set height, width
		self.image = pygame.Surface([10, 70])
		self.image.fill(WHITE)

		# Make our top-left corner the passed-in location.
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.x = x

	def changespeed(self, y):
		""" Change the speed of the player. Called with a keypress. """
		self.change_y += y

	def move(self):
		""" Find a new position for the player """
        # Move up/down
		self.rect.y += self.change_y

class Ball(pygame.sprite.Sprite):
	# Speed and direction of the ball
	ball_change_x = 9
	ball_change_y = 9

	def __init__(self,ball_x,ball_y):
		""" Constructor function """

        # Call the parent's constructor
		super().__init__()

        # Set height, width
		self.image = pygame.Surface([5, 5])
		self.image.fill(WHITE)

		# Make our top-left corner the passed-in location.
		self.rect = self.image.get_rect()
		pygame.draw.circle(screen, WHITE, [ball_x, ball_y],5)
		self.rect.y = ball_y
		self.rect.x = ball_x
	
	def move(self):
		# Move the rectangle starting point
		self.rect.x += self.ball_change_x
		self.rect.y += self.ball_change_y
		# Bounce the ball if needed
		if self.rect.y > 500 or self.rect.y < 0:
			self.ball_change_y = self.ball_change_y * -1
		# Replace the ball if out
		if self.rect.x > 700 or self.rect.x < 0:
			self.ball_change_x = self.ball_change_x * -1 #Bounced
			r = random.randint(10,490)
			self.rect.x = r
			
	def	rebondir(self):
		self.ball_change_x = self.ball_change_x * -1

def checkCollision(sprite1, sprite2):
	col = pygame.sprite.collide_rect(sprite1, sprite2)
	return col
			
pygame.init()
#semble prendre énormement de processeur

#------------------ Construction ---------------------
size = [700, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PongMe")

player = Player(10,250)
adversaire = Player(680,250)
ball = Ball(250,350)

adversaire.changespeed(9) #Speed of Adversaire
movingsprites = pygame.sprite.Group()
movingsprites.add(player)
movingsprites.add(adversaire)
movingsprites.add(ball)

myfont1 = pygame.font.SysFont("Comic Sans MS", 100)
pl_score = 0 
ad_score = 0

done = False
clock = pygame.time.Clock()

#----------------------- Boucle --------------------------

while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			done = True # Flag that we are done so we exit this loop
		#Keyboard
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				player.changespeed(-5)
			if event.key == pygame.K_DOWN:
				player.changespeed(5)

#----------------------- Move -------------------------

	player.move()
	if player.rect.y < 0:
		player.rect.y = 0
	if player.rect.y > 430:
		player.rect.y = 430

	adversaire.move()
	if adversaire.rect.y > 430:
		adversaire.change_y = adversaire.change_y * -1
	if adversaire.rect.y < 0:
		adversaire.change_y = adversaire.change_y * -1

	ball.move()

# ----------------------- Terrain -------------------
	screen.fill(BLACK)
	movingsprites.draw(screen)
	pygame.draw.lines(screen, WHITE, False, [(350,0), (350,500)], 1)

# ------------------------ Logique --------------------	
	boum = checkCollision(player,ball) 
	if boum == True:
		ball.rebondir()
	
	boum2 = checkCollision(adversaire,ball)
	if boum2 == True:
		ball.rebondir()

# ------------------------ Score -----------------------

	label1 = myfont1.render(str(pl_score), 1,WHITE)
	label2 = myfont1.render(str(ad_score), 1,WHITE)
	screen.blit(label1, (175, 10))
	screen.blit(label2, (525, 10))
	if ball.rect.x >= 695:
		pl_score += 1
	if ball.rect.x <= 5:
		ad_score += 1
# -------------------------------------------------------	
	pygame.display.flip()
	clock.tick(20)

pygame.quit()

