import pygame


class MovingPlatform(pygame.sprite.Sprite):
    def __init__(self, rect, start_pos, end_pos):
      """
      creates a moving platform barrier

      parameters:
      rect (Rect): the rect of the barrier
      start_pos (int): a value that signfies one of the turning points of the platform
      end_pos (int): a value that signifies the other turning point of the platform
      """
      super().__init__()
      self.rect = rect   # Adjust the rect as needed
      self.start_pos = start_pos
      self.end_pos = end_pos
      self.speed = 1  # Adjust the speed as needed
      self.direction = 1  # 1 for moving down, -1 for moving up
      self.going_up = True

    def move_platform(self, screen):
      """
      moves the rect of the platform according to its start and end positions

      parameters:
      screen (display): the surface where the platform is displayed
      """
      if self.going_up:
        self.rect.y -= 1
      else:
        self.rect.y += 1

      if self.rect.top <= self.start_pos:
        self.going_up = False
      elif self.rect.bottom >= self.end_pos:
        self.going_up = True
