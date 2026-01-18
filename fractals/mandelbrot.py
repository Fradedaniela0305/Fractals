from utils import *
import colorsys

ZOOM_IN_FACTOR = 0.2
DOMAIN = (-2, 1)
RANGE = (-1.5, 1.5)
X_PIXEL_WEIGHT = abs(DOMAIN[1] - DOMAIN[0]) / WIDTH
Y_PIXEL_WEIGHT = abs(RANGE[1] - RANGE[0])/HEIGHT
MAX_ITERATIONS = 200


def generate_mandelbrot(screen):
    """
    PURPOSE: Generate the Mandelbrot set visualization on the given screen.

    PARAMETERS: Screen is a valid pygame Surface object.

    MODIFIES: screen (its pixel buffer is updated).

    EFFECTS: Computes the Mandelbrot set for each pixel and colors the screen accordingly.

    """
    for x in range(WIDTH):
        for y in range(HEIGHT):
            complex_num = pixel_to_complex((x, y))
            mandelbrot(screen, complex_num)


def mandelbrot(screen, complex_num):
    """
    PURPOSE: Determine if a complex number belongs to the Mandelbrot set
             and color the corresponding pixel on the screen.

    PARAMETERS: screen is a valid pygame Surface object.
                complex_num is a complex number.

    MODIFIES: screen (pixel buffer updated).

    EFFECTS: Colors the pixel corresponding to complex_num based on the number of iterations.
    """
    z = 0
    for n in range(MAX_ITERATIONS):
        if abs(z) > 2:
            color_pixels_mandelbrot(complex_num, n, screen)
            return
        z = z ** 2 + complex_num
    # if the loop finishes then it's inside the set
    color_pixels_mandelbrot(complex_num, MAX_ITERATIONS, screen)

def color_pixels_mandelbrot(complex_num, num_iterations, screen):
    """
    PURPOSE: Convert a complex number to pixel coordinates and color it based on iteration count.

    PARAMETERS: complex_num is a complex number.
                num_iterations is an integer.
                screen is a valid pygame Surface object.

    MODIFIES: screen (its pixel buffer is updated).

    EFFECTS: Colors the pixel corresponding to complex_num using get_color_mandelbrot.
    """
    pixel = complex_to_pixel(complex_num)
    color = get_color_mandelbrot(num_iterations, MAX_ITERATIONS)
    screen.set_at(pixel, color)

def get_color_mandelbrot(n, max_iterations):
    """
    PURPOSE: Determine the RGB color for a point in the Mandelbrot set based on iteration count.

    PARAMETERS: n and max_iterations are integers with 0 <= n <= max_iterations.

    RETURNS: A tuple (R, G, B) representing the color of the point.
    """
    if n == max_iterations:
        return COLOR_BLACK  # black for inside
    hue = n / max_iterations
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    return int(r*255), int(g*255), int(b*255)


def zoom_in(screen, mouse_pos):
    """
    PURPOSE: Zoom in on the Mandelbrot visualization centered at the mouse position.

    PARAMETERS: screen is a valid pygame Surface object.
                mouse_pos is a tuple (x, y) of integers representing the pixel position.

    MODIFIES: DOMAIN, RANGE (global variables), and screen (updated via generate_mandelbrot).

    EFFECTS: Updates the viewport to zoom in.
             Regenerates the Mandelbrot set visualization for the new viewport.
    """
    global DOMAIN
    global RANGE
    set_viewport(mouse_pos)
    generate_mandelbrot(screen)

def set_viewport(mouse_pos):
    """
    PURPOSE: Update DOMAIN and RANGE globals to zoom in centered at mouse_pos.

    PARAMETERS: mouse_pos is a tuple (x, y) of integers.

    MODIFIES: DOMAIN, RANGE (global variables).

    EFFECTS: Computes new DOMAIN and RANGE based on the zoom factor.
             Updates X_PIXEL_WEIGHT and Y_PIXEL_WEIGHT via recompute_weights().
    """
    global DOMAIN, RANGE

    my_domain, my_range = compute_range_domain(mouse_pos)

    DOMAIN = my_domain
    RANGE = my_range

    recompute_weights()

def compute_range_domain(mouse_pos) -> tuple:
    """
    PURPOSE: Compute the new DOMAIN and RANGE for a zoom centered at mouse_pos.

    PARAMETERS: mouse_pos is a tuple (x, y) of integers.

    RETURNS: A tuple (new_domain, new_range), each a tuple of floats representing
             the x-axis and y-axis limits of the zoomed viewport.
    """
    my_domain = DOMAIN
    my_range = RANGE

    x1, x2 = my_domain
    y1, y2 = my_range
    new_x_length = abs(x1 - x2) * ZOOM_IN_FACTOR
    new_y_length = abs(y1 - y2) * ZOOM_IN_FACTOR

    cx, cy = pixel_to_complex(mouse_pos).real, pixel_to_complex(mouse_pos).imag

    new_x1, new_x2 = cx - (new_x_length / 2), cx + (new_x_length / 2)
    new_y1, new_y2 = cy - (new_y_length / 2), cy + (new_y_length / 2)

    return (new_x1, new_x2), (new_y1, new_y2)

def recompute_weights():
    """
    PURPOSE: Recompute the scaling factors that map pixels to the complex plane,
            based on the current DOMAIN, RANGE, WIDTH, and HEIGHT.

    MODIFIES: X_PIXEL_WEIGHT (global variable): updated to represent the complex-plane width per pixel.
              Y_PIXEL_WEIGHT (global variable): updated to represent the complex-plane height per pixel.

    EFFECTS: Recomputes X_PIXEL_WEIGHT and Y_PIXEL_WEIGHT to reflect the current DOMAIN, RANGE, WIDTH, and HEIGHT.

    """
    global X_PIXEL_WEIGHT, Y_PIXEL_WEIGHT
    X_PIXEL_WEIGHT = (DOMAIN[1] - DOMAIN[0]) / WIDTH
    Y_PIXEL_WEIGHT = (RANGE[1]  - RANGE[0])  / HEIGHT

def get_top_left_complex() -> tuple:
    """
    PURPOSE: Returns top-left corner in the complex plane
    """
    return DOMAIN[0], RANGE[1]


def pixel_to_complex(pixel) -> complex:
    """
    PURPOSE: Converts the coordinates of a screen pixel into a corresponding complex number in the complex plane.

    PARAMETER: pixel is a tuple (x, y) of integers representing pixel coordinates on the screen.

    RETURNS: A complex number corresponding to the pixel position, where the real part maps
             to the x-axis and the imaginary part maps to the y-axis.
    """
    top_left_x, top_left_y = get_top_left_complex()
    x_value = pixel[0]*X_PIXEL_WEIGHT + top_left_x
    y_value = top_left_y - pixel[1] * Y_PIXEL_WEIGHT
    return complex(x_value, y_value)

def complex_to_pixel(complex_num) -> tuple:
    """
    PURPOSE: Converts a complex number in the fractal coordinate system into the corresponding
             pixel coordinates on the screen.
    PARAMETER: complex_num is a complex number representing a point in the complex plane.
    RETURNS: A tuple (x, y) of integers representing the pixel coordinates on the screen corresponding
             to the complex number.
    """
    real_part = complex_num.real
    imag_part = complex_num.imag
    top_left_x, top_left_y = get_top_left_complex()

    x_position = (real_part - top_left_x)/X_PIXEL_WEIGHT
    y_position = (top_left_y - imag_part) / Y_PIXEL_WEIGHT

    return int(round(x_position)), int(round(y_position))


