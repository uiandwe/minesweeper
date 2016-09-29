import random


class mine_Sweeper:

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


#예외상황 넣기
    def create_map(self):
        for i in range(self.x):
            temp_map_array = []
            for j in range(self.y):
                temp_map_array.append(self.empty)
            self.map.append(temp_map_array)

#예외상황 넣기
    def create_mine(self):
        check_mine = 0
        while check_mine < self.mine_count:
            mine_x = random.randrange(0, self.x)
            mine_y = random.randrange(0, self.y)

            if self.map[mine_x][mine_y] != self.mine:
                self.map[mine_x][mine_y] = self.mine
                check_mine += 1

    def view_map(self):
        for i in range(len(self.map)):
            print(self.map[i])

    def find_mine(self):
        for i in range(self.x):
            for j in range(self.y):
                if self.map[i][j] != self.mine:
                    self.map[i][j] = self.check_square(i, j)

    def view_square(self, x, y):
        square = []

        for i in range(y-1, y+2):
            temp_array = []
            for j in range(x-1, x+2):
                temp_array.append(self.map[i][j])
            square.append(temp_array)
        return square

    def check_square(self, x, y):
        is_mine = 0
        if x-1 >= 0 and y-1 >= 0 and self.map[x-1][y-1] == self.mine:
            is_mine += 1
        if x >= 0 and y-1 >= 0 and self.map[x][y-1] == self.mine:
            is_mine += 1
        if x+1 < self.x and y-1 >= 0 and self.map[x+1][y-1] == self.mine:
            is_mine += 1

        if x-1 >= 0 and y < self.y and self.map[x-1][y] == self.mine:
            is_mine += 1
        if x+1 < self.x and y < self.y and self.map[x+1][y] == self.mine:
            is_mine += 1

        if x-1 >= 0 and y+1 < self.y and self.map[x-1][y+1] == self.mine:
            is_mine += 1
        if x < self.x and y+1 < self.y and self.map[x][y+1] == self.mine:
            is_mine += 1
        if x+1 < self.x and y+1 < self.y and self.map[x+1][y+1] == self.mine:
            is_mine += 1

        return is_mine

if __name__ == '__main__':

    m = mine_Sweeper()
    m.create_map()
    m.create_mine()
    m.view_map()
    m.find_mine()
    m.view_map()
