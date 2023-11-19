from OpenGL.GL import *
from OpenGL.GLUT import *


def draw_rectangle(x, y, width, height, color):
    glColor3fv(color)
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()


def draw_triangle(x1, y1, x2, y2, x3, y3, color):
    glColor3fv(color)
    glBegin(GL_TRIANGLES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glEnd()


def draw_house():
    # Draw background
    draw_rectangle(0, 0, 800, 700, [1.0, 0.647, 0.0])  #orange

    # Draw house shape 
    draw_rectangle(100, 200, 500, 200, [0.5, 0.49, 0.5])  #gray

    # Draw roof
    draw_triangle(50, 200, 650, 200, 450, 50, [    #pink
                  1.0, 0.16, 1.0])  

    # Draw door 
    draw_rectangle(220, 250, 90, 150, [0.6, 0.4, 0.2])  # brown
    draw_rectangle(220, 230, 90, 10, [0.6, 0.4, 0.2])  # brown

    # Draw window 
    draw_rectangle(400, 270, 150, 100, [1.0, 0.0, 0.0])  # red
    draw_rectangle(400, 230, 150, 20, [1.0, 0.0, 0.0])  # red


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_house()
    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutCreateWindow(b"House")
    glutReshapeWindow(700, 700)
    glOrtho(0, 800, 600, 0, -1, 1)
    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()