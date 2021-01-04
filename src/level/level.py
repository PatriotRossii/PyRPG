from src.player.player import Player
from src.tile.complex_objects.door import Door
from src.tile.tile import Tile


def load_level(filename):
    filename = "../resources/maps/" + filename
    with open(filename, 'r') as map_file:
        level_map = [line.strip() for line in map_file]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == ".":
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y, True)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
            elif level[y][x] == "D":
                Door(x, y)
    return new_player, x, y
