import pygame
from pygame.locals import *

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 250, 0)


# Define a stack data structure
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

# Initialize Pygame
pygame.init()

# Create a window
window_size = (400, 400)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Boundary Fill Algorithm")

# Initialize the stack
stack = Stack()

# Push a point onto the stack
def push(x, y):
    stack.push((x, y))

# Pop a point from the stack
def pop():
    return stack.pop()

# Boundary fill function for individual pixels
def boundary_fill(x, y, fill_color, boundary_color):
    if screen.get_at((x, y)) != fill_color and screen.get_at((x, y)) != boundary_color:
        pygame.draw.rect(screen, fill_color, (x, y, 1, 1))
        push(x, y)

# Boundary fill using stack
def boundary_fill_stack(x0, y0, fill_color, boundary_color):
    push(x0, y0)

    while not stack.is_empty():
        x, y = pop()
        boundary_fill(x - 1, y, fill_color, boundary_color)
        boundary_fill(x + 1, y, fill_color, boundary_color)
        boundary_fill(x, y + 1, fill_color, boundary_color)
        boundary_fill(x, y - 1, fill_color, boundary_color)
        boundary_fill(x + 1, y + 1, fill_color, boundary_color)
        boundary_fill(x - 1, y + 1, fill_color, boundary_color)
        boundary_fill(x + 1, y - 1, fill_color, boundary_color)
        boundary_fill(x - 1, y - 1, fill_color, boundary_color)
       
# Main function
def main():
    running = True
    screen.fill(WHITE)
    
    # Define the vertices of the polygon (change as needed)
    polygon_vertices = [(200, 100), (250, 50), (300, 100), (275, 150), (225, 150)]
    
    # Draw the filled polygon with a green boundary
    pygame.draw.polygon(screen, GREEN, polygon_vertices, 1)  # Green boundary
    boundary_fill_stack(250, 100, RED, GREEN)  # Red polygon
    
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
