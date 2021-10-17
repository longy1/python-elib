#!/usr/bin/ python3
# -*- coding: utf-8 -*-

'Abstract Factory'

__author__ = 'Ethan Long'

from abc import ABCMeta, abstractmethod

from creational_01_base_maze_class import *


# not a pure virtual class, that's ok
class MazeFactory(metaclass=ABCMeta):

    def __init__(self):
        pass

    def make_maze(self):
        return Maze()

    def make_wall(self):
        return Wall()

    def make_door(self, room1, room2):
        return Door(room1, room2)

    def make_room(self, room_no):
        return Room(room_no)


# we can easily implement a new factory making diff rooms
class EnchantedMazeFactory(MazeFactory):

    def __init__(self):
        super().__init__()

    def make_room(self, room_no):
        return EnchantedRoom(room_no)

    def make_door(self, room1, room2):
        return DoorNeedingSpell(room1, room2)


class EnchantedRoom(Room):

    def __init__(self, room_no):
        super().__init__(room_no)


class DoorNeedingSpell(Door):

    def __init__(self, room1, room2):
        super().__init__(room1, room2)


if __name__ == '__main__':
    # create maze with abstract factory pattern
    def create_maze(maze_factory):
        a_maze = maze_factory.create_maze()
        room1 = maze_factory.make_room(1)
        room2 = maze_factory.make_room(2)
        door = maze_factory.make_door(room1, room2)

        a_maze.add_room(room1)
        a_maze.add_room(room2)

        r1.set_side(direction.north, Wall())
        r1.set_side(direction.east, door1)
        r1.set_side(direction.south, Wall())
        r1.set_side(direction.west, Wall())

        r2.set_side(direction.north, Wall())
        r2.set_side(direction.east, wall())
        r2.set_side(direction.south, Wall())
        r2.set_side(direction.west, door1)