import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def bresenham_line(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1
    d = 2*dy - dx
    glVertex2f(x, y)

    while (x <= x2):
        if d >= 0:
            y += 1
            d += 2*(dy-dx)
            glVertex2f(x, y)
        elif d < 0:
            x += 1
            d += 2*dy
            glVertex2f(x, y)
        x+=1


def draw_line():
    glBegin(GL_POINTS)
    glColor3f(1.0, 0.0, 0.0)
    bresenham_line(200, 250, 450, 190)
    glEnd()


def main():
    pygame.init()
    display = (600, 400)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluOrtho2D(0, 800, 0, 600)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT)
        # Call draw line function
        draw_line()
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
