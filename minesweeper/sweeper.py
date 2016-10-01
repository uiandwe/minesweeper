
from .mine import mine as m


class sweeper:

    mine = None

    def __init__(self):
        self.mine = m(12, 12)
        self.mine.create_mine()

    def view_map(self):
        for i in range(1, self.mine.x-1):
            print(self.mine.mine_map[i][1:self.mine.y-1])

    '''
    mine 찾기 위한 map 재귀 순회
    mine 찾을시 check_square() 호출
    '''
    def recursive_find_mine(self, x=1, y=1):

        if self.mine.mine_map[x][y] == self.mine.mine:
            self.check_square(x, y)

        if y >= 10:
            self.recursive_find_mine(x+1, 1)
        elif x >= 10:
            return
        else:
            self.recursive_find_mine(x, y+1)


    '''
    mine 찾기 위한 map 순회
    mine을 찾을시 check_square() 호출
    '''
    def find_mine(self):
        for i in range(1, self.mine.x-1):
            for j in range(1, self.mine.y-1):
                if self.mine.mine_map[i][j] == self.mine.mine:
                    self.check_square(i, j)

    def view_square(self, x, y):
        square = []

        for i in range(x-1, x+2):
            temp_array = []
            for j in range(y-1, y+2):
                temp_array.append(self.mine.mine_map[i][j])
            square.append(temp_array)
        return square

    '''
    해당 좌표(mine)를 중심으로 +1식 증가

    :param  int x int y
    '''
    def check_square(self, x, y):
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if type(self.mine.mine_map[i][j]) is int:
                    self.mine.mine_map[i][j] += 1


