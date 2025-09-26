from fractals import get_font


class Button:

    def __init__(self, x, y, image, text):


        self.x = x
        self.y = y
        self.image = image
        self.text = text_surface_black = get_font().render(text, False, (255, 255, 255))
        self.rect_image = self.image.get_rect(center=(self.x, self.y))
        self.rect_text = self.text.get_rect(center=(self.x, self.y))

    def draw(self, screen):
        screen.blit(self.image, self.rect_image)
        screen.blit(self.text, self.rect_text)
