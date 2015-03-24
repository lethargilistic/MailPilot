""" mail_pilot.py
    A basic game
    Designed by Andy Harris, programmed by Mike Overby
    12-23-2013 """

import pygame, mail_pilot_game, mail_pilot_instructions, mail_pilot_sprite_objects
pygame.init()

def main():
    resolution = 640, 480
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Mail Pilot")

    background = pygame.Surface(screen.get_size())
    background.fill((0,255,0))

    score = 0 #Dummy text
    done_playing = False
    
    while done_playing == False:
        done_playing = mail_pilot_instructions.instructions(screen, score)
        if not done_playing:
            score, done_playing = mail_pilot_game.game(screen, background)

    pygame.mouse.set_visible(True)
if __name__ == "__main__":
    main()
