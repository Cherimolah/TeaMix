import random
from typing import NoReturn, List

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
        self.x_length = 9
        self.y_length = 9
        super(Field, self).__init__(SafeList([SafeList([None for _ in range(self.x_length)],
                                                       default=Tile()) for _ in range(self.y_length)]),
                                    default=SafeList(default=Tile()))

    def get(self, x: int, y: int) -> Tile:
        return self[y][x]

    def set(self, number: int, x: int, y: int):
        tile = Tile(number, x, y)
        self[y][x] = tile

    def row(self, row_id: int) -> List[Tile]:
        return self[row_id]

    def column(self, column_id: int) -> List[Tile]:
        return SafeList([x[column_id] for x in self], default=Tile())

    def _check_previous_column(self, tile: Tile) -> bool:
        return not (self.get(tile.x - 1, tile.y).number == self.get(tile.x - 2, tile.y).number == tile.number)

    def _check_previous_line(self, tile: Tile) -> bool:
        return not (self.get(tile.x, tile.y - 1).number == self.get(tile.x, tile.y - 2).number == tile.number)

    def _check_previous(self, tile: Tile) -> bool:
        return self._check_previous_line(tile) and self._check_previous_column(tile)

    def check_row(self, row_id: int) -> bool:
        row = self.row(row_id)
        for i in range(len(row) - 2):
            if row[i].number == row[i + 1].number == row[i + 2].number:
                return True
        return False

    def check_column(self, column_id: int) -> bool:
        row = self.column(column_id)
        for i in range(len(row) - 2):
            if row[i].number == row[i + 1].number == row[i + 2].number:
                return True
        return False

    def init_tiles(self) -> NoReturn:
        for y in range(self.y_length):
            for x in range(self.x_length):
                tile = Tile(random.randint(0, 5), x, y)
                while not self._check_previous(tile):
                    tile = Tile(random.randint(0, 5), x, y)
                self.set(tile.number, x, y)

    def swap(self, tile1: Tile, tile2: Tile) -> NoReturn:
        self.set(tile2.number, tile1.x, tile1.y)
        self.set(tile1.number, tile2.x, tile2.y)

    def exist_steps(self):
        steps = []
        for y in range(self.y_length):
            for x in range(self.x_length):
                if x < self.x_length - 1:
                    tile1 = self.get(x, y)
                    tile2 = self.get(x + 1, y)
                    self.swap(tile1, tile2)
                    if self.check_column(x) or self.check_column(x + 1) or self.check_row(y):
                        steps.append([tile1, tile2])
                    self.set(tile1.number, tile1.x, tile1.y)
                    self.set(tile2.number, tile2.x, tile2.y)
                if y < self.y_length - 1:
                    tile1 = self.get(x, y)
                    tile2 = self.get(x, y + 1)
                    self.swap(tile1, tile2)
                    if self.check_row(y) or self.check_row(y + 1) or self.check_column(x):
                        steps.append([tile1, tile2])
                    self.set(tile1.number, tile1.x, tile1.y)
                    self.set(tile2.number, tile2.x, tile2.y)
        return steps
