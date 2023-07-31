import pygame


class Settings:
    """A class to store all settings for Rotating Circles."""

    def __init__(self):
        """Initialize the game's static settings."""

        # Set the dimensions of the window
        self.width, self.height = 800, 800

        # Define window
        self.window = pygame.display.set_mode((self.width, self.height))

        # Set the color of the circles
        self.circle_colors = {
            'white': (255, 255, 255),
            'green': (0, 255, 0),
            'blue': (0, 0, 255),
            'red': (255, 0, 0),
        }

        # Set circle coordinates
        circles_xy = []

        # Create a font for the text
        self.font = pygame.font.SysFont(None, 24)

        # Get the center coordinates of the window
        self.center_x, self.center_y = self.width // 2, self.height // 2

        # Initialize the angle for the circles
        self.angles = [90, 210, 330]

        # Define the speed of rotation
        self.line_speed = 1

        # Initialize the direction of the line movement
        self.line_direction = 0
