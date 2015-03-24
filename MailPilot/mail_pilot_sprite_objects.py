""" mail_pilot.py
    Sprite classes for mail_pilot.py
    Designed by Andy Harris, programmed by Mike Overby
    12-28-2013 """

import pygame, random
pygame.init

SCROLLING_SPEED = 5

class Sea(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/sea.gif")
        self.rect = self.image.get_rect()

        #Check if the sea image will work
        if self.rect.height != screen.get_height() * 3 or self.rect.width != screen.get_width():
            print("Error: The sea image is an abnormal size (not screen_height * 3). The sea will not look right.")
        
        self.reset(screen)

        self.dy = SCROLLING_SPEED

    def update(self, screen):
        #Scroll the sea down, dy should be constant with island speed.
        self.rect.top += self.dy

        if self.rect.top == 0:
            self.reset(screen)

    def reset(self, screen):
        self.rect.top = screen.get_height() * -2

class Plane(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/plane.gif")
        self.rect = self.image.get_rect()
        self.yay = pygame.mixer.Sound("assets/yay.ogg")
        self.thunder = pygame.mixer.Sound("assets/thunder.ogg")
        self.engine = pygame.mixer.Sound("assets/plane_engine.ogg")

    def update(self):
        current_x, y = pygame.mouse.get_pos()
        self.rect.center = (current_x, 440)

class Island(pygame.sprite.Sprite):
    def __init__(self, screen): #here is where the parameters must be listed.
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/island.gif")
        self.rect = self.image.get_rect()

        self.reset(screen)

    def update(self, screen):
        self.dy = SCROLLING_SPEED
        self.rect.centery += self.dy
        if self.rect.top > screen.get_height():
            self.reset(screen)

    def reset(self, screen):
        #reset rect above the screen, so it scrolls in
        self.rect.bottom = 0
        #Reset x position
        #"self.rect.width/2" ensures that the whole island will always be on screen.
        self.rect.centerx = random.randrange(0 + self.rect.width/2, screen.get_width() - + self.rect.width/2)

class Cloud(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/cloud.gif")
        self.rect = self.image.get_rect()

        self.reset(screen)

    def update(self, screen):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        if self.rect.top >= screen.get_height():
            self.reset(screen)

        if self.rect.left > screen.get_width():
            self.reset(screen)

        if self.rect.right < 0:
            self.reset(screen)

    def reset(self, screen):
        #reset rect above the screen, so it scrolls in
        self.rect.bottom = 0
        #Reset x position
        #midpoint ensures that the whole island will always be on screen. Positions center based on it.
        midpoint = int(self.rect.width/2)
        self.rect.centerx = random.randrange(0 + midpoint, screen.get_width() - midpoint)

        self.dy = random.randrange(SCROLLING_SPEED+1, 10) #SCROLLING_SPEED+1 so clouds never appear to be still.
        self.dx = random.randrange(-3,3)

class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.lives = 5
        self.score = 0
        
        self.font = pygame.font.SysFont("None", 30)

    def update(self):
        self.text  = "Planes: %d, Score: %d" %(self.lives, self.score)
        self.image = self.font.render(self.text, 1, (255,255,255))
        self.rect = self.image.get_rect()
        self.rect.topleft = (20, 20)
