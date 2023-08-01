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
    # Draw a circle at 400x 400y, radius 200, width 1
    pygame.draw.circle(window, colors['white'], (400, 400), 200, 1)
    # Draw circle2
    pygame.draw.circle(window, colors['green'], (circle_coords[0][0], circle_coords[0][1]), 150, 1)
    # Draw circle3
    pygame.draw.circle(window, colors['red'], (circle_coords[1][0], circle_coords[1][1]), 150, 1)
    # Draw circle4
    pygame.draw.circle(window, colors['blue'], (circle_coords[2][0], circle_coords[2][1]), 150, 1)


def update_text(angles, colors, font, window):
    # Create text surfaces and rectangles and render to the screen
    texts = [
        ("angle1: ", angles[0], colors['green']),
        ("angle2: ", angles[1], colors['red']),
        ("angle3: ", angles[2], colors['blue']),
    ]

    for i, (text, angle, color) in enumerate(texts):
        text_surface = font.render(text + str(round(angle, 2)), True, color)
        text_rect = text_surface.get_rect()
        text_rect.topright = (770, 10 + i * 30)
        window.blit(text_surface, text_rect)
