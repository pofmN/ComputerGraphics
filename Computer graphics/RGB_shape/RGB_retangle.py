from OpenGL.GL import *
from OpenGL.GLUT import *

def mydisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0, 1)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(1, -1)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(-1, -1)
    glEnd()

    glFlush()

def main():
    glutInit(sys.argv)
    glutCreateWindow(b"segitiga")
    glutDisplayFunc(mydisplay)
    glutMainLoop()

if __name__ == "__main__":
    main()
