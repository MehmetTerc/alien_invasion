import pygame

class Ship:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.settings = ai_game.settings
        self.x = float(self.rect.x)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            if self.moving_right:
                self.rect.x += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            if self.moving_left:
                self.rect.x -= self.settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            if self.moving_down:
                self.rect.y += self.settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            if self.moving_up:
                self.rect.y -= self.settings.ship_speed_factor
    def blitme(self):
        self.screen.blit(self.image, self.rect)