# -*- coding: utf-8 -*-
# Author: Alexander Zakharov

from figures.figure import Figure
from errors import InvalidMove


class Bishop(Figure):

    def __init__(self, color, pos):
        super().__init__(color, pos)
        self.__symbols__ = {'w': '♗', 'b': '♝'}

    def assert_legal_move(self, value):
        self.assert_correct_move_value(value)
        x0, y0 = self.pos
        x1, y1 = value
        print(x1 - x0)
        print(y1 - y0)
        if x1 - x0 != y1 - y0 or x1 - x0 == 0 or y1 - y0 == 0:
            raise InvalidMove('Impossible move')