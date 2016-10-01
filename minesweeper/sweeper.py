import random, sys
from .mine import mine as m


class sweeper:

    mine = None

    def __init__(self):
        self.mine = m()

    def exception_check_mine_obj(self):
        if self.mine is None:
            sys.exit(" sweeper init error. ")

    def exception_check_mine_size(self):
        if self.mine.x <= 0 or self.mine.y <= 0:
            sys.exit(" mine map size size should be greater than zero. ")

    '''
    입력된 x,y 만큼의 map 생성
    '''
    def create_map(self):
        self.exception_check_mine_obj()

        for i in range(self.mine.x+2):
            temp_map_array = []
            for j in range(self.mine.y+2):
                temp_map_array.append(self.mine.empty)
            self.mine.map.append(temp_map_array)

    '''
    map 에 줌 랜덤 좌표로 mine 을 넣어줌
    '''
    def create_mine(self):

        self.exception_check_mine_obj()
        self.exception_check_mine_size()

        check_mine = 0
        while check_mine < self.mine.mine_count:
            mine_x = random.randrange(1, self.mine.x+1)
            mine_y = random.randrange(1, self.mine.y+1)

            if self.mine.map[mine_x][mine_y] != self.mine.mine:
                self.mine.map[mine_x][mine_y] = self.mine.mine
                check_mine += 1

    def view_map(self):
        for i in range(1, self.mine.x+1):
            print(self.mine.map[i][1:self.mine.y+1])

    '''
    mine 찾기 위한 map 순회
    '''
    def find_mine(self):
        for i in range(1, self.mine.x+1):
            for j in range(1, self.mine.y+1):
                if self.mine.map[i][j] == self.mine.mine:
                    self.check_square(i, j)

    def view_square(self, x, y):
        square = []

        for i in range(x-1, x+2):
            temp_array = []
            for j in range(y-1, y+2):
                temp_array.append(self.mine.map[i][j])
            square.append(temp_array)
        return square

    '''
    해당 좌표(mine)를 중심으로 +1식 증가

    :param  int x int y
    '''
    def check_square(self, x, y):
        is_mine = 0

        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if i == x and j == y:
                    pass
                else:
                    if type(self.mine.map[i][j]) is int:
                        self.mine.map[i][j] += 1

        return is_mine

if __name__ == '__main__':

    mine_sweeper = sweeper()
    mine_sweeper.create_map()
    mine_sweeper.create_mine()
    mine_sweeper.view_map()
    mine_sweeper.find_mine()
    mine_sweeper.view_map()
