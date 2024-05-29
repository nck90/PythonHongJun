# game.py

import pygame
import random
from .pan import Pan
from .rice import Rice
from .customer import Customer
from .constants import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("볶음밥 타이쿤 게임")
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.pans = []
        self.rices = []
        self.customers = []
        self.score = 0
        self.target_score = 10000  
        self.game_over = False
        self.last_customer_time = 0

        for i in range(4):
            pan = Pan((i+1)*150, 500)
            self.all_sprites.add(pan)
            self.pans.append(pan)

        for _ in range(10):
            rice = Rice(random.randint(50, 750), random.randint(50, 450))
            self.all_sprites.add(rice)
            self.rices.append(rice)

    def run(self):
        running = True
        while running:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(WHITE)
            self.all_sprites.update()
            self.all_sprites.draw(self.screen)

            if not self.game_over:
                current_time = pygame.time.get_ticks()
                if current_time - self.last_customer_time > random.randint(5000, 15000):
                    self.spawn_customer()
                    self.last_customer_time = current_time

                for customer in self.customers:
                    for pan in self.pans:
                        if pan.rect.colliderect(customer.rect):
                            self.handle_customer(pan, customer)
                            self.customers.remove(customer)
                            customer.kill()

                if self.score >= self.target_score:
                    self.game_over = True
                    self.show_game_over()

            pygame.display.flip()

        pygame.quit()

    def spawn_customer(self):
        customer = Customer(random.randint(50, 750), 50)
        self.all_sprites.add(customer)
        self.customers.append(customer)

    def handle_customer(self, pan, customer):
        if pan.contents == COOKED_PERFECT:
            self.score += int(PRICE_PERFECT * customer.price_factor)
        elif pan.contents == COOKED_UNDERCOOKED:
            self.score += int(PRICE_UNDERCOOKED * customer.price_factor)
        elif pan.contents == COOKED_BURNT:
            self.score += int(PRICE_BURNT * customer.price_factor)

    def show_game_over(self):
        font = pygame.font.Font(None, 50)
        text = font.render("목표 달성! 점수: {}".format(self.score), True, BLACK)
        text_rect = text.get_rect(center=(400, 300))
        self.screen.blit(text, text_rect)
