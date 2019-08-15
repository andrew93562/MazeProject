# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 09:04:39 2019

@author: socksandstilettos
"""

from enum import Enum

class MapSite():
    
    def Enter(self):
        raise NotImplementedError('Abstract Base Class Method')

class Direction(Enum):
    North =  0
    East  =  1
    South =  2
    West  =  3
    
class Room(MapSite):
    
    def __init__(self, roomNo):
        self._sides = (Mapsite) * 4
        self._roomNumber = int(roomNo)

    def GetSide(self, Direction):
        return self._sides(Direction)
    
    def SetSide(self, direction, MapSite):
        self._sides(Direction) = Mapsite
        
    def Enter(self):
        print('    You have entered room: ' + str(self._roomNumber))
        
class Wall(MapSite):
    
    def Enter(self):
        print('    You just ran into a Wall...')
        
class Door(Mapsite):
    
    def __init__(self, Room1 = None, Room2 = None):
        self._room1 = Room1
        self._room2 = Room2
        self._isOpen = False
        
    def OtherSideFrom(self, Room):
        print('\tDoor obj: This door is a side of Room: ()'.format(Room._roomNumber))
        if 1 == Room._roomNumber:
            other_room = self._room2
        else:
            other_room = self._room1
        return other_room
    
    def Enter(self):
        if self.isOpen: Print('    **** You have passed through this door...')
        else: print('    ** This door needs to be opened before you can pass through it...')

class Maze():
