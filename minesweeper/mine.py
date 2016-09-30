import sys


class mine:
    x = 0
    y = 0
    mine_count = 0
    map = []
    mine = 'X'
    empty = 'O'

    def __init__(self, x=10, y=10, mine_count=10):
        self.x = x
        self.y = y
        self.mine_count = mine_count


