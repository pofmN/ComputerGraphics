from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_teapot():
    glutSolidTeapot(0.5)  # Draw a solid teapot with a scale factor of 0.5

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 3, 0, 0, 0, 0, 1, 0)  # Set the camera position

    draw_teapot()

    glutSwapBuffers()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (width / height), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Teapot Example")
    glEnable(GL_DEPTH_TEST)

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)

    glClearColor(0.0, 0.0, 0.0, 1.0)  # Set the clear color to black

    glutMainLoop()

if __name__ == "__main__":
    main()
