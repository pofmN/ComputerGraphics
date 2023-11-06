import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Define the vertices of the polygon
vertices_polygon = [
    (0.25, 0.25),
    (0.75, 0.25),
    (0.75, 0.75),
    (0.25, 0.75)
]

# vertices_triangle = [
#     (0.25, 0.75),
#     (0.75, 0.75),
#     (0.5, 1.0 )
# ]

def draw_polygon(vertices_polygon):
    glBegin(GL_POLYGON)
    glColor3f(1.0, 1.0, 1.0)
    for vertex in vertices_polygon:
        glVertex2fv(vertex)
    glEnd()
def draw_polygon(vertices_polygon):
    glBegin(GL_POLYGON)
    glColor3f(1.0, 1.0, 1.0)
    dlVertex2f()
    glEnd()
# def draw_triangle():
#     glBegin(GL_POLYGON) 
#     glColor3f(0.0, 1.0, 0.0)
#     for vertex in vertices_triangle:
#         glVertex2fv(vertex)
#     glEnd()



def main():
    pygame.init()
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluOrtho2D(0, 1, 0, 1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


        draw_polygon(vertices_polygon1)
        draw_polygon(vertices_polygon2)
        draw_polygon(vertices_polygon3)
        draw_polygon(vertices_polygon4)
        # draw_triangle()
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
