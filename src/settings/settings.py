import pygame
from src.util.utils import load_image

FPS = 30

tile_width = 50
tile_height = 50

settings = dict()

all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()

borders_group = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
interaction_group = pygame.sprite.Group()

tile_images = {
    "wall": load_image("box.png"),
    "empty": load_image("grass.png"),

    "door_closed": load_image("closed_door.png"),
    "door_opened": load_image("opened_door.png"),
}
player_image = load_image("mario.png")
