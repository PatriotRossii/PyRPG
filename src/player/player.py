from enum import Enum

import pygame

from src.settings.settings import all_sprites, player_group, borders_group, player_image
from src.settings.settings import tile_width, tile_height, settings


class Direction(Enum):
    LEFT = 1,
    RIGHT = 2,
    UP = 3,
    DOWN = 4,


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, player_group)

        self.height = None
        self.width = None
        self.direction = None

        self.pos = (pos_x, pos_y)

        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5
        )

    def load_size_of_screen(self):
        self.height = settings["height"]
        self.width = settings["width"]

    def move(self, dx, dy):
        dx = tile_width * dx
        dy = -tile_height * dy

        if 0 <= self.rect.x + dx <= self.width and 0 <= self.rect.y + dy <= self.height:
            source_rect = self.rect
            self.rect = self.rect.move(dx, dy)

            if pygame.sprite.spritecollideany(self, borders_group):
                self.rect = source_rect
                return

        self.pos = (self.pos[0] + dx, self.pos[1] + dy)

    def get_direction(self):
        return self.direction

    def set_direction(self, direction: Direction):
        self.direction = direction

    def get_pos(self):
        return self.pos
