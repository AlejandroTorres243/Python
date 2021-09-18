# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 15:45:48 2021

@author: Manuel
"""

# Attempt this with paitience and remeber that you'll only succed when you fail
# Start off by creating the Guest class and it's methods
class Guest():

    def __init__(self, name):
        self.name = name.lower().capitalize()
        self.dict1 = {'John':'A011', 'Kyle': 'A009', 'Jake':'BQ02', 'Tamra':'A015', 'Josh':'BQ03'}
        self.kys = ['A010', 'A012', 'A014', 'BQ01']      
        self.regd = self.name in self.dict1
    def is_regd(self):
        if(self.regd):
            print('Registered')
        else:
            print('No registered')
    def get_key(self):
        if self.kys:
            print(f'Key :{self.dict[self.name]}')
        else: 
            print('Not Registered')
    def reg(self):
        if len(self.kys) < 1:
            print('Is not available in the room')
        else:
            self.dict1[self.name] = self.kys[0]
            self.kys.pop(0)
            self.reg = True

cad_name = ['Josh', 'Hans', 'Evan', 'Kyle', 'Ted', 'Karl', 'Sam']

for guest_name in cad_name:

    gst = Guest(guest_name)
    print(gst.name)
    gst.is_regd()

    if gst.regd:
        gst.get_key

    else:
        gst.reg
        gst.get_key
