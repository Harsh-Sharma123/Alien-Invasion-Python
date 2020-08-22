import pygame
from Settings import Settings
from Ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard


def run_game():
    # Initialize game here and creating a ship object
    pygame.init()    #it initializes the background setting needed by pygame to run properly
    ai_settings = Settings()     #instance of the settings class
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Create an instance to store the game statistics and scoreboard.
    stats = GameStats(ai_settings)
    sb = ScoreBoard(ai_settings, screen, stats)

    #Make the play button.
    play_button = Button(ai_settings, screen, "Play")

    #Make a ship
    ship = Ship(ai_settings ,screen)

    #Make a group to store bullets in.
    bullets = Group()

    #Make a group of Aliens.
    aliens = Group()

    #Create the fleet of the aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Starting the main loop for the game

    while True:

        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()

