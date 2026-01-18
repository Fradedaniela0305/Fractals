from fractals.utils import *

def initialize_screen(title, color):
    """
    PURPOSE: Initialize the screen for drawing a Sierpinski triangle.
    REQUIRES: Pygame is initialized and global variable SCREEN is defined.
    MODIFIES: Fills the screen with white background and sets window caption.
    EFFECTS: Updates display so the window shows a white screen with the title 'Sierpinski Triangle'.
    """

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(title)
    screen.fill(color)
    pygame.display.flip()
    return screen


