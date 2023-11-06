from OpenGL.GL import *
from OpenGL.GLUT import *
import sys

rastersT = bytes([
    0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x3c, 0x3c, 0xff, 0xff
])

rastersC = bytes([
    0x3c, 0x7e, 0xe7, 0xc3, 0xc3, 0xc0, 0xc0, 0xc0, 0xc0, 0xc3, 0xe7, 0x7e, 0x3c
])

rastersDot = bytes([
    0x3c, 0x3c, 0x3c, 0x3c, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
])

rastersB = bytes([
    0xfe, 0xff, 0xc3, 0xc3, 0xc3, 0xc3, 0xfe, 0xfc, 0xc6, 0xc6, 0xc6, 0xfe, 0xfc
])

rastersA = bytes([
    0xc3, 0xc3, 0xc3, 0xff, 0xff, 0xc3, 0xc3, 0xc3, 0x66, 0x66, 0x24, 0x3c, 0x18,
    # ?
    0x00, 0x00, 0x30, 0x30, 0x18, 0x0c, 0x66, 0x7c, 0x38
])

rastersO = bytes([
    0x3c, 0x7e, 0xe7, 0xc3, 0xc3, 0xc3, 0xc3, 0xc3, 0xc3, 0xc3, 0xe7, 0x7e, 0x3c
])

def init():
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glClearColor(0.0, 0.0, 0.0, 0.0)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glRasterPos2i(20, 20)
    glBitmap(8, 13, 0.0, 0.0, 9.0, 0.0, rastersT)
    
    glBitmap(8, 13, 0.0, 0.0, 9.0, 0.0, rastersDot)
    glColor3f(1.0, 0.0, 0.0)
    glRasterPos2i(38, 20)
    glBitmap(8, 13, 0.0, 0.0, 9.0, 0.0, rastersC)
    glBitmap(8, 13, 0.0, 0.0, 9.0, 0.0, rastersDot)
    
    glColor3f(1.0, 1.0, 0.0)
    glRasterPos2i(56, 20)
    glBitmap(8, 13, 0.0, 0.0, 9.0, 0.0, rastersB)
    glBitmap(8, 22, 0.0, 0.0, 9.0, 0.0, rastersA)
    glBitmap(8, 13, 0.0, 0.0, 9.0, 0.0, rastersO)
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
