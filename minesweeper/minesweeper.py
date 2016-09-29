__author__ = 'uiandwe'

import random

class mine_Sweeper:

    x = 0
    y = 0
    mine = 0
    map = []

    def __init__(self):
        self.x = 10
        self.y = 10
        self.mine = 10

    def create_map(self):
        for i in range(self.x):
            temp_map_array = []
            for j in range(self.y):
                temp_map_array.append("O")
            self.map.append(temp_map_array)

    def create_mine(self):
        for i in range(self.mine):
            mine_x = random.randrange(0, self.x)
            mine_y = random.randrange(0, self.y)

            self.map[mine_x][mine_y] = 'X'

    def view_map(self):
        for i in range(len(self.map)):
            print(self.map[i])


if __name__ == '__main__':

    m = mine_Sweeper()
    m.create_map()
    m.create_mine()
    m.view_map()
