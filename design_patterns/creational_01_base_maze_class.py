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

    def __init__(self, room_no1=0, room_no2=0):
        self._room1 = room1
        self._room2 = room2
        self._is_open = False

    def enter(self):
        pass

    def other_side(self, room_no):
        if self._room1 == room_no:
            return self._room2
        return self._room1


class Maze(object):

    def __init__(self):
        pass

