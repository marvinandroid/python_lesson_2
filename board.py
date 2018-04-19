# Author: Alexander Zakharov


class ChessBoard(object):

    def __init__(self, height=10, width=None, symbols=None, alphabet=None, cell_width=None):
        self.__height = height
        if width:
            self.__width = width
        else:
            self.__width = height
        self.symbols = symbols
        self.alphabet = alphabet
        self.cell_width = cell_width

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @property
    def symbols(self):
        return self.__symbols

    @symbols.setter
    def symbols(self, value):
        if value and type(value) == dict:
            self.__symbols = value
        else:
            self.__symbols = {
                'ltc': '┏',
                'vb':  '┃',
                'lbc': '┗',
                'hb':  '━',
                'rtc': '┓',
                'rbc': '┛',
                'bl':  '█',
                'wh':  '░'
            }

    @property
    def alphabet(self):
        return self.__alphabet

    @alphabet.setter
    def alphabet(self, value):
        if value and type(value) == str:
            self.__alphabet = value
        else:
            self.__alphabet = 'abcdefghijklmnopqrstuvwxyz'

    @property
    def cell_width(self):
        return self.__cell_width

    @cell_width.setter
    def cell_width(self, value):
        if type(value) == int and value % 2 == 1:
            self.__cell_width = value
            self.__cell_height = int(value/2)
        elif value is None:
            self.__cell_width = 7
            self.__cell_height = 3
        else:
            raise ValueError('Cell width must be odd')

    @property
    def cell_height(self):
        return self.__cell_height

    def __str__(self):
        return '<{classname} {height}x{width}>'.format(classname=self.__class__.__name__,
                                                       height=self.height,
                                                       width=self.width)

    __repr__ = __str__

    def show(self):
        self.__print_alphabet()
        print('  ' + self.symbols['ltc'] + self.symbols['hb']*self.cell_width*self.width + self.symbols['rtc'])
        for line in range(0, self.height):
            cells = (self.symbols['bl']*self.cell_width + self.symbols['wh']*self.cell_width)*self.width
            if line % 2 != 0:
                cells = cells[self.cell_width:]
            cells = cells[:self.width*self.cell_width]
            for n in range(self.cell_height + 1):
                if n == int(self.cell_height/2):
                    print('{n:2d}'.format(n=line + 1) + self.symbols['vb'] + cells +
                          self.symbols['vb'] + '{n:2d}'.format(n=line + 1))
                else:
                    print('  ' + self.symbols['vb'] + cells + self.symbols['vb'])
        print('  ' + self.symbols['lbc'] + self.symbols['hb']*self.cell_width*self.width + self.symbols['rbc'])
        self.__print_alphabet()

    def __print_alphabet(self):
        print('  ', end='')
        for i in range(self.width):
            print(' '*self.cell_height + self.alphabet[i] + ' '*self.cell_height, end='')
        print()