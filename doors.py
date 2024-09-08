import pygame


class door:
  def __init__(self, position, image):
    """
    
    """
    self._image = pygame.image.load(image)
    self._rect = self._image.get_rect(midbottom = position)

  def check_player(self, player_rect):
    """
    checks if the player rect that is passed throught the parameters is colliding with the door

    parameters:
    player_rect (Rect): the rect of the player being checked

    returns:
    (bool): returns either true of false to be used in a condition
    """
    if self._rect.colliderect(player_rect):
      return True
    return False

  def draw(self, screen):
    """
    blits the door onto a screen

    parameters:
    screen (display): the surface that the door is displayed on
    """
    screen.blit(self._image, self._rect)
