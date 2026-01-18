import pygame
WIDTH, HEIGHT = 600, 600
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GREEN = (68, 255, 5)

def place_point(screen, point):
    """
    PURPOSE:  To draw a point on the given screen at the specified coordinates.
    PARAMETERS: screen is a valid pygame Surface object.
              point is a tuple (x, y) of numbers (int or float).
    MODIFIES: screen (its pixel buffer is updated).
    EFFECTS: Colors the pixel at (⌊x⌋, ⌊y⌋) with COLOR_BLACK.
    """
    screen.set_at((int(point[0]), int(point[1])), COLOR_BLACK)

def get_font(size) -> pygame.font.Font:
    """
    PURPOSE: Getter for program's font
    PARAMETERS: Consumes an int which will be the size of the font
    RETURNS: The pixel font used in the program
    """
    font = pygame.font.Font("pixelFont.ttf", size)
    return font

def compute_mid_point(point_1, point_2) -> int or float:
    """
    PURPOSE: Compute the midpoint between two points point_1, point_2
    PARAMETERS: Coordinate_1 and coordinate_2 are numbers (int or float).
    RETURNS: The midpoint between coordinate_1 and coordinate_2, as a number.
    """
    return (point_1 + point_2) / 2


def compute_mid_point_c(coordinate_1, coordinate_2) -> tuple:
    """
    PURPOSE: Compute the midpoint between two coordinates x1,y1 and x2,y2
    PARAMETERS: coordinate_1 and coordinate_2 are points in 2d, each represented as a tuple (x, y)
              where x and y are numbers (int or float).
    RETURNS: The midpoint between point_1 and point_2, as a tuple (x, y).
    """
    x1, y1 = coordinate_1
    x2, y2 = coordinate_2
    x = compute_mid_point(x1, x2)
    y = compute_mid_point(y1, y2)
    return x, y



def create_triangle(screen, color, top, left, right, width):
    """
    PURPOSE: Draw a triangle in given screen with given color and x, y, z points.
    PARAMETER: Screen is a valid pygame Surface object, color is a tuple of three numbers,
               top, left and right are coordinates in the screen of type int (will be the corners of the triangle).
               Width is an int or float, which describes how thick the triangle's outline will be.
    MODIFIES: Draws a triangle outline in given screen
    EFFECTS: Updates display so the window shows a triangle outline in given coordinates
    """
    pygame.draw.polygon(screen, color, (top, left, right), width)



def compute_distance(point_1, point_2) -> float:
    """
    PURPOSE: To compute the Euclidean distance between two 2D points.
    PARAMETER: point_1 and point_2 are tuples (x, y), where x and y are numbers (int or float).
    RETURNS: The distance between point_1 and point_2 as a float.
    """
    x1, y1 = point_1
    x2, y2 = point_2
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


def display_title(font, screen):
    """
    PURPOSE: To render and display the title text "Fractals" at the top of the screen.
    PARAMETERS: Font is a valid pygame Font object. Screen is a valid pygame Surface object.
    MODIFIES: screen (its pixel buffer is updated).
    EFFECTS: Draws the text "Fractals" in COLOR_WHITE centered at (WIDTH/2, 100).
    RETURNS: None.
    """
    text_surface_black = font.render("Fractals", False, COLOR_WHITE)
    text_rect = text_surface_black.get_rect(center=(WIDTH / 2, 100))
    screen.blit(text_surface_black, text_rect)


def get_main_screen_background():
    """
    PURPOSE: To load and scale the background image for the main screen.
    EFFECTS: Loads an image from disk.
             Scales the image to dimensions (WIDTH, HEIGHT).
    RETURNS: A pygame Surface object containing the scaled background image.
    """
    image = pygame.image.load('images/background.png')
    return pygame.transform.scale(image, (WIDTH, HEIGHT))

def compute_end_point(point, mid_point):
    """
    PURPOSE: To compute the point on the opposite side of mid_point from point,
             effectively reflecting point across mid_point.

    PARAMETERS: point is a tuple (x, y) of numbers (int or float).
                mid_point is a tuple (x, y) of numbers (int or float).

    RETURNS: A tuple (x, y) representing the new end point.
    """
    a, b = point
    c, d = mid_point
    x = 2 * c - a
    y = 2 * d - b
    return x, y



def set_text(text, color, font):
    """
    PURPOSE: Render a text string into a pygame Surface with the given color and font.
    EFFECTS: text is a string.
             color is a tuple of 3 integers (R, G, B), each 0-255.
             font is a valid pygame Font object.
    RETURNS: A pygame Surface containing the rendered text.
    """
    return font.render(text, False, color)