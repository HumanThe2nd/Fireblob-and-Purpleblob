import pygame


class button(pygame.sprite.Sprite):

  def __init__(self, size, position, font, words):
    """
    creates an instance of the button class (creates a button)
    
    parameters:
    size (tuple): specifies the width and height of the button
    position (tuple): specifies the x and y positions of the button
    font (Font): specifies the font and font size of the text
    words (string): specifies the words that appear on the button
    """
    super().__init__()
    self._font = font
    self._words = words
    self._image = pygame.Surface(size)
    self._text = self._font.render(words, True, "White")
    self._image.fill("#873e23")
    self._rect = self._image.get_rect(topleft = position)

  def mouse_hover(self):
    """
       darkens the button when the mouse hovers over it
    """
    if self._rect.collidepoint(pygame.mouse.get_pos()):
      self._image.fill("#21130d")
      self._text = self._font.render(self._words, True, "Gray")

  def mouse_off(self):
    """
       darkens the button when the mouse moves off of it
    """
    if not self._rect.collidepoint(pygame.mouse.get_pos()):
      self._image.fill("#873e23")
      self._text = self._font.render(self._words, True, "White")

  def draw(self, screen):
    """
    blits the button

    parameters:
    screen (display): specifies the screen that the button is being drawn on
    """
    screen.blit(self._image, self._rect)
    screen.blit(self._text, self._rect)

  def get_rect(self):
    return self._rect
