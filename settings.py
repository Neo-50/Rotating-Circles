import pygame
class Settings:
    """A class to store all settings for Rotating Circles."""

    def __init__(self):
        """Initialize the game's static settings."""

        # Set the dimensions of the window
        self.width, self.height = 800, 800

        # Create the window
        self.window = pygame.display.set_mode((self.width, self.height))

        # Set the color of the circles
        self.circle1_color = (255, 255, 255)  # White
        self.circle2_color = (0, 255, 0)  # Green
        self.circle3_color = (0, 0, 255)  # Blue
        self.circle4_color = (255, 0, 0)  # Red

        # Create a font for the text
        self.font = pygame.font.SysFont(None, 24)

        # Get the center coordinates of the window
        self.center_x, self.center_y = self.width // 2, self.height // 2

        # Initialize the angle for the circles
        self.angle1 = 90
        self.angle2 = 210
        self.angle3 = 330

        # Define the speed of the line movement
        self.line_speed = 1

        # Calculate the initial coordinates of the edge of the circle
        self.edge_x = self.center_x
        self.edge_y = self.center_y - 200

        # Initialize the direction of the line movement
        self.line_direction = 0