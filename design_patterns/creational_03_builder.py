#!/usr/bin/python3
# -*- coding: utf-8 -*-

'Builder pattern'

__author__ = 'Ethan Long'

from abc import ABCMeta, abstractmethod

from creational_01_base_maze_class import *


class MazeBuilder:

    def __init__(self):
        pass

    def build_maze(self):
        pass

    def build_room(self, room_no):
        pass

    def build_door(self, room1, room2):
        pass

    def get_maze(self):
        pass
        