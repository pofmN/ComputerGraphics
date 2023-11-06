import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
import math

def initGL():
    glClearColor(0.8, 0.8, 0.8, 1.0)  # R=0.8, G=0.8, B=0.8, Alpha=1
    glOrtho(-30, 30, -30, 30, -1, 1)

def mydisplay():
    step = 2 * 3.14 / 10
    angle = 0.0
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 0.0)  # Yellow
    glBegin(GL_POLYGON)
    for i in range(10):
        if (i % 2 == 1):
            glVertex3f(25 * math.cos(angle), 25 * math.sin(angle), 0.0)
        else:
            glVertex3f(12 * math.cos(angle), 12 * math.sin(angle), 0.0)
        angle += step
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow("Filled Star")

    glutDisplayFunc(mydisplay)
    initGL()
    glutMainLoop()

if __name__ == "__main__":
    main()
