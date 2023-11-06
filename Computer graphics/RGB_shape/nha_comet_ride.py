from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

light_ambientY = [1.0, 1.0, 0.0, 1.0]
light_ambientR = [1.0, 0.0, 0.0, 1.0]
light_ambientB = [0.0, 0.5, 1.0, 1.0]

# Global variable for teapot rotation angle
global_rotation_angle = 0
big_global_rotation_angle = 0

# Global variable for teapot position
pos_rotate = 0


def init():
    mat_specular = [1.0, 1.0, 1.0, 1.0]
    mat_shininess = [50.0]
    light_position = [1.0, 1.0, 1.0, 0.0]
    glShadeModel(GL_SMOOTH)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    # glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)


def draw_small_global():
    glPushMatrix()

    glTranslatef(-2, 0, pos_rotate)
    glRotatef(global_rotation_angle, 0, 1, 0)
    glTranslatef(2, 0, -pos_rotate)
    # glTranslatef(0, 0,  0)
    # glRotatef(0.04, 1, 1, 0)
    # glTranslatef(0, 0, 0)

    glutWireSphere(0.4, 20, 20)
    glColor3f(1, 0, 0)
    glBegin(GL_LINES)
    glVertex3f(0, 0.7, 0)
    glVertex3f(0, -0.7, 0)
    glEnd()
    glPopMatrix()


def draw_big_global():
    glPushMatrix()
    glRotatef(big_global_rotation_angle, 1, 0, 0)  # Rotate big_global
    glutWireSphere(1.0, 30, 30)
    glPopMatrix()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glLoadIdentity()

    gluLookAt(0, 0, 6, 0, 0, 0, 0, 1, 0)

    # Set material and lighting properties for the large sphere (blue)
    glPushMatrix()
    glTranslatef(0, 0, 0)

    glMaterialfv(GL_FRONT, GL_AMBIENT, light_ambientR)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, light_ambientR)
    draw_big_global()
    glPopMatrix()

    # Set material and lighting properties for the second small sphere (yellow)
    glPushMatrix()
    glTranslatef(2, 0, 0)

    glMaterialfv(GL_FRONT, GL_AMBIENT, light_ambientY)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, light_ambientY)

    draw_small_global()
    glPopMatrix()

    glutSwapBuffers()


def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glLoadIdentity()
    gluPerspective(65, (width / height), 1.0, 20.0)
    glMatrixMode(GL_MODELVIEW)


# glutIdleFunc(spin): function to redisplay many time
def spin():
    global global_rotation_angle, pos_rotate, big_global_rotation_angle
    pos_rotate = 1
    global_rotation_angle -= 0.04
    big_global_rotation_angle += 0.04
    glutPostRedisplay()


def stop():
    global global_rotation_angle, pos_rotate
    pos_rotate = 0
    global_rotation_angle = 0
    glutPostRedisplay()


def keyboard(key, x, y):
    global global_rotation_angle

    if key == b'a':
        glutIdleFunc(spin)
    elif key == b's':
        glutIdleFunc(stop)

    glutPostRedisplay()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Sphere")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)  # Register the keyboard callback
    glutMainLoop()


if __name__ == "__main__":
    main()