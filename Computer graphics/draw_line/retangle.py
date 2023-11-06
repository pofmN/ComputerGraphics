import pygame
from pygame.locals import *

from OpenGL.GL import *

def draw_rectangle():
    length = 0.8
    width = 0.3

    half_length = length / 2
    half_width = width / 2

    glBegin(GL_LINE_LOOP)
    glVertex2f(-half_length, -half_width)  # Bottom-left vertex
    glVertex2f(half_length, -half_width)  # Bottom-right vertex
    glVertex2f(half_length, half_width)  # Top-right vertex
    glVertex2f(-half_length, half_width)  # Top-left vertex
    glEnd()
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)  # Red color
    draw_rectangle()
    glFlush()


def main():
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1.0, 0.0, 0.0)  # Red color
        draw_rectangle()
        pygame.display.flip()
if __name__ == "__main__":
    main()