from OpenGL.GL import *
from OpenGL.GLUT import *
import math

r, g, b, x, y = 0.0, 0.0, 0.0, 0, 0
flag = True
color_order = 0

def mouse(button, state, mousex, mousey):
    global flag, x, y, color_order
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        flag = True
        x = mousex
        y = 600 - mousey
        if color_order > 4:
            color_order = 0
        color_order += 1
    # elif button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
    #     glutPostRedisplay()

def keyboard(key, x, y):
    if key == b'\x1b':
        glutHideWindow()

def display():
    global flag, x, y, color_order
    angle_theta = 0.0
    if color_order == 1:
        glColor3f(1.0, 0.0, 0.0)
    elif color_order == 2:
        glColor3f(0.0, 1.0, 0.0)
    elif color_order == 3:
        glColor3f(0.0, 1.0, 1.0)
    elif color_order == 4:
        glColor3f(1.0, 0.0, 1.0)
    elif color_order == 5:
        glColor3f(0.0, 0.5, 1.0)
    elif color_order == 5:
        glColor3f(0.6, 0.5, 1.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 800.0, 0.0, 600.0, -1.0, 1.0)

    if flag:
        glBegin(GL_POLYGON)
        for i in range(360):
            angle_theta = i * 3.142 / 180
            glVertex2f(x + 50 * math.cos(angle_theta), y + 50 * math.sin(angle_theta))
        glEnd()
    glFlush()

def main():
    global color_order
    glutInit(sys.argv)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(100, 100)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutCreateWindow(b"Circle Creation on mouse click")
    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glutDisplayFunc(display)
    glutMouseFunc(mouse)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()
