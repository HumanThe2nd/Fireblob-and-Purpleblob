import pygame


class barriers:

    def __init__(self):
        """
      creates a 2D list containing all the floors/barriers in every level, each level's floors are found in a separate sub-list
      """
        self._barriers = [
            [
                pygame.Rect(150, 50, 600, 20),  # top floor
                pygame.Rect(0, 150, 600, 20),  # second top
                pygame.Rect(250, 250, 350, 20),  # middle
                pygame.Rect(0, 350, 600, 20),  # second bottom
                pygame.Rect(0, 460, 720, 30),
                pygame.Rect(75, 300, 115, 20),
                pygame.Rect(0, 90, 85, 20)
            ],
            [
                pygame.Rect(150, 50, 600, 20),  # top floor
                pygame.Rect(0, 150, 600, 20),
                pygame.Rect(520, 250, 200, 200),
                pygame.Rect(420, 300, 80, 20),
                pygame.Rect(320, 350, 80, 20),
                pygame.Rect(220, 400, 80, 20),
                pygame.Rect(0, 450, 720, 20)  #floor
            ]
        ]

    def get_barriers(self):
        """
      Returns a 2D list that contains all barriers used in the game, these barriers are separated into different sub-lists depending on which level they are used in

      returns:
      _barriers (2D list): the list containin all barriers across all levels
      """
        return self._barriers
