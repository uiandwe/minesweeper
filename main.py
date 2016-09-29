__author__ = 'uiandwe'
from minesweeper import minesweeper


if __name__ == '__main__':
    m = minesweeper.mine_Sweeper()
    m.create_map()
    m.create_mine()
    m.find_mine()
    m.view_map()


