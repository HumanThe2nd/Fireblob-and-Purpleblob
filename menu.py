# Import necessary modules
import pygame as pg
from selector import level_selector
import sys

class main_menu:
    """
    The `main_menu` class represents the main menu interface.
    It contains methods to display the main menu and handle user interactions.
    """

    @staticmethod
    def open_menu():
        """
        Opens the main menu screen where the user can change settings,
        continue, or exit the game.

        Returns: str: "selector" ,"settings" or "quit" when said buttons are clicked.
        """
        print("Menu Opened!")
        pg.init()

        # Set up screen properties
        size = (720, 480)
        screen = pg.display.set_mode(size)
        clock = pg.time.Clock()

        # Load the background and button images
        background = pg.image.load('images/menu.jpg')
        start_button = pg.image.load('images/start.png')
        start_hovered = pg.image.load('images/start_hovered.jpg')
        exit = pg.image.load('images/exit.png')
        exit_hovered = pg.image.load('images/exit_hovered.png')

        # Set the unhovered state of buttons
        start_unhovered = start_button
        exit_unhovered = exit

        # Get the rectangle of the start button image
        start_rect = start_button.get_rect()
        exit_rect = exit.get_rect()
        exit_rect.topright = (720, 0)

        # Position the button in the center of the screen
        start_rect.center = (390, 280)

        # Main game loop
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                # Check for mouse hover and click events on the start button
                if start_rect.collidepoint(pg.mouse.get_pos()):
                    start_button = start_hovered
                    if event.type == pg.MOUSEBUTTONDOWN:
                        print("Menu Closed!\nStart game!")
                        return "selector"   
                else:
                    start_button = start_unhovered

                # Check for mouse hover and click events on the exit button
                if exit_rect.collidepoint(pg.mouse.get_pos()):
                    exit = exit_hovered
                    if event.type == pg.MOUSEBUTTONDOWN:
                        print("Exiting game!")
                        return "quit"
                else:
                    exit = exit_unhovered

            # Draw the background and button images
            screen.blit(background,(0,0))
            screen.blit(start_button, start_rect)
            screen.blit(exit, exit_rect)

            # Update the display
            pg.display.flip()
            clock.tick(60)
