# pan.py

import pygame
from .constants import COOKED_PERFECT

class Pan(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/pan.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.contents = COOKED_PERFECT

    def update(self):
        pass
