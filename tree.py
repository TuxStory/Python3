import pygame

def draw_tree(screen,x,y): 
	pygame.draw.rect(screen, BROWN, [60+x, 170+y, 30, 45])
	pygame.draw.polygon(screen, GREEN, [[150+x,170+y],[75+x,20+y], [x,170+y]])
	pygame.draw.polygon(screen, GREEN, [[140+x,120+y], [75+x,y], [10+x,120+y]])

# Define some colors as global constants
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BROWN	 = ( 139,  69,  19)

pygame.init()

size = [700, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tree")
done = False
clock = pygame.time.Clock()

while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			done = True # Flag that we are done so we exit this loop

	screen.fill(WHITE)
	        
	draw_tree(screen,0,230)
	draw_tree(screen,67,50)
	draw_tree(screen,250,240)

	pygame.display.flip()

	clock.tick(20)

pygame.quit()

