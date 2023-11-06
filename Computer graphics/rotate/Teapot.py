import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Initialize Pygame
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

teapot_scale = 1.0
rotation_x = 0.0
rotation_y = 0.0

def teapot():
    glPushMatrix()
    glutSolidTeapot(1.0)
    glPopMatrix()

def wire_teapot():
    glPushMatrix()
    glutWireTeapot(1.0)
    glPopMatrix()

def scale_teapot(scale_factor):
    glScale(scale_factor, scale_factor, scale_factor)

def main():
    global teapot_scale, rotation_x, rotation_y

    glutInit()  # Initialize GLUT
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    rotation_x += 5
                elif event.key == pygame.K_DOWN:
                    rotation_x -= 5
                elif event.key == pygame.K_LEFT:
                    rotation_y += 5
                elif event.key == pygame.K_RIGHT:
                    rotation_y -= 5
                elif event.key == pygame.K_s:
                    teapot_scale += 0.1
                elif event.key == pygame.K_d:
                    teapot_scale -= 0.1

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        glTranslatef(0.0, 0.0, -5)
        glRotate(rotation_x, 1, 0, 0)
        glRotate(rotation_y, 0, 1, 0)

        scale_teapot(teapot_scale)

        teapot()
        wire_teapot()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
