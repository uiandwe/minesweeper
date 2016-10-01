from .map import map
import random, sys


class mine:
    x = 0
    y = 0
    mine_count = 0
    mine = 'X'
    empty = 0
    mine_map = []

    def __init__(self, x=10, y=10, mine_count=10):
        self.x = x
        self.y = y
        self.mine_map = map(x, y).map
        self.mine_count = mine_count

    def exception_check_mine_obj(self):
        if len(self.mine_map) == 0:
            sys.exit(" sweeper init error. ")

    def exception_check_mine_size(self):
        if self.x <= 0 or self.y <= 0:
            sys.exit(" mine map size size should be greater than zero. ")

    '''
    map 에 줌 랜덤 좌표로 mine 을 넣어줌
    '''
    def create_mine(self):

        self.exception_check_mine_obj()
        self.exception_check_mine_size()

        check_mine = 0
        while check_mine < self.mine_count:
            mine_x = random.randrange(1, self.x-1)
            mine_y = random.randrange(1, self.y-1)

            if self.mine_map[mine_x][mine_y] != self.mine:
                self.mine_map[mine_x][mine_y] = self.mine
                check_mine += 1
