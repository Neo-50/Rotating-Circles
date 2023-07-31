import math
import pygame


def update_angles(angles, speed, direction):
    # Calculate the updated angle based on the line direction
    for i in range(len(angles)):
        angles[i] += speed * direction


def reset_angle(angles):
    # Reset the angle to zero after it passes 360
    if angles[0] > 360:
        angles[0] = 0
    elif angles[0] < -360:
        angles[0] = 0
    if angles[1] > 360:
        angles[1] = 0
    elif angles[1] < -360:
        angles[1] = 0
    if angles[2] > 360:
        angles[2] = 0
    elif angles[2] < -360:
        angles[2] = 0


def update_coords(angles, centerx, centery):
    # Calculate the updated coordinates of the edge of the circle
    circle_coords = []
    for angle in angles:
        angle_rad = math.radians(angle)
        circle_x = centerx + 200 * math.cos(angle_rad)
        circle_y = centery - 200 * math.sin(angle_rad)
        circle_coords.append((circle_x, circle_y))

    return circle_coords


def draw_circles(window, colors, circle_coords):
    # Draw a circle with the center at (400, 400) or the center of the window
    pygame.draw.circle(window, colors['white'], (400, 400), 200, 1)
    # Draw circle2
    pygame.draw.circle(window, colors['green'], (circle_coords[0][0], circle_coords[0][1]), 150, 1)
    # Draw circle3
    pygame.draw.circle(window, colors['red'], (circle_coords[1][0], circle_coords[1][1]), 150, 1)
    # Draw circle4
    pygame.draw.circle(window, colors['blue'], (circle_coords[2][0], circle_coords[2][1]), 150, 1)


def update_text(cset):
    # Create the text surface for angle1
    cset.angle1_text = cset.font.render("angle1: " + str(round(cset.angles[0], 2)), True, cset.circle2_color)

    # Create the text surface for angle2
    cset.angle2_text = cset.font.render("angle2: " + str(round(cset.angles[1], 2)), True, cset.circle3_color)

    # Create the text surface for angle3
    cset.angle3_text = cset.font.render("angle3: " + str(round(cset.angles[2], 2)), True, cset.circle4_color)

    # Get the rect object for angle1_text
    cset.angle1_rect = cset.angle1_text.get_rect()

    # Get the rect object for angle2_text
    cset.angle2_rect = cset.angle2_text.get_rect()

    # Get the rect object for angle3_text
    cset.angle3_rect = cset.angle3_text.get_rect()

    # Set the position of angle1_text in the upper right corner
    cset.angle1_rect.topright = (cset.width - 30, 10)

    # Set the position of line_2 len text below the angle text
    cset.angle2_rect.topright = (cset.width - 30, cset.angle1_rect.bottom + 10)

    # Set the position of line_3 len text below the line_2 text
    cset.angle3_rect.topright = (cset.width - 30, cset.angle2_rect.bottom + 10)

    # Draw the angle text on the window surface
    cset.window.blit(cset.angle1_text, cset.angle1_rect)
    cset.window.blit(cset.angle2_text, cset.angle2_rect)
    cset.window.blit(cset.angle3_text, cset.angle3_rect)