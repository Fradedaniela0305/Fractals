import random
import pygame
import time

WIDTH, HEIGHT = 600, 600
TOP = (WIDTH / 2, 50)
LEFT = (50, HEIGHT - 50)
RIGHT = (WIDTH - 50, HEIGHT - 50)
corners = [TOP, LEFT, RIGHT]
COLOR = (0, 0, 0)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
REPETITIONS = 30000

pygame.init()
pygame.mixer.init()

def initialize_screen():
    """
    PURPOSE: Initialize the screen for drawing a Sierpinski triangle.
    REQUIRES: Pygame is initialized and global variable SCREEN is defined.
    MODIFIES: Fills the screen with white background and sets window caption.
    EFFECTS: Updates display so the window shows a white screen with the title 'Sierpinski Triangle'.
    """
    pygame.display.set_caption('Sierpinski Triangle')
    SCREEN.fill((255, 255, 255))
    pygame.display.flip()

def compute_coordinate(coordinate_1, coordinate_2):
    """
    PARAMETER: Consumes two coordinates of screen as numbers
    EFFECTS: Computes the midpoint between two points
    """
    return (coordinate_1 + coordinate_2) / 2

def get_new_point(start):
    """
    PARAMETER: Consumes a tuple with coordinates (x, y) that must be inside the triangle
    REQUIRES: Global variable corners should be initialized
    EFFECTS: Computes new point for Sierpinski triangle and returns it
    """
    corner = random.choice(corners)
    x1, y1 = start
    x2, y2 = corner
    point_x = compute_coordinate(x1, x2)
    point_y = compute_coordinate(y1, y2)
    return int(point_x), int(point_y)

def place_point(point):
    """
    PARAMETER: Consumes a tuple with coordinates (x, y)
    REQUIRES: Global variable COLOR is defined
    MODIFIES: Pygame screen and buffer
    EFFECTS: Places new pixel of Sierpinski triangle
    """
    SCREEN.set_at((int(point[0]), int(point[1])), COLOR)

def draw_sierpinski(start, repetitions):
    """
    PURPOSE: Draw the Sierpinski triangle on the screen.
    REQUIRES:
        - Global constants WIDTH, HEIGHT are defined
        - Function place_point(point) is defined
    MODIFIES:
        - The contents of the Pygame display surface SCREEN
        - The Pygame display buffer
    EFFECTS:
        - Plots `repetitions` points of the Sierpinski triangle
        - Updates the display incrementally
    """
    place_point(start)
    n = repetitions
    while n > 0:
        new_start = get_new_point(start)
        place_point(new_start)
        start = new_start
        n -= 1


        if n % 100 == 0:
            pygame.display.flip()

    pygame.display.flip()
    return start

def sierpinski_chaos():
    """
    PURPOSE: Run one iteration of the Sierpinski chaos game.
    REQUIRES:
        - Global variables SCREEN, WIDTH, HEIGHT, REPETITIONS defined
        - Pygame is initialized
    MODIFIES:
        - Pygame screen and buffer
        - Program flow if quit event occurs
    EFFECTS:
        - Draws a Sierpinski triangle, exits if user closes window
    """
    handle_events()
    start = (WIDTH / 2, HEIGHT - 50)
    draw_sierpinski(start, REPETITIONS)

def handle_events():
    """
    REQUIRES: Pygame is initialized
    EFFECTS: If the user closes the window, quits pygame and exits the program
    """
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()

initialize_screen()
sierpinski_chaos()

running = True
while running:
    handle_events()

pygame.quit()





