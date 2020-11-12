import pygame

def draw_damier(screen):
	x=50
	y=0
	for l in range(8):
		for i in range(4):
			pygame.draw.rect(screen, BLACK, [x, y, 50, 50])
			x =x+100
			i =+ 1
		if l%2 == 0:
			x=0
		else:
			x=50
		y =y+50
		l =+ 1

# Define some colors as global constants
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BROWN	 = ( 139,  69,  19)
#Image
Tux = pygame.image.load("Tux.png")

#pygame.init()
#semble prendre énormement de processuer

size = [400, 400]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("damier")
done = False
clock = pygame.time.Clock()
TX = 0 ; TY = 0

while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			done = True # Flag that we are done so we exit this loop
		#Keyboard
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				TX = TX - 50
				if TX < 0:
					TX = 0
			elif event.key == pygame.K_RIGHT:
				TX = TX + 50
				if TX > 350:
					TX = 350
			elif event.key == pygame.K_UP:
				TY = TY - 50
				if TY < 0:
					TY = 0
			elif event.key == pygame.K_DOWN:
				TY = TY + 50
				if TY > 350:
					TY = 350
	screen.fill(WHITE)
	draw_damier(screen)
	screen.blit(Tux,(TX,TY)) #Code pour imprimer l'image
	pygame.display.flip()

	clock.tick(20)

pygame.quit()

