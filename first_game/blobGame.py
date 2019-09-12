import pygame
pygame.init()   # Function that starts lib

win = pygame.display.set_mode((500,500))    # Window resolution
pygame.display.set_caption("Blob Game")     # Set title of game window (top left)

# Positions of object
x = 50      
y = 50

# Size of object
width = 40 
height = 60 

vel = 5     # Velocity of object moving

run = True
while run:
    pygame.time.delay(100) # Make things run a bit slower so it doesn't run too fast (in miliseconds)

    # Gets all event that pygame gets from user
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:   # If user clicks on exit button (top right of window), makes run
            run = False                 # false and stops loop, eventually running pygame.quit() which is outside of loop

pygame.quit()