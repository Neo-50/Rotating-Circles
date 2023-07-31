import pygame
from settings import Settings
import functions as gf


def run_game():
    # Initialize pygame and settings
    pygame.init()
    cset = Settings()

    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    cset.line_direction = -1  # Move the line clockwise
                elif event.key == pygame.K_LEFT:
                    cset.line_direction = 1  # Move the line counterclockwise
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    cset.line_direction = 0  # Stop the line movement

        # Fill the window with black color
        cset.window.fill((0, 0, 0))

        # Update the angle
        gf.update_angles(cset.angles, cset.line_speed, cset.line_direction)

        # Reset the angle after it passes 360
        gf.reset_angle(cset.angles)

        # Update the coordinates for the centerpoints for each circle
        circle_coords = gf.update_coords(cset.angles, cset.center_x, cset.center_y)

        # Draw the circles
        gf.draw_circles(cset.window, cset.circle_colors, circle_coords)

        # Draw and update the text surfaces
        gf.update_text(cset.angles, cset.circle_colors, cset.font, cset.window)

        # Update the display
        pygame.display.flip()

        pygame.time.Clock().tick(20)


run_game()
