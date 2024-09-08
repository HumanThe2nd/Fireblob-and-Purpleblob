from level_one import level_one
from menu import main_menu
from selector import level_selector

#start the game at the menu
display = "menu"
while(True):
  if display=="quit":
    print("Game Closed. Thanks for playing!")
    break
  if display=="menu":
    display = main_menu.open_menu()
  elif display=="settings":
    print("Setiings")
  elif display=="selector":
    ls = level_selector()
    display = ls.display_level_selector()
  elif display == "level one":
    display = level_one.run_game()
