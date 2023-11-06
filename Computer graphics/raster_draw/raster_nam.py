from OpenGL.GL import *
from OpenGL.GLUT import *
import sys

rastersN = bytes([
    0xc3, 0xcf, 0xcf, 0xdf, 0xdf, 0xdb, 0xdb, 0xfb, 0xfb, 0xf3, 0xf3, 0xe3
])

rastersA = bytes([
    0xc3, 0xc3, 0xc3, 0xc3, 0xc3, 0xff, 0xff, 0xc3, 0xc3, 0xe7, 0xff, 0xff 
])

rastersM = bytes([
    0xc3, 0xc3, 0xc3, 0xc3, 0xc3, 0xc3, 0xdb, 0xdb, 0xff, 0xe7, 0xe7, 0xc3 
])

rastersDot = bytes([
    0x3c, 0x3c, 0x3c, 0x3c, 0x00, 0x00, 0x00, 0x00
])

rastersHeart = bytes([
    0x28, 0x38, 0x7c, 0xfe, 0xfe, 0xee, 0x44
])

rastersP = bytes([
    0xc0, 0xc0, 0xc0, 0xc0, 0xc0, 0xff, 0xff, 0xc3, 0xc3, 0xc3, 0xff, 0xff
])

rastersV = bytes([
    0x18, 0x3c, 0x66, 0xe7, 0xc3, 0xc3, 0xc3, 0xc3, 0xc3, 0xc3, 0xc3, 0xc3
])

def init():
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glClearColor(0.0, 0.0, 0.0, 0.0)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glRasterPos2i(20, 20)
    glBitmap(8, 7, 0.0, 0.0, 100.0, 0.0, rastersHeart)

    glColor3f(1.0, 1.0, 0.0)
    glRasterPos2i(30, 20)
    glBitmap(8, 12, 0.0, 0.0, 9.0, 0.0, rastersP)
    glColor3f(1.0, 1.0, 0.0)

    glColor3f(1.0, 1.0, 1.0)
    glRasterPos2i(40, 20)
    glBitmap(8, 8, 0.0, 0.0, 9.0, 0.0, rastersDot)

    glColor3f(1.0, 1.0, 0.0)
    glRasterPos2i(48, 20)
    glBitmap(8, 12, 0.0, 0.0, 9.0, 0.0, rastersV)
    
    glColor3f(1.0, 1.0, 1.0)
    glRasterPos2i(58, 20)
    glBitmap(8, 8, 0.0, 0.0, 9.0, 0.0, rastersDot)

    glColor3f(1.0, 1.0, 0.0)
    glRasterPos2i(66, 20)
    glBitmap(8, 12, 0.0, 0.0, 9.0, 0.0, rastersN)
    glBitmap(8, 12, 0.0, 0.0, 9.0, 0.0, rastersA)
    glBitmap(8, 12, 0.0, 0.0, 9.0, 0.0, rastersM)

    glColor3f(1.0, 0.0, 0.0)
    glRasterPos2i(96, 20)
    glBitmap(8, 7, 0.0, 0.0, 9.0, 0.0, rastersHeart)
    glFlush()

def reshape(w, h):
    glViewport(0, 0, GLsizei(w), GLsizei(h))
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, w, 0, h, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)

def keyboard(key, x, y):
    if key == b'\x1b':
        sys.exit(0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(100, 100)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(sys.argv[0].encode())
    init()
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
