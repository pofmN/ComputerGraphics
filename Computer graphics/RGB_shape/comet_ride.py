from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

light_ambientY = [1.0, 1.0, 0.0, 1.0]
light_ambientR = [1.0, 0.0, 0.0, 1.0]
light_ambientB = [0.0, 0.5, 1.0, 1.0]

# In the PyOpenGL library, the polar regions are already on the y-axis by default, so we don't need to rotate the sphere like in the C++ code.

# Function to draw a wireframe sphere
def myWireSphere(radius, slices, stacks):
    glutWireSphere(radius, slices, stacks)

# Global variables for year and day
year = 0
day = 0

# Function to display the solar system simulation
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()

    # Draw the sun: a yellow sphere of radius 1 centered at the origin
    glMaterialfv(GL_FRONT, GL_AMBIENT, light_ambientB)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, light_ambientB)
    myWireSphere(1.0, 15, 15)

    # Draw the planet: a blue sphere of radius 0.2, 2 units away from the sun, with a white "pole" for its axis
    glRotatef(year, 0.0, 1.0, 0.0)
    glTranslatef(4.5, 0.0, 0.0)
    glRotatef(day, 0.0, 1.0, 0.0)
    glMaterialfv(GL_FRONT, GL_AMBIENT, light_ambientY)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, light_ambientY)
    myWireSphere(0.2, 15, 15)

    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    glVertex3f(0, -0.3, 0)
    glVertex3f(0, 0.3, 0)
    glEnd()

    glPopMatrix()
    glFlush()
    glutSwapBuffers()

# Function to update the view for animation
u = 0.0
du = 0.1

def timer(v):
    global u, year, day
    u += du
    day = (day + 1) % 360
    year = (year + 2) % 360
    glLoadIdentity()
    gluLookAt(20 * math.cos(u/8.0) + 12, 5 * math.sin(u/8.0) + 1, 10 * math.cos(u/8.0) + 2, 0, 0, 0, 0, 1, 0)
    glutPostRedisplay()
    glutTimerFunc(1000/60, timer, v)

# Function to reshape the window
def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(7.5, 1.0, 1.0, 40.0)
    glMatrixMode(GL_MODELVIEW)

# Main function
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"nomnom")
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
    glutDisplayFunc(display)
    glutReshapeFunc(reshape(800,600))
    glutTimerFunc(1000, timer, 0)
    glEnable(GL_DEPTH_TEST)
    glutMainLoop()

if __name__ == "__main__":
    main()
