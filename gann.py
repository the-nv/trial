# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 01:25:33 2022

@author: nverm
"""

import numpy as np

class GannSquare():
    """An container object for Gann Square"""

    def __init__(self, size, date='2007-03-21'):

        """ attributes and method of Gann Square
            input parameters: size
            output returned: an object along with its attributes
        """
        self.size = size
        self.even_size = size % 2 == 0
        self.odd_size = size % 2 == 1
        self.num_elements = size ** 2
        
        self.date = date
        
        self.matrix = self.generate()
        
        self.horizontal_axis = self.get_horizontal_axis()
        self.vertical_axis = self.get_vertical_axis()
        self.diagonal_1 = self.get_diagonal_1()
        self.diagonal_2 = self.get_diagonal_2()
        self.diagonal_axis = self.get_diagonal_axis()

        
    def generate(self):
        """
        generate a Gann Square based on the input parameter size
        """
        from numpy import array
        NORTH, SOUTH, EAST, WEST = (0, 1), (0, -1), (1, 0), (-1, 0) # directional vectors
        clockwise = {
            WEST:NORTH,
            NORTH: EAST, 
            EAST: SOUTH, 
            SOUTH: WEST
        } # clockwise transformation
        
        RIGHT, LEFT = 1, -1
        # forward or backward increment

        if self.size < 1:
            raise ValueError
        x, y = self.size // 2, self.size // 2 
        # the middle of the box
        dx, dy =  WEST # initial direction
        inc = LEFT # backward increment

        G = [[None] * self.size for _ in range(self.size)]
        
        count = 0

        while True:
            count += 1
            G[x][y] = count # visit
            # follow predefined direction
            _dx, _dy = clockwise[dx,dy]
            _x, _y = x +inc* _dx, y +inc* _dy

            if (0 <= _x < self.size and 0 <= _y < self.size and
                G[_x][_y] is None): 
                # in the box
                x, y = _x, _y
                dx, dy = _dx, _dy

            else: # fill in the box
                x, y = x +inc* dx, y +inc* dy
                if not (0 <= x < self.size and 0 <= y < self.size):
                    return array(G) # out of the box
    
    def display_matrix(self):
        width = len(str(max(e for row in self.matrix for e in row if e is not None)))
        fmt = "{:0%dd}" % width
        for row in self.matrix:
            print(" ".join("_"*width if e is None else fmt.format(e) for e in row))
            
    def get_horizontal_axis(self):
        return self.matrix[self.size//2, :]
    
    def get_vertical_axis(self):
        return self.matrix[:, self.size//2]
    
    def get_diagonal_1(self):
        diagonal_1 = []
        for i in range(self.size):
            diagonal_1.append(self.matrix[i,self.size-i-1])
        return diagonal_1
    
    def get_diagonal_2(self):
        diagonal_2 = []
        for i in range(self.size):
            diagonal_2.append(self.matrix[i,i])
        return diagonal_2
    
    def get_diagonal_axis(self):
        from numpy import concatenate
        return concatenate((self.diagonal_1, self.diagonal_2))
    
    def get_0(self):
        horizontal_axis = self.get_horizontal_axis()
        res = list(horizontal_axis[len(horizontal_axis)//2:])
        
        dateRes = [self.date + np.timedelta64(i - 1, 'D') for i in res]
        
        return res, dateRes
    
    def get_180(self):
        horizontal_axis = self.get_horizontal_axis()
        res = list(horizontal_axis[:len(horizontal_axis)//2 + 1])[::-1]
        
        dateRes = [self.date + np.timedelta64(i - 1, 'D') for i in res]
        
        return res, dateRes
    
    def get_45(self):
        diagonal_1 = self.get_diagonal_1()
        res = list(diagonal_1[:len(diagonal_1)//2 + 1])[::-1]
        
        dateRes = [self.date + np.timedelta64(i - 1, 'D') for i in res]
        
        return res, dateRes

    def get_225(self):
        diagonal_1 = self.get_diagonal_1()
        res = list(diagonal_1[len(diagonal_1)//2:])
        
        dateRes = [self.date + np.timedelta64(i - 1, 'D') for i in res]
        
        return res, dateRes
    
    def get_90(self):
        vertical_axis = self.get_vertical_axis()
        res = list(vertical_axis[:len(vertical_axis)//2 + 1])[::-1]
        
        dateRes = [self.date + np.timedelta64(i - 1, 'D') for i in res]
        
        return res, dateRes

    def get_270(self):
        vertical_axis = self.get_vertical_axis()
        res = list(vertical_axis[len(vertical_axis)//2:])
        
        dateRes = [self.date + np.timedelta64(i - 1, 'D') for i in res]
        
        return res, dateRes
    
    def get_135(self):
        diagonal_2 = self.get_diagonal_2()
        res = list(diagonal_2[:len(diagonal_2)//2 + 1])[::-1]
        
        dateRes = [self.date + np.timedelta64(i - 1, 'D') for i in res]
        
        return res, dateRes

    def get_315(self):
        diagonal_2 = self.get_diagonal_2()
        res = list(diagonal_2[len(diagonal_2)//2:])
        
        dateRes = [self.date + np.timedelta64(i - 1, 'D') for i in res]
        
        return res, dateRes
