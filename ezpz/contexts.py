from enum import Enum

class Context(Enum):
    WORLD = 0
    SCREEN = 1
    OVERLAY = 2

class Anchor(Enum):
    NW = 0
    N = 1
    NE = 2
    W = 3
    C = 4
    E = 5
    SW = 6
    S = 7
    SE = 8
