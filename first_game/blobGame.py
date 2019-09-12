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