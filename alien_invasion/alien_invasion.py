import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # make a ship
    ship = Ship(ai_settings,screen)

    #Start the main loop for the game
    while True:
        gf.check_events(ship)
        ship.update()
        # Redraw the screen
        gf.update_screen(ai_settings, screen, ship)
print("THANgitgiKS FOR PLAYING")
run_game()
