# Author: Alexander Zakharov


class Board(object):
    def __init__(self, height=10, width=None):
        self.__height = height
        if width:
            self.__width = width
        else:
            self.__width = height

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    def __str__(self):
        return '<{classname} {height}x{width}>'.format(classname=self.__class__.__name__,
                                                       height=self.height,
                                                       width=self.width)

    __repr__ = __str__
