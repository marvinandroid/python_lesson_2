# -*- coding: utf-8 -*-
# Author: Alexander Zakharov

from figures.figure import Figure
from errors import InvalidMove


class Rook(Figure):

    def __init__(self, color, pos):
        super().__init__(color, pos)
        self.__symbols__ = {'w': '♖', 'b': '♜'}

    def assert_legal_move(self, value):
        self.assert_correct_move_value(value)
        x0, y0 = self.pos
        x1, y1 = value
        if x0 != x1 and y0 != y1:
            raise InvalidMove('Impossible move')