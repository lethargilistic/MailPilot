""" mail_pilot.py
    Instruction screen for Mail Pilot
    Designed by Andy Harris, programmed by Mike Overby
    12-23-2013 """

import pygame, mail_pilot_sprite_objects
pygame.init()

def instructions(screen, score):
    """ Instructions screen """
    plane = mail_pilot_sprite_objects.Plane()
    sea   = mail_pilot_sprite_objects.Sea(screen)

    my_font = pygame.font.SysFont("Victoria", 30) #sync font size by passing veriable

    instructions = (
    "Welcome to Mail Pilot! Last Score: %d" %score,
    "These letters must be delivered to the archipelago,",
    "but there's a storm brewing!",
    "",
    "Use the mouse to move left and right.",
    "Avoid the storm clouds or the plane will be destroyed.",
    "Fly over the islands to drop the mail!",
    "",
    "click to continue, escape to exit"
    )

    instruction_label = []
    for line in instructions:
        temp_label = my_font.render(line, 1, (255,255,255))
        instruction_label.append(temp_label)

    keep_going = True
    done_playing = False
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    
    while keep_going == True:
        clock.tick(30) #Sync with game clock with passed variables
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_going = False
                done_playing = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                keep_going = False
                done_playing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keep_going = False
                    done_playing = True

        sea.update(screen)
        plane.update()
        
        screen.blit(sea.image, (0,sea.rect.height * -2/3))
        screen.blit(plane.image, (plane.rect.topleft))

        for i in range(len(instruction_label)):
            screen.blit(instruction_label[i], (50, 30*i + 30))

        pygame.display.flip()
        
    return done_playing
