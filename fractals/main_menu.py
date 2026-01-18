from utils import *
from Button import *
def draw_main_menu(screen):
    """
    PURPOSE: Draw the main menu screen, including background, title, and buttons.

    PARAMETERS: screen is a valid pygame Surface object.

    MODIFIES: screen (updates the visual display of the menu).

    EFFECTS: Displays the main menu background and title.
             Creates and draws all buttons on the screen.
    """
    screen.blit(get_main_screen_background(), (0, 0))
    display_title(get_font(55), screen)
    buttons = get_main_menu_buttons()
    draw_buttons(screen, buttons)


def draw_buttons(screen, buttons):
    """
    PURPOSE: Draw all buttons on the given screen.

    REQUIRES: screen is a valid pygame Surface object.
              buttons is a dictionary mapping button names to Button objects.

    MODIFIES: screen (updates pixels where buttons are drawn).

    EFFECTS: Calls the draw method for each Button object to render it on the screen.
    """
    for button in buttons.keys():
        buttons[button].draw(screen)


def get_main_menu_buttons() -> dict[str, 'Button']:
    """
    PURPOSE: Create and return all buttons for the main menu.

    EFFECTS: Instantiates three Button objects for the main menu.

    RETURNS: A dictionary mapping button names to Button objects.
    """
    font = get_font(10)
    return {
        "sierpinski_chaos_button": create_button(WIDTH / 2, 225, "Sierpinski Triangle", (400, 75), font),
        "sierpinski_recursive_button": create_button(WIDTH / 2, 325, "Sierpinski Triangle Recursive", (400, 75), font),
        "mandelbrot_button": create_button(WIDTH / 2, 425, "Simple Mandelbrot Fractal", (400, 75), font)
    }
