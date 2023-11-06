import pygame
from pygame.locals import *
from OpenGL.GL import *

def draw_polygon():
    glBegin(GL_POLYGON)
    glVertex2f(100, 100)
    glVertex2f(200, 100)
    glVertex2f(200, 200)
    glVertex2f(100, 200)
    glEnd()

def boundary_fill(x, y, fill_color, boundary_color):
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()
        glReadBuffer(GL_FRONT)
        current_color = glReadPixels(x, y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE)
        current_color = current_color[::-1]  # Convert BGR to RGB

        if current_color != boundary_color and current_color != fill_color:
            glColor3ubv(fill_color)
            glBegin(GL_POINTS)
            glVertex2i(x, y)
            glEnd()
            stack.extend([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x + 1, y + 1), (x - 1, y + 1), (x + 1, y - 1), (x - 1, y - 1)])

def display_callback():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3ub(0, 255, 0)  # Boundary color (green)
    draw_polygon()
    glColor3ub(255, 0, 0)  # Fill color (red)
    boundary_fill(150, 150, (0, 0, 255), (255, 0, 0))  # Start filling from (150, 150)
    glFlush()

def main():
    pygame.init()
    pygame.display.set_mode((400, 400), DOUBLEBUF | OPENGL)
    glOrtho(0, 400, 0, 400, -1, 1)
    glClearColor(1, 1, 1, 1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        display_callback()

if __name__ == "__main__":
    main()
