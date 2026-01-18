from fractals import initialize_screen
from events import handle_events
from utils import *
from main_menu import *
from fractals.Button import *
from sierpinski import draw_sierpinski
from sierpinski_recursive import sierpinski_recursive
from sierpinski import initialize_sierpinski_screen, draw_line_and_point
from mandelbrot import generate_mandelbrot, zoom_in


def main_menu():
    """
    PURPOSE: Initialize and run the main menu screen with buttons.

    MODIFIES: screen (pygame display) is updated with menu visuals and button states.
              Button objects' internal state.
    EFFECTS: Displays the main menu.
             Handles user interactions via buttons.
             Calls the corresponding functions when buttons are clicked.

    """
    screen = initialize_screen("Main Menu", (126, 196, 252))
    draw_main_menu(screen)

    pygame.display.flip()

    running = True

    buttons = get_main_menu_buttons()
    while running:
        running = handle_events()
        if buttons["mandelbrot_button"].is_clicked():
            mandelbrot_main()
        if buttons["sierpinski_chaos_button"].is_clicked():
            sierpinski_chaos_main()
        if buttons["sierpinski_recursive_button"].is_clicked():
            sierpinski_recursive_main()

        for button in buttons.values():
            button.change_color(screen)  # updates hover/default color

        pygame.display.flip()



def sierpinski_chaos_main():
    """
    PURPOSE: Initialize and run the Sierpinski Triangle visualization using the chaos method.

    MODIFIES: screen (pygame Surface) is updated with the Sierpinski triangle and lines.
              Button objects' internal state.

    EFFECTS: Allows user to pick a point to start the chaos method.
             Continuously draws points and lines as user interacts with the mouse.
             Provides a "Go Back" button to return to the main menu.
    """
    screen = initialize_screen("Sierpinski Triangle Chaos", COLOR_WHITE)
    initialize_sierpinski_screen(screen)
    go_back_button = get_go_back_button()
    go_back_button.draw(screen)
    pygame.display.flip()

    running = True
    picked = False
    started_drawing = False
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                running = False
            elif go_back_button.is_clicked():
                main_menu()
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if not picked and not started_drawing:
                    mouse_pos = pygame.mouse.get_pos()
                    screen.fill(COLOR_WHITE)
                    go_back_button.draw(screen)
                    draw_sierpinski(screen, mouse_pos, repetitions=30000)
                    picked = True
                    started_drawing = True
                elif started_drawing:
                    mouse_pos = pygame.mouse.get_pos()
                    draw_line_and_point(screen, mouse_pos)





def sierpinski_recursive_main():
    """
    PURPOSE: Initialize and display the Sierpinski Triangle using the recursive method.

    MODIFIES: screen (pygame Surface) is updated with the recursive Sierpinski triangle.
              Button objects' internal state.

    EFFECTS: Draws the Sierpinski triangle recursively.
             Provides a "Go Back" button to return to the main menu.
    """
    screen = initialize_screen("Sierpinski Triangle Recursive", COLOR_WHITE)
    sierpinski_recursive(screen, (WIDTH / 2, 50), (50, HEIGHT - 50), (WIDTH - 50, HEIGHT - 50))

    go_back_button = get_go_back_button()
    go_back_button.draw(screen)
    pygame.display.flip()

    running = True
    while running:
        running = handle_events()
        if go_back_button.is_clicked():
            main_menu()


def mandelbrot_main():
    """
    PURPOSE: Initialize and display the Mandelbrot set visualization.

    MODIFIES: screen (pygame Surface) is updated with the Mandelbrot visualization.
              Button objects' internal state.

    EFFECTS: Displays the Mandelbrot set on screen.
             Allows zooming in at mouse click positions.
             Provides a "Go Back" button to return to the main menu.
    """
    screen = initialize_screen("Simple Mandelbrot Fractal", COLOR_WHITE)
    generate_mandelbrot(screen)

    go_back_button = get_go_back_button()
    go_back_button.draw(screen)
    pygame.display.flip()

    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif go_back_button.is_clicked():
                main_menu()
            elif e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                zoom_in(screen, mouse_pos)
                go_back_button.draw(screen)
                pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    pygame.init()
    main_menu()