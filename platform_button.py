import pygame


class PlatformButton:
    def __init__(self, image_path, position):
      """
      creates a button that the player in interact with
      parameters:
      image_path (str): the path directory of the image
      position: (tuple): the coordinates of the image
      """
      self._image = pygame.image.load(image_path).convert_alpha()
      self._rect = self._image.get_rect(center=position)
      self.touched = False

    def draw(self, surface):
      """
      blits the button
      """
      surface.blit(self._image, self._rect)

    def get_rect(self):
      """
      returns the button rectangle
      """
      return self._rect

    def set_touched(self, touched):
      """
      allows you to change the touched state of the button

      parameters:
      touched (bool): the state that the button is set to
      """
      self.touched = touched

    def is_touched(self):
      """
      returns the touched state of the button
      """
      return self.touched

    def check_pressed(self, p1_rect, p2_rect):
      """
      checks if the button is being pressed by either player
      parameters:
      p1_rect (rect): rect of player 1
      p2_rect (rect): rect of player 2
      """
      if p1_rect.colliderect(
        self._rect) or p2_rect.colliderect(
            self.get_rect()):
        self.set_touched(True)
      else:
        self.set_touched(False)
