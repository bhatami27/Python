import pygame, sys
import math
from pygame.locals import *
import random as rn
pygame.init()

BLUE = (0,0,255)
WHITE = (255,255,255)
 
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)

pygame.display.set_caption('S-Triangle')

#INPUT takes a location loc = (x,y) pair of points and width
#RETURN 3 points of the equilateral triangle determined by loc and width
def triangle(loc,width):
    #pass
    x = loc[0]
    y = loc[1]
    #TODO: Implement function    
    z = math.sqrt(pow(width, 2) - pow(width/2, 2))
    
    top = (width/2 + x, y)
    left = (x,y + z)
    right = (width + x, y + z)

    return (top, left, right)


DISPLAYSURF.fill(WHITE)

#Draws Triangle
#(triangle(loc,w)) is a tuple of tuples...)
def draw_triangle(loc, w):
    r = rn.randint(0, 255)
    g = rn.randint(0, 255)
    b = rn.randint(0, 255)
    color = (r,g,b)
    pygame.draw.polygon(DISPLAYSURF, color , (triangle(loc,w)),1)

#INPUT location and width
#RETURN nothing -- follows algorithm
def s(loc,width):
    #pass
    #TODO: Implement Function
    #Relies on triangle
    #1) draw current triangle | 2) call triangle() to get coords of next three
    # triangles, 3) call s() on the 3 new coords
    if width > 1:
        z = math.sqrt(pow(width, 2) - pow(width/2, 2))
        draw_triangle(loc, width)
       
        x = loc[0]
        y = loc[1]
        
        top = [x + width / 4, y]
        left = [x, z/2 + y]
        right = [x + width/2, y + z/2]
        
        s(top,width/2)
        s(left, width / 2)
        s(right, width / 2)
       
    else:
        return
    
s((0,0),440)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
