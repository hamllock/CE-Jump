import pygame
from random import choice, randrange
import random

vec = pygame.math.Vector2

# Library of game constants
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)
yellow = (255, 255, 0)
orange = (255, 196, 0)
spritesheet_file_name = "spritesheet_jumper.png"
platform_colors = [(0, 0, 0), (200, 0, 0), (255, 255, 255),
                   (0, 200, 0), (255, 255, 0), (255, 196, 0)]
display_width = 600
display_height = 800
fps = 60
block_width = 50
block_height = 100
player_Acc = 8
player_Fric = -0.06
gravity = 0.3
Font_Name = "scoreboard"
hs_file = "highscore.txt"
power_up_boost = -40
power_up_spawn_freq = 7
enemies_freq = 5000  # time in ms


class SpriteSheet:
    def __init__(self):
        self.spritesheet = pygame.image.load(
            'spritesheet_jumper.png').convert()

    def imageLoad(self, x, y, width, height):
        image = pygame.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        image = pygame.transform.scale(image, (width//3, height//3))
        return image


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img_cechar_sprite = pygame.sprite.Sprite()
        self.img_cechar_sprite.image = pygame.image.load(
            'cechar.png').convert()
        self.img_cechar_sprite.rect = self.img_cechar_sprite.image.get_rect()
        self.pos = vec(display_width / 2, display_height - 100)
        self.img_cechar_sprite.rect.topleft = [self.pos.x, self.pos.y]
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.mask_image = pygame.mask.from_surface(
            self.img_cechar_sprite.image)


class Platform(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game

    def getPlatform(self, x, y, images):
        self.image = choice(images)
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        if randrange(100) < power_up_spawn_freq:
            PowerUps(self, self.game)

    def getImages(self):
        self.spritesheetsobj = SpriteSheet()
        self.images = [self.spritesheetsobj.imageLoad(0, 768, 380, 94),
                       self.spritesheetsobj.imageLoad(213, 1662, 201, 100)]
        return self.images


class lowPlatform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h))
        color = platform_colors[random.randrange(0, len(platform_colors))]
        self.image = pygame.image.load('layer-2.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Enemies(pygame.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.spritesheetsobj = SpriteSheet()
        self.image_up = self.spritesheetsobj.imageLoad(566, 510, 122, 139)
        self.image_up.set_colorkey(black)
        self.image_down = self.spritesheetsobj.imageLoad(568, 1534, 122, 135)
        self.image_down.set_colorkey(black)
        self.image = self.image_up
        self.rect = self.image.get_rect()
        self.rect.centerx = random.choice([-100, display_width + 100])
        self.vx = random.randrange(1, 4)
        if self.rect.centerx > display_width:
            self.vx = -self.vx
        self.rect.y = random.randrange(0, display_height/2)
        self.vy = 0
        self.dy = 0.5

    def update(self):
        self.rect.x += self.vx
        self.vy += self.dy
        if self.vy > 3 or self.vy < -3:
            self.dy = -self.dy
        center = self.rect.center
        if self.dy < 0:
            self.image = self.image_up
        else:
            self.image = self.image_down
        self.rect = self.image.get_rect()
        self.mask_image = pygame.mask.from_surface(self.image)
        self.rect.center = center
        self.rect.y += self.vy
        if self.rect.left > display_width + 100 or self.rect.right < -100:
            self.kill()


class PowerUps(pygame.sprite.Sprite):
    def __init__(self, platform, game):
        self.groups = game.powerups
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.plat = platform
        self.spritesheetsobj = SpriteSheet()
        self.image = self.spritesheetsobj.imageLoad(563, 1843, 133, 160)
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (133//6, 160//6))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.plat.rect.centerx
        self.rect.bottom = self.plat.rect.top - 5

        print("Power-UP ADDED!")

    def update(self):
        self.rect.bottom = self.plat.rect.top - 5
        if not self.game.platforms.has(self.plat):
            self.kill()
