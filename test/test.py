__author__ = 'uiandwe'

import pytest
xfail = pytest.mark.xfail

from ..minesweeper.minesweeper import mine_Sweeper

m = mine_Sweeper()


def test_check_create_map():
    m.create_map()
    assert len(m.map) == 12
    assert len(m.map[0]) == 12


def test_check_mine_count():
    m.create_mine()
    count = 0
    for i in range(m.x):
        for j in range(m.y):
            if m.map[i][j] == "X":
                count += 1
    assert count == 10
#
#
# def test_check_mine_square():
#     map = [['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X'],
#             ['O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
#             ['O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O'],
#             ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
#             ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
#             ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X'],
#             ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
#             ['O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
#             ['O', 'O', 'O', 'O', 'X', 'X', 'O', 'O', 'O', 'O'],
#             ['O', 'X', 'O', 'O', 'O', 'X', 'O', 'O', 'X', 'O']]
#     m.map = map
#     assert m.view_square(8, 1) == [['O', 'O', 'X'], ['O', 'O', 'O'], ['O', 'O', 'O']]
#     m.view_map()
#     count = m.check_square(8, 1)
#     assert count == 2


@xfail
def test_bubble_fail():
    temp_list = [9, 2, 6, 1, 8, 10, 4, 5, 3, 7]
