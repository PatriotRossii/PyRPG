from src.settings.settings import tile_images, borders_group
from src.tile.tile import Tile


class Door(Tile):
    def __init__(self, pos_x, pos_y):
        super().__init__("door_closed", pos_x, pos_y, border=True)

    def open(self):
        self.image = tile_images["door_opened"]
        borders_group.remove(self)

    def close(self):
        self.image = tile_images["door_closed"]
        borders_group.add(self)
