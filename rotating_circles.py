import pygame
import math

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
width, height = 800, 800

# Create the window
window = pygame.display.set_mode((width, height))

# Set the title of the window
pygame.display.set_caption("Rotating Circles")

# Set the color of the circles
circle1_color = (255, 255, 255) # White
circle2_color = (0, 255, 0) # Green
circle3_color = (0, 0, 255) # Blue
circle4_color = (255, 0, 0) # Red

# Get the center coordinates of the window
center_x, center_y = width // 2, height // 2

# Initialize the angle for the circles
angle1 = 90
angle2 = 210
angle3 = 330

# Define the speed of the line movement
line_speed = 1

# Calculate the initial coordinates of the edge of the circle
edge_x = center_x
edge_y = center_y - 200

# Initialize the direction of the line movement
line_direction = 0

# Create a font for the text
font = pygame.font.SysFont(None, 24)

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                line_direction = -1  # Move the line clockwise
            elif event.key == pygame.K_LEFT:
                line_direction = 1  # Move the line counterclockwise
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                line_direction = 0  # Stop the line movement

    # Fill the window with black color
    window.fill((0, 0, 0))

    # Calculate the updated angle based on the line direction
    angle1 += line_speed * line_direction
    angle2 += line_speed * line_direction
    angle3 += line_speed * line_direction

    # Reset the angle to zero after it passes 360
    if angle1 > 360:
        angle1 = 0
    elif angle1 < -360:
        angle1 = 0
    if angle2 > 360:
        angle2 = 0
    elif angle2 < -360:
        angle2 = 0
    if angle3 > 360:
        angle3 = 0
    elif angle3 < -360:
        angle3 = 0

    # Calculate the updated coordinates of the edge of the circle
    edge_x_circle2 = center_x + 200 * math.cos(math.radians(angle1))  # Update the x coordinate
    edge_y_circle2 = center_y - 200 * math.sin(math.radians(angle1))  # Update the y coordinate

    edge_x_circle3 = center_x + 200 * math.cos(math.radians(angle2))  # Update the x coordinate
    edge_y_circle3 = center_y - 200 * math.sin(math.radians(angle2))  # Update the y coordinate

    edge_x_circle4 = center_x + 200 * math.cos(math.radians(angle3))  # Update the x coordinate
    edge_y_circle4 = center_y - 200 * math.sin(math.radians(angle3))  # Update the y coordinate

    # Draw a circle with the center at (400, 400) or the center of the window
    pygame.draw.circle(window, circle1_color, (center_x, center_y), 200, 1)  # Radius = 200, Width = 1

    # Draw circle2
    pygame.draw.circle(window, circle2_color, (edge_x_circle2, edge_y_circle2), 150, 1)

    # Draw circle3
    pygame.draw.circle(window, circle3_color, (edge_x_circle3, edge_y_circle3), 150, 1)

    # Draw circle4
    pygame.draw.circle(window, circle4_color, (edge_x_circle4, edge_y_circle4), 150, 1)

    # Create the text surface for angle1
    angle1_text = font.render("angle1: " + str(round(angle1, 2)), True, circle2_color)

    # Create the text surface for angle2
    angle2_text = font.render("angle2: " + str(round(angle2, 2)), True, circle3_color)

    # Create the text surface for angle3
    angle3_text = font.render("angle3: " + str(round(angle3, 2)), True, circle4_color)

    # Get the rect object for angle1_text
    angle1_rect = angle1_text.get_rect()

    # Get the rect object for angle2_text
    angle2_rect = angle2_text.get_rect()

    # Get the rect object for angle3_text
    angle3_rect = angle3_text.get_rect()

    # Set the position of angle1_text in the upper right corner
    angle1_rect.topright = (width - 30, 10)

    # Set the position of line_2 len text below the angle text
    angle2_rect.topright = (width - 30, angle1_rect.bottom + 10)

    # Set the position of line_3 len text below the line_2 text
    angle3_rect.topright = (width - 30, angle2_rect.bottom + 10)

    # Draw the angle text on the window surface
    window.blit(angle1_text, angle1_rect)
    window.blit(angle2_text, angle2_rect)
    window.blit(angle3_text, angle3_rect)

    # Update the display
    pygame.display.flip()

    pygame.time.Clock().tick(20)

# Quit the game
pygame.quit()