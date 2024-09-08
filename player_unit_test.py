import unittest
from player import player
import pygame

class TestPlayer(unittest.TestCase):

    def setUp(self):
        # Create a test screen for the player to move within
        self.test_screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Test Screen")

        # Create a test player instance
        self.test_player = player((100, 100), "images/fb.png")

    def test_initialization(self):
        # Check if the player's initial position is set correctly
        self.assertEqual(self.test_player.get_rect().midbottom, (100, 100))

    def test_movement(self):
        # Set movement variables
        self.test_player.t_right()
        self.test_player.move([])

        # Check if the player's position is updated correctly after moving right
        self.assertEqual(self.test_player.get_rect().midbottom, (105, 100))

        # Reset movement variables
        self.test_player.f_right()

        # Set movement variables
        self.test_player.t_left()
        self.test_player.move([])

        # Check if the player's position is updated correctly after moving left
        self.assertEqual(self.test_player.get_rect().midbottom, (100, 100))

    def test_jump(self):
        # Set jump variables
        self.test_player.t_up()
        self.test_player.move([])

        # Check if the player's position is updated correctly after jumping
        self.assertEqual(self.test_player.get_rect().midbottom, (100, 88))

        # Reset jump variables
        self.test_player.f_up()

        # Check if the player's position is updated correctly after not jumping
        self.assertEqual(self.test_player.get_rect().midbottom, (100, 100))

    def tearDown(self):
        pygame.quit()

if __name__ == "__main__":
    unittest.main()
