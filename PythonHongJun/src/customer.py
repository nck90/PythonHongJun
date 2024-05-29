# customer.py

import pygame
import random

class Customer(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/customer.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.price_factor = random.uniform(0.5, 1.5)
