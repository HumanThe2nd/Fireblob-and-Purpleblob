import pygame


class player(pygame.sprite.Sprite):
  def __init__(self, position, image):
    """
    creates an instance of the player class (creates a button)

    parameters:
    size (tuple): specifies the width and height of the button
    position (tuple): specifies the spawn location of the player
    image (str): provides the path directory to the image used as the players sprite
    """
    self._image = pygame.image.load(image)
    self._player_rect = self._image.get_rect(midbottom = position)
    self._movement = 0
    self._gravity = 0
    self._right = False
    self._left = False
    self._up = False

  def collision_test(self, tiles):
    """
    checks for player collisions all barriers on the screen (floors)

    parameters:
    tiles (list): stores all barriers on the screen

    returns:
    collisions (array): stores all barriers that are colliding with the player rect
    """
    collisions = []
    for tile in tiles[0]:
      if self.get_rect().colliderect(tile):
        collisions.append(tile)
    return collisions

  def move(self, tiles):  # movement = [5,2]
    """
    Changes the movement variable to allow movement toward the right and left as well as the gravity variable to simulate jumping
    Moves the player in the x and y direction according to the _movement and _gravity variables, also checks for collisions and prevents phasing through walls

    parameters:
    tiles (list): stores all barriers on the screen
    """
    self._movement = 0
    if self._right:
      self._movement += 5
    if self._left:
      self._movement -= 5
    if self._up and self._gravity == 0:
      self._gravity = -12
      self._up = False
    if self._gravity == -1:
      self._gravity += 2
    else:
      self._gravity += 1
    self.get_rect().x += self._movement
    collisions = self.collision_test(tiles)
    for tile in collisions:
      if self._movement > 0:
        self.get_rect().right = tile.left
      if self._movement < 0:
        self.get_rect().left = tile.right
    self.get_rect().y += self._gravity
    collisions = self.collision_test(tiles)
    for tile in collisions:
      if self._gravity > 0:
        self.get_rect().bottom = tile.top-1
      if self._gravity < 0:
        self.get_rect().top = tile.bottom
      self._gravity = 0

  def get_rect(self):
    """
    Returns the rect of the player
    """
    return self._player_rect

  def t_up(self):
    """
    Sets _up variable to True
    """
    self._up = True

  def t_left(self):
    """
    Sets _left variable to True
    """
    self._left = True

  def t_right(self):
    """
    Sets _right variable to True
    """
    self._right = True

  def f_up(self):
    """
    Sets _up variable to False
    """
    self._up = False

  def f_left(self):
    """
    Sets _left variable to False
    """
    self._left = False

  def f_right(self):
    """
    Sets _right variable to False
    """
    self._right = False

  def draw(self, screen):
    """
    blit the player onto the screen and also restrict their movement to within the boundaries of the screen

    parameters:
    screen (pygame.display): the screen where all objects are displayed
    """
    self.get_rect().clamp_ip(screen.get_rect())
    screen.blit(self._image, self.get_rect())

  def set_position(self, position):
    self.get_rect().midbottom = position
