aimport pygame
from button import button

class level_selector:

  pygame.init()
  background = pygame.image.load("images/selector.jpeg")
  title_font = pygame.font.Font(None, 160)
  title = title_font.render("Select Level", True, "White")
  title_rect = title.get_rect(midtop = (360, 20))
  size = (720, 480)
  screen = pygame.display.set_mode(size)

  screen.blit(title, title_rect)
  font = pygame.font.Font(None, 80)
  button1 = button((600, 50), (60, 150), font, "Level 1")
  button2 = button((600, 50), (60, 200), font, "Level 2")
  button3 = button((600, 50), (60, 250), font, "Level 3")
  menu_button = pygame.image.load('images/menu.png')
  menu_button_rect = menu_button.get_rect(midtop = (360, 350))
  button1_rect = button1.get_rect()
  buttons = [button1, button2, button3]
  
  def display_level_selector(self): 
    """
    displays the level selector screen

    returns:
    (str): used to determine which screen to switch to after this screen. For example: menu and level 1
    """
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.menu_button_rect.collidepoint(mouse_pos):
                    return "menu"
                elif self.button1_rect.collidepoint(mouse_pos):
                    return "level one"
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.title, self.title_rect)
        for Button in self.buttons:
            Button.draw(self.screen)
            if Button._rect.collidepoint(pygame.mouse.get_pos()):
                Button.mouse_hover()
            else:
                Button.mouse_off()
        self.screen.blit(self.menu_button, self.menu_button_rect)
        pygame.display.flip()
