# Author: Alexander Zakharov

from errors import InvalidColor


class Figure(object):

    __colors = {'w', 'b'}

    def __init__(self, color, pos):
        self.color = color
        self.pos = pos
        self.__symbols__ = {'w': None, 'b': None}

    def assert_legal_move(self, value):
        raise NotImplementedError('Method is abstract')

    @staticmethod
    def assert_correct_move_value(value):
        if type(value) != tuple or len(value) != 2:
            raise ValueError('Move must be tuple and has length of 2')

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        if type(value) != str or value not in self.__colors:
            raise InvalidColor('Color {color} is not correct'.format(color=value))
        self.__color = value

    @property
    def __symbols(self):
        return self.__symbols__

    @property
    def pos(self):
        return self.__pos

    @pos.setter
    def pos(self, value):
        if hasattr(self, '_Figure__pos'):
            self.assert_legal_move(value)
        else:
            self.assert_correct_move_value(value)
        self.__pos = value

    @property
    def symbol(self):
        return self.__symbols[self.color]

    def __str__(self):
        return self.symbol