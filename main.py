import pygame
import math
from settings import Settings


def run_game():
    # Initialize pygame, settings, and screen object.
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

        # Calculate the updated angle based on the line direction
        cset.angle1 += cset.line_speed * cset.line_direction
        cset.angle2 += cset.line_speed * cset.line_direction
        cset.angle3 += cset.line_speed * cset.line_direction

        # Reset the angle to zero after it passes 360
        if cset.angle1 > 360:
            cset.angle1 = 0
        elif cset.angle1 < -360:
            cset.angle1 = 0
        if cset.angle2 > 360:
            cset.angle2 = 0
        elif cset.angle2 < -360:
            cset.angle2 = 0
        if cset.angle3 > 360:
            cset.angle3 = 0
        elif cset.angle3 < -360:
            cset.angle3 = 0

        # Calculate the updated coordinates of the edge of the circle
        edge_x_circle2 = cset.center_x + 200 * math.cos(math.radians(cset.angle1))
        edge_y_circle2 = cset.center_y - 200 * math.sin(math.radians(cset.angle1))

        edge_x_circle3 = cset.center_x + 200 * math.cos(math.radians(cset.angle2))
        edge_y_circle3 = cset.center_y - 200 * math.sin(math.radians(cset.angle2))

        edge_x_circle4 = cset.center_x + 200 * math.cos(math.radians(cset.angle3))
        edge_y_circle4 = cset.center_y - 200 * math.sin(math.radians(cset.angle3))

        # Draw a circle with the center at (400, 400) or the center of the window
        pygame.draw.circle(cset.window, cset.circle1_color, (cset.center_x, cset.center_y), 200, 1)  # Radius = 200, Width = 1

        # Draw circle2
        pygame.draw.circle(cset.window, cset.circle2_color, (edge_x_circle2, edge_y_circle2), 150, 1)

        # Draw circle3
        pygame.draw.circle(cset.window, cset.circle3_color, (edge_x_circle3, edge_y_circle3), 150, 1)

        # Draw circle4
        pygame.draw.circle(cset.window, cset.circle4_color, (edge_x_circle4, edge_y_circle4), 150, 1)

        # Create the text surface for angle1
        angle1_text = cset.font.render("angle1: " + str(round(cset.angle1, 2)), True, cset.circle2_color)

        # Create the text surface for angle2
        angle2_text = cset.font.render("angle2: " + str(round(cset.angle2, 2)), True, cset.circle3_color)

        # Create the text surface for angle3
        angle3_text = cset.font.render("angle3: " + str(round(cset.angle3, 2)), True, cset.circle4_color)

        # Get the rect object for angle1_text
        angle1_rect = angle1_text.get_rect()

        # Get the rect object for angle2_text
        angle2_rect = angle2_text.get_rect()

        # Get the rect object for angle3_text
        angle3_rect = angle3_text.get_rect()

        # Set the position of angle1_text in the upper right corner
        angle1_rect.topright = (cset.width - 30, 10)

        # Set the position of line_2 len text below the angle text
        angle2_rect.topright = (cset.width - 30, angle1_rect.bottom + 10)

        # Set the position of line_3 len text below the line_2 text
        angle3_rect.topright = (cset.width - 30, angle2_rect.bottom + 10)

        # Draw the angle text on the window surface
        cset.window.blit(angle1_text, angle1_rect)
        cset.window.blit(angle2_text, angle2_rect)
        cset.window.blit(angle3_text, angle3_rect)

        # Update the display
        pygame.display.flip()

        pygame.time.Clock().tick(20)


run_game()
