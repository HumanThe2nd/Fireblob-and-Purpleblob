import pygame
import sys
from pygame.locals import *
from player import player
from barriers import barriers
from platform_button import PlatformButton
from doors import door
from moving_platform import MovingPlatform
from colour_pits import ColourPit


class level_one:
    """
    A class representing Level One of the game.

    This class initializes and runs the main game loop for Level One,
    including the creation of players, doors, buttons, platforms, color pits,
    and barriers. It handles player movement, collisions, button presses,
    and updates the game display.
    """
    @staticmethod
    def run_game():
        """
        Run the main game loop for Level One.
        """

        # Initialize Pygame
        pygame.init()

        # Set window title and dimensions
        pygame.display.set_caption('Level One')
        screen = pygame.display.set_mode((720, 480), 0, 32)

        # Create players
        p1 = player((50, 690), "images/fb.png")
        p2 = player((100, 690), "images/pb.png")

        # Create doors
        fdoor = door((620, 50), "images/fd.png")
        pdoor = door((690, 50), "images/pd.png")

        # Load background wallpaper and create barriers
        wallpaper = pygame.image.load('images/wallpaper.jpeg')
        map = barriers()

        # Create buttons
        button1 = PlatformButton("images/button.png", (450, 340))
        button2 = PlatformButton("images/button.png", (360, 450))
        button3 = PlatformButton("images/button.png", (400, 140))
        button4 = PlatformButton("images/button.png", (475, 240))

        # Create moving platform
        black_platform = MovingPlatform(map.get_barriers()[0][5], 250, 330)

        # Create color pits
        orange_pit = ColourPit((150, 50, 200), (550, 453, 30, 20))
        purple_pit = ColourPit((200, 100, 50), (150, 453, 30, 20))
        orange_pit2 = ColourPit((150, 50, 200), (400, 247, 30, 20))
        purple_pit2 = ColourPit((200, 100, 50), (300, 247, 30, 20))

        mainClock = pygame.time.Clock()

        # loop #
        while True:
            # draw and blit the objects
            screen.blit(wallpaper, (0, 0))

            p1.move(map.get_barriers())
            p2.move(map.get_barriers())

            # draw players, doors, buttons and colour pits
            p1.draw(screen)
            p2.draw(screen)
            fdoor.draw(screen)
            pdoor.draw(screen)
            button1.draw(screen)
            button2.draw(screen)
            button3.draw(screen)
            button4.draw(screen)
            orange_pit.draw(screen)
            purple_pit.draw(screen)
            orange_pit2.draw(screen)
            purple_pit2.draw(screen)
            black_platform.move_platform(screen)

            # Draw the barriers including walls
            for tile in map.get_barriers()[0]:
                pygame.draw.rect(screen, (100, 100, 100), tile)

            # check if the players are touching thier opposite colour pits
            if orange_pit.check_player(
                    p1.get_rect()) or orange_pit2.check_player(p1.get_rect()):
                p1.set_position((50, 440))
            if purple_pit.check_player(
                    p2.get_rect()) or purple_pit2.check_player(p2.get_rect()):
                p2.set_position((100, 440))

            # ends game when the players are touching their doors
            if fdoor.check_player(p1.get_rect()) and pdoor.check_player(
                    p2.get_rect()):
                return "menu"

            button1.check_pressed(p1.get_rect(), p2.get_rect())
            button2.check_pressed(p1.get_rect(), p2.get_rect())
            button3.check_pressed(p1.get_rect(), p2.get_rect())
            button4.check_pressed(p1.get_rect(), p2.get_rect())

            # check if players are touching any of the buttons
            if button1.is_touched() or button2.is_touched():
                new_barrier = pygame.Rect(650, 415, 70, 20)
                if new_barrier not in map.get_barriers()[0]:
                    map.get_barriers()[0].append(new_barrier)
            else:
                barrier_to_remove = pygame.Rect(650, 415, 70, 20)
                if barrier_to_remove in map.get_barriers()[0]:
                    map.get_barriers()[0].remove(barrier_to_remove)

            if button3.is_touched() or button4.is_touched():
                new_barrier = pygame.Rect(650, 215, 70, 20)
                if new_barrier not in map.get_barriers()[0]:
                    map.get_barriers()[0].append(new_barrier)
            else:
                barrier_to_remove = pygame.Rect(650, 215, 70, 20)
                if barrier_to_remove in map.get_barriers()[0]:
                    map.get_barriers()[0].remove(barrier_to_remove)

            # Event handling
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        p1.t_right()
                    if event.key == K_LEFT:
                        p1.t_left()
                    if event.key == K_UP:
                        p1.t_up()
                    if event.key == K_d:
                        p2.t_right()
                    if event.key == K_a:
                        p2.t_left()
                    if event.key == K_w:
                        p2.t_up()
                if event.type == KEYUP:
                    if event.key == K_RIGHT:
                        p1.f_right()
                    if event.key == K_LEFT:
                        p1.f_left()
                    if event.key == K_DOWN:
                        p1.f_up()
                    if event.key == K_d:
                        p2.f_right()
                    if event.key == K_a:
                        p2.f_left()
                    if event.key == K_w:
                        p2.f_up()

            # Update display
            pygame.display.update()
            mainClock.tick(60)
