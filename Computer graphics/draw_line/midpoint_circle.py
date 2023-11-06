import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def initGL():
    pygame.init()
    display = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("DEMO THUAT TOAN VE DUONG TRON - MIDPOINT")
    display.fill((0, 0, 0))
    pygame.display.flip()

def draw8point(xc, yc, x, y):
    pygame.draw.circle(display, (255, 0, 0), (xc + x, yc + y), 1)
    pygame.draw.circle(display, (255, 0, 0), (xc + y, yc + x), 1)
    pygame.draw.circle(display, (255, 0, 0), (xc + y, yc - x), 1)
    pygame.draw.circle(display, (255, 0, 0), (xc + x, yc - y), 1)
    pygame.draw.circle(display, (255, 0, 0), (xc - x, yc - y), 1)
    pygame.draw.circle(display, (255, 0, 0), (xc - y, yc - x), 1)
    pygame.draw.circle(display, (255, 0, 0), (xc - y, yc + x), 1)
    pygame.draw.circle(display, (255, 0, 0), (xc - x, yc + y), 1)
    pygame.display.flip()

def CircleMidpoint(xc, yc, R):
    P = 5/4 - R
    y = R
    x = 0
    draw8point(xc, yc, x, y)
    while x < y:
        if P < 0:
            P += 2 * x + 3
        else:
            P += 2 * (x - y) + 5
            y -= 1
        x += 1
        draw8point(xc, yc, x, y)

def mydisplay():
    CircleMidpoint(0, 0, 200)
    pygame.display.flip()

initGL()
mydisplay()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()