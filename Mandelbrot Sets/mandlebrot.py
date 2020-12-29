import math
import pygame
import sys

most = 80
Iter_present = 0

def mandlebrot(c):

    point = 0
    Val = [0,0]
    Iter_present = 0

    while(point <2 and Iter_present < most):

        RL = ( Val[0] * Val[0] ) - ( Val[1] * Val[1] )
        IMG = ( Val[0] * Val[1] ) + ( Val[0] * Val[1] )

        Val = [ RL, IMG ]

        Val[0] = ( Val[0] + c[0] )
        Val[1] = ( Val[1] + c[1] )

        point = math.sqrt( Val[0]**2 + Val[1]**2 )
        
        Iter_present += 1

    if Iter_present == most:
        return -1
        
    else:
        return (Iter_present)

print(mandlebrot([.5,.5]))

pygame.init()

blk = ( 0, 0, 0 )
r = ( 255, 0, 0 )
w = ( 255, 255, 255 )
blu = ( 0, 0, 255 )
g = ( 0, 255, 0 )
p = ( 128, 0, 128 )
y = ( 255, 255, 0 )



size = [900,600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Mandelbrot')
screen.fill(w)
pixar = pygame.PixelArray(screen)

for i in range( -150, 150 ):

    for j in range( -150, 150 ):
        c = ( i/150, j/150 )
        v = mandlebrot(c)

        if v == -1:
            pixar[ i+150, j+150 ] = y

        else:
            pixar[ i+150, j+150 ] = blk

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
