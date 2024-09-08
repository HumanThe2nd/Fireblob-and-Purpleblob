import unittest
from unittest.mock import MagicMock, patch
from level_one import level_one

class TestLevelOne(unittest.TestCase):

    @patch('builtins.quit', MagicMock())
    def test_run_game(self):
        # Replace the Pygame functions with MagicMock
        pygame_init_mock = MagicMock()
        pygame_display_set_caption_mock = MagicMock()
        pygame_set_mode_mock = MagicMock()
        pygame_image_load_mock = MagicMock()
        pygame_quit_mock = MagicMock()
        pygame_time_clock_mock = MagicMock()

        with patch('pygame.init', pygame_init_mock), \
             patch('pygame.display.set_caption', pygame_display_set_caption_mock), \
             patch('pygame.display.set_mode', pygame_set_mode_mock), \
             patch('pygame.image.load', pygame_image_load_mock), \
             patch('pygame.quit', pygame_quit_mock), \
             patch('pygame.time.Clock', pygame_time_clock_mock):

            result = level_one.run_game()

        # Assertions for Pygame function calls
        pygame_init_mock.assert_called_once()
        pygame_display_set_caption_mock.assert_called_once_with('Level One')
        pygame_set_mode_mock.assert_called_once_with((720, 480), 0, 32)
        pygame_image_load_mock.assert_called_once_with('images/wallpaper.jpeg')
        pygame_quit_mock.assert_called_once()

        # Assertions for the expected result
        self.assertEqual(result, "menu")

if __name__ == '__main__':
    unittest.main()
