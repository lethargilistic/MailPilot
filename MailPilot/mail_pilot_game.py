""" mail_pilot_game.py
    The game loop for Mail Pilot
    Designed by Andy Harris, programmed by Mike Overby
    Jan 5, 2014 """
import pygame, mail_pilot_sprite_objects
pygame.init()

def game(screen, background):
    sea    = mail_pilot_sprite_objects.Sea(screen)
    island = mail_pilot_sprite_objects.Island(screen)
    plane  = mail_pilot_sprite_objects.Plane()
    cloud1 = mail_pilot_sprite_objects.Cloud(screen)
    cloud2 = mail_pilot_sprite_objects.Cloud(screen)
    cloud3 = mail_pilot_sprite_objects.Cloud(screen)
    scoreboard = mail_pilot_sprite_objects.Scoreboard()
    
#Review organization of the sprite groups.
    sea_sprite  = pygame.sprite.Group(sea)
    island_sprite = pygame.sprite.Group(island)
    plane_sprite  = pygame.sprite.Group(plane)
    cloud_sprites = pygame.sprite.Group(cloud1, cloud2, cloud3)
    scoreboard_sprite = pygame.sprite.Group(scoreboard)
    
    keep_going = True
    done_playing = False
    clock = pygame.time.Clock()

    while keep_going == True:
        clock.tick(30)
        pygame.mouse.set_visible(False)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_going = False
                done_playing = True #Indicating that they want to shut down the game

#Collision Detection

    #Need Sounds. Record sounds via Audacity.
        if plane.rect.colliderect(island.rect):
            plane.yay.play()
            scoreboard.score += 100
            island.reset(screen)

    #This is from Harris's book, pg. 319
        hit_clouds = pygame.sprite.spritecollide(plane, cloud_sprites, False)
        if hit_clouds:
            plane.thunder.play()
            scoreboard.lives -= 1
            if scoreboard.lives == 0:
                keep_going = False #Returns to instructions, but does not shut off game.
                done_playing = False
            for the_cloud in hit_clouds:
                the_cloud.reset(screen)

#Update graphics
        sea_sprite.clear(screen, background)
        island_sprite.clear(screen, background)
        plane_sprite.clear(screen, background)
        cloud_sprites.clear(screen, background)
        scoreboard_sprite.clear(screen, background)
        
        sea_sprite.update(screen)
        island_sprite.update(screen)
        plane_sprite.update()
        cloud_sprites.update(screen)
        scoreboard_sprite.update()
        
        sea_sprite.draw(screen)
        island_sprite.draw(screen)
        plane_sprite.draw(screen)
        cloud_sprites.draw(screen)
        scoreboard_sprite.draw(screen)
        
        pygame.display.flip()
        
    return scoreboard.score, done_playing
