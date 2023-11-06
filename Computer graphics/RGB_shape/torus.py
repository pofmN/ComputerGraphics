from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Clears the window and draws the torus.
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    
    glColor3f(1.0, 1.0, 1.0)
    glutWireTorus(0.5, 3, 15, 30)
    
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(10, 0, 0)
    glColor3f(0, 1, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 10, 0)
    glColor3f(0, 0, 1)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, 10)
    glEnd()
    
    glFlush()

def init():
    # Set the current clear color to black and the current drawing color to white.
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glColor3f(1.0, 1.0, 1.0)
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(70.0, 4.0 / 3.0, 1, 40)
    
    # Position camera at (4, 6, 5) looking at (0, 0, 0) with the vector <0, 1, 0> pointing upward.
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(12, 10, 10, 0, 0, 0, 0, 1, 0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(80, 80)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Torus Nom")
    glutDisplayFunc(display)
    init()
    glutMainLoop()

if __name__ == "__main__":
    main()
