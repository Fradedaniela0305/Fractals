from fractals.utils import *
import time



def sierpinski_recursive(screen, top, left, right):
    """
    PURPOSE: Recursively draw a Sierpinski triangle on the screen.

    PARAMETERS: screen is a valid pygame Surface object.
                top, left, right are tuples (x, y) representing coordinates of the triangle's vertices.
    MODIFIES: screen, display is updated recursively.

    EFFECTS:
           - Draws outlined triangles on the screen to create the Sierpinski triangle pattern.
           - Updates the display after drawing each triangle.
       """
    side = compute_distance(top, left)
    if side < 2: # base case
        create_triangle(screen, COLOR_BLACK, (0,0), (0,0), (0,0), 0)
    else: # recursive case
        create_triangle(screen, COLOR_BLACK, top, left, right, 1)
        pygame.display.update()  # update the screen
        # pygame.time.delay(1)
        top_left = compute_mid_point_c(top, left)
        top_right = compute_mid_point_c(top, right)
        left_right = compute_mid_point_c(left, right)

        sierpinski_recursive(screen, top, top_left, top_right) # top
        sierpinski_recursive(screen, top_left, left, left_right) # left
        sierpinski_recursive(screen, top_right, left_right, right) # right



