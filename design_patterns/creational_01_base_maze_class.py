#!/usr/bin/ python3
# -*- coding: utf-8 -*-

'Base class in Maze creation'

__author__ = 'Ethan Long'

from abc import ABCMeta, abstractmethod
from enum import Enum


class Direction(Enum):
    north = 0
    sounth = 1
    east = 2
    west = 3


class MapSite(metaclass=ABCMeta):

    @abstractmethod
    def enter():
        pass


class Room(MapSite):

    def __init__(self, room_no: int):
        self._roomNumber = room_no
        self._sides = {}

    def get_side(self, direction):
        return self._sides[direction]

    def set_side(self, direction, map_site):
        self._sides[direction] = map_site

    def enter(self):
        # todo: define the actions when enter room
        pass


class Wall(MapSite):

    def __init__(self):
        pass

    def enter(self):
        pass


class Door(MapSite):

    def __init__(self, room1=0, room2=0):
        self._room1 = room1
        self._room2 = room2
        self._is_open = False

    def enter(self):
        pass

    def other_side(self, room_no):
        if self._room1 == room_no:
            return self._room2
        return self._room1


# a new maze example
class Maze(object):

    def __init__(self):
        pass

    def add_room(self, room_no):
        pass

    def get_room_no(self, room):
        pass
            

if __name__ == '__main__':
    # a naive maza create procedure, it usually belongs to a Game class
    def create_maze():
        a_maze = Maze()

        r1 = Room(1)
        r2 = Room(2)
        door1 = Door(r1, r2)

        a_maze.add_room(r1)
        a_maze.add_room(r2)

        r1.set_side(direction.north, Wall())
        r1.set_side(direction.east, door1)
        r1.set_side(direction.south, Wall())
        r1.set_side(direction.west, Wall())

        r2.set_side(direction.north, Wall())
        r2.set_side(direction.east, wall())
        r2.set_side(direction.south, Wall())
        r2.set_side(direction.west, door1)