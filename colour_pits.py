import pygame


class ColourPit:
    def __init__(self, colour, rect):
        """
        Initialize a ColourPit instance.

        Parameters:
        - colour (tuple): The RGB color tuple representing the color of the pit.
        - rect (tuple or pygame.Rect): The rectangular area occupied by the color pit.
          If a tuple is provided, it will be converted to a pygame.Rect.
        """
        self.colour = colour
        self.rect = pygame.Rect(rect)

    def draw(self, screen):
        """
        Draw the color pit on the specified Pygame screen.

        Parameters:
        - screen: The Pygame screen surface.
        """
        pygame.draw.rect(screen, self.colour, self.rect)

    def check_player(self, player_rect):
        """
        Check if the player, represented by the given rectangle, is colliding with the color pit.

        Parameters:
        - player_rect (pygame.Rect): The rectangular area occupied by the player.

        Returns:
        - bool: True if the player is colliding with the color pit, False otherwise.
        """
        return self.rect.colliderect(player_rect)
