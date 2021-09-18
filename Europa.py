# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class EU():
    def __init__(self, name, year, up, down, width, garbanzo):
        self.name = name
        self.year = year
        self.up = up
        self.down = down
        self.width = width
        self.garbanzo = garbanzo

    def toString(self):
        print('Name:',self.name,'/Year:',self.year,'/Up:',
              self.up,'/Down:',self.down,'/Width:',self.width,
              'Le gusta los garbanzos:',self.garbanzo)
                
persona = EU('Paco','1957','1.82','40','61','SI')

persona.toString()