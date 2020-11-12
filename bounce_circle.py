"""
 Show how to use a sprite backed by a graphic.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (500, 400)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# Starting position of the rectangle
rect_x = 20
rect_y = 20
 
 # Speed and direction of rectangle
rect_change_x = 5
rect_change_y = 5
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

    # --- Game logic should go here

    # --- Drawing code should go here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, [rect_x, rect_y],15)
    pygame.draw.rect(screen, RED, [rect_x -5, rect_y -5 ,10, 10])
    rect_x += rect_change_x
    rect_y += rect_change_y
    
    # Bounce the rectangle if needed
    if rect_y > 385 or rect_y < 15:
        rect_change_y = rect_change_y * -1
    if rect_x > 485 or rect_x < 15:
        rect_change_x = rect_change_x * -1
           
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()

