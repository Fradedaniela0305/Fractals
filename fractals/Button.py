import pygame
from utils import *
COLOR_WHITE = (255, 255, 255)
COLOR_GREEN = (68, 255, 5)

class Button:
    """
    PURPOSE: Represent a clickable UI button with text that can change color when hovered or clicked.
    """

    def __init__(self, x, y, image, text, font):
        """
        PURPOSE: Initialize a Button object with position, image, text, and font.

        PARAMETERS: x, y are integers representing the center coordinates of the button.
                    image is a pygame Surface object.
                    text is a string.
                    ont is a valid pygame Font object.

        EFFECTS: Sets up the button image, text surfaces, rectangles, and clicked flag.
        """
        self.x = x # x coordinate of center of button
        self.y = y # y coordinate of center of button
        self.image = image # image to display button
        self.font = font  # font for button display
        self.text_input = text # text for button display
        self.text = set_text(text, COLOR_WHITE, self.font) # text for button with font
        self.rect_image = self.image.get_rect(center=(self.x, self.y)) # rect image for button
        self.rect_text = self.text.get_rect(center=(self.x, self.y)) # rect image for text
        self.clicked = False # represents whether the button has been clicked

    def draw(self, screen):
        """
        PURPOSE: Draw the button (image and text) on the screen.

        PARAMETERS: screen is a valid pygame Surface.

        MODIFIES: screen (pixel buffer updated).

        EFFECTS: Displays the button image and text on the given screen.
        """

        screen.blit(self.image, self.rect_image)
        screen.blit(self.text, self.rect_text)


    def is_clicked(self) -> bool:
        """
        PURPOSE: Determine if the button has been clicked.

        MODIFIES: self.clicked may be updated.

        EFFECTS: Checks the mouse position and click state.
                 Updates the clicked flag.

        RETURNS: True if the button was just clicked, False otherwise.
        """
        action = False
        mouse_position = pygame.mouse.get_pos()

        if self.rect_image.collidepoint(mouse_position):

            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        return action

    def change_color(self, screen):
        """
        PURPOSE: Change the button text color when the mouse hovers over it.

        PARAMETER: screen is a valid pygame Surface.

        MODIFIES: self.text updated based on hover state.
                  screen (pixels updated when draw is called).

        EFFECTS: Changes text color to COLOR_GREEN when hovered, COLOR_WHITE otherwise.
                 Redraws the button.
        """
        mouse_position = pygame.mouse.get_pos()
        if self.rect_image.collidepoint(mouse_position):
            self.text = set_text(self.text_input, COLOR_GREEN, self.font)
        else:
            self.text = set_text(self.text_input, COLOR_WHITE, self.font)

        self.draw(screen)




def create_button(x, y, text, scale, font):
    """
    PURPOSE: Create a Button object at the given position with the specified text and font.

    PARAMETERS: x, y are integers for the center position.
                text is a string.
                scale is a tuple (width, height) for the button image.
                font is a valid pygame Font object.
    RETURNS: A Button object.
    """
    button_img = pygame.image.load('images/buttonImage.png')
    button_img = pygame.transform.scale(button_img, scale)
    button = Button(x, y, button_img, text, font)
    return button



def get_go_back_button() -> Button:
    """
    PURPOSE: Creates and return a "BACK" button for the GUI.
    RETURNS: A button object representing a "BACK" button, positioned at (100, 30).
    """
    go_back_button = create_button(55, 20, "BACK", (100, 30), get_font(10))
    return go_back_button
