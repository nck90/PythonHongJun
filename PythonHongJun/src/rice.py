# rice.py

import pygame

class Rice(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/rice.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
