import pygame

from src.level.level import generate_level, load_level
from src.player.camera import Camera
from src.player.player import Direction
from src.settings.settings import all_sprites, tiles_group, player_group, FPS, settings
from src.util.utils import terminate

map_file = input()
try:
    level = load_level(map_file)
    player, level_x, level_y = generate_level(level)

    width = (level_x + 1) * 50
    height = (level_y + 1) * 50

    settings["width"] = width
    settings["height"] = height

    player.load_size_of_screen()
except FileNotFoundError as e:
    print(e)
    terminate()


pygame.init()
pygame.display.set_caption("Игра")
screen = pygame.display.set_mode((width, height))


def draw_frame(screen):
    screen.fill((0, 0, 0))

    tiles_group.draw(screen)
    player_group.draw(screen)

    pygame.display.flip()


if __name__ == "__main__":
    camera = Camera()
    clock = pygame.time.Clock()

    draw_frame(screen)

    while True:
        camera.update(player)
        for sprite in all_sprites:
            camera.apply(sprite)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_w, pygame.K_s):
                    up = event.key == pygame.K_w
                    player.move(0, 1 if up else -1)
                    player.set_direction(Direction.UP if up else Direction.DOWN)
                if event.key in (pygame.K_d, pygame.K_a):
                    right = event.key == pygame.K_d
                    player.move(1 if right else -1, 0)
                    player.set_direction(Direction.RIGHT if right else Direction.LEFT)
                draw_frame(screen)

        clock.tick(FPS)
