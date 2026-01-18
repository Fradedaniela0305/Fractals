import pygame

def handle_events():
    """
    EFFECTS: If the user closes the window, quits pygame and exits the program
    """
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            return False
        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()  # (x, y)
            print("Mouse clicked at:", mouse_pos)
    return True