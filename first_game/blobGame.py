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
    

    keys = pygame.key.get_pressed()     # Gets all keys pressed and stores it into a list

    # If these key arrows are moved, update position of object
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    win.fill((0,0,0))   # Fill screen before drawing another one to not create a mess
    pygame.draw.rect(win, (0, 255, 100), (x, y, width, height))  # Creates the rectangle shape on window surface
    pygame.display.update()     # Updates window to put shape on window

pygame.quit()   # Closes window and exits program