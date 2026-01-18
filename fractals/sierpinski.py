import random
import time
from fractals.utils import *
from events import *

TOP = (WIDTH / 2, 50)
LEFT = (50, HEIGHT - 50)
RIGHT = (WIDTH - 50, HEIGHT - 50)
CORNERS = [TOP, LEFT, RIGHT]
pygame.init()


def initialize_sierpinski_screen(screen):
    """
    PURPOSE: To set up the screen for visualizing the Sierpinski triangle by clearing it
             and drawing the initial large triangle where the user can place the first point
    PARAMETERS: screen is a valid pygame Surface object.
    MODIFIES: screen (its pixel buffer is updated).
    EFFECTS: Fills the entire screen with white (COLOR_WHITE).
             Draws a black triangle (COLOR_BLACK) using the vertices TOP, LEFT, RIGHT.

    """
    screen.fill(COLOR_WHITE)
    create_triangle(screen, COLOR_BLACK, TOP, LEFT, RIGHT, 3)



def draw_sierpinski(screen, start, repetitions):
    """
    PURPOSE: Draw the Sierpinski triangle on the screen using chaos method.
    PARAMETERS: Screen is a valid pygame Surface object.
                Start is a coordinate in the screen of type tuple.
                Repetitions is the number of points that will be drawn on screen of type int.

    MODIFIES:
        - The contents of the Pygame display surface SCREEN
        - The Pygame display buffer
    EFFECTS:
        - Plots `repetitions` points of the Sierpinski triangle
        - Updates the display incrementally
    """

    place_point(screen, start)
    n = repetitions
    while n > 0:
        new_start = get_new_point(start)
        place_point(screen, new_start)
        start = new_start
        n -= 1


        if n % 100 == 0:
            pygame.display.flip()
            time.sleep(0.001)

    pygame.display.flip()


def draw_line_and_point(screen, mouse_position):
    """
    PURPOSE: Visualize one step of the chaos method for constructing a Sierpinski triangle
             by drawing a new point and a connecting line from the current mouse position.

    PARAMETERS: Screen is a valid pygame Surface object.
                mouse_position is a tuple (x, y) representing the current position of the mouse.

    MODIFIES: screen.

    EFFECTS:
        Draws a red circle at the new point returned by get_new_point.
        Draws a green line from mouse_position to the computed end point.
        Updates the display to show the new point and line immediately.

    """

    new_point = get_new_point(mouse_position)
    pygame.draw.circle(screen, (255, 0, 0), new_point, 5)
    pygame.draw.line(screen, COLOR_GREEN, mouse_position, compute_end_point(mouse_position, new_point), 3)
    pygame.display.flip()


def get_new_point(start):
    """
    PARAMETER: Consumes a tuple with coordinates (x, y) that must be inside the triangle
    REQUIRES: Global variable corners should be initialized
    EFFECTS: Computes new point for Sierpinski triangle and returns it
    """
    corners = CORNERS
    corner = random.choice(corners)
    x1, y1 = start
    x2, y2 = corner
    point_x = compute_mid_point(x1, x2)
    point_y = compute_mid_point(y1, y2)
    return int(point_x), int(point_y)


def get_corners():
    return CORNERS






