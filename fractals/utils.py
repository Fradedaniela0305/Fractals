import pygame

WIDTH, HEIGHT = 600, 600
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

def place_point(screen, point):
    """
    PARAMETER: Consumes a tuple with coordinates (x, y)
    REQUIRES: Global variable COLOR is defined
    MODIFIES: Pygame screen and buffer
    EFFECTS: Places new pixel of Sierpinski triangle
    """
    screen.set_at((int(point[0]), int(point[1])), COLOR_BLACK)

def get_font():
    font = pygame.font.Font("../PressStart2P-Regular.ttf", 40)
    return font

def compute_mid_point(coordinate_1, coordinate_2):
    """
    PARAMETER: Consumes two coordinates of screen as numbers
    EFFECTS: Computes the midpoint between two points
    """
    return (coordinate_1 + coordinate_2) / 2

def compute_mid_point_c(point_1, point_2):
    x1, y1 = point_1
    x2, y2 = point_2
    x = compute_mid_point(x1, x2)
    y = compute_mid_point(y1, y2)
    return x,y




def create_triangle(screen, color, top, left, right, width):
    """
       PURPOSE: Draw a triangle in given screen with given color and x, y, z coordinates.
       PARAMETER: Consumes a screen, a color, and x, y, z coordinates.
       REQUIRES: Pygame is initialized
       MODIFIES: Draws a triangle outline in given screen
       EFFECTS: Updates display so the window shows a triangle outline in given coordinates
       """
    pygame.draw.polygon(screen, color, (top, left, right), width)


def compute_distance(point_1, point_2):
    x1, y1 = point_1
    x2, y2 = point_2
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def display_title(font, screen):
    text_surface_black = font.render("Fractals", False, COLOR_WHITE)  # creates text surface
    text_rect = text_surface_black.get_rect(center=(WIDTH / 2, 100))  # makes a rectangle of the size of the surface centered at x,y
    screen.blit(text_surface_black, text_rect)  # places it in that rectangle