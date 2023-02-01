import random
from typing import NoReturn

from framework.tile import Tile


class SafeList(list):

    def __init__(self, *args, default=None):
        super(SafeList, self).__init__(*args)
        self.default_value = default

    def __getitem__(self, item: int):
        if item < 0 or item >= len(self):
            return self.default_value
        return super().__getitem__(item)


class Field(SafeList):

    def __init__(self):
        super(Field, self).__init__(SafeList([SafeList([None for _ in range(9)], default=Tile()) for _ in range(9)]),
                                    default=SafeList(default=Tile()))

    def get(self, x: int, y: int) -> Tile:
        return self[y][x]

    def set(self, value: Tile, x: int, y: int):
        self[y][x] = value

    def _check_previous_column(self, tile: Tile) -> bool:
        return not (self.get(tile.x - 1, tile.y).number == self.get(tile.x - 2, tile.y).number == tile.number)

    def _check_previous_line(self, tile: Tile) -> bool:
        return not (self.get(tile.x, tile.y - 1).number == self.get(tile.x, tile.y - 2).number == tile.number)

    def _check_previous(self, tile: Tile) -> bool:
        return self._check_previous_line(tile) and self._check_previous_column(tile)

    def init_tiles(self) -> NoReturn:
        for y in range(9):
            for x in range(9):
                tile = Tile(random.randint(0, 5), x, y)
                while not self._check_previous(tile):
                    tile = Tile(random.randint(0, 5), x, y)
                self.set(tile, x, y)
