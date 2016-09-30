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
        for i in range(self.x+2):
            temp_map_array = []
            for j in range(self.y+2):
                temp_map_array.append(self.empty)
            self.map.append(temp_map_array)

#예외상황 넣기
    def create_mine(self):
        check_mine = 0
        while check_mine < self.mine_count:
            mine_x = random.randrange(1, self.x+1)
            mine_y = random.randrange(1, self.y+1)

            if self.map[mine_x][mine_y] != self.mine:
                self.map[mine_x][mine_y] = self.mine
                check_mine += 1

    def view_map(self):
        for i in range(len(self.map)):
            print(self.map[i])

    def find_mine(self):
        for i in range(1, self.x+1):
            for j in range(1, self.y+1):
                if self.map[i][j] != self.mine:
                    self.map[i][j] = self.check_square(i, j)

    def view_square(self, x, y):
        square = []

        for i in range(x-1, x+2):
            temp_array = []
            for j in range(y-1, y+2):
                temp_array.append(self.map[i][j])
            square.append(temp_array)
        return square

#간소화 시키기
    def check_square(self, x, y):
        is_mine = 0

        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if i == x and j == y:
                    pass
                else:
                    if self.map[i][j] == self.mine:
                        is_mine += 1

        return is_mine

if __name__ == '__main__':

    m = mine_Sweeper()
    m.create_map()
    m.create_mine()
    m.view_map()
    m.find_mine()
    m.view_map()
