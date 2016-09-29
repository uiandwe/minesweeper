__author__ = 'uiandwe'


import pytest
xfail = pytest.mark.xfail


from minesweeper.minesweeper import mine_Sweeper


def test_check_create_map():
    m = mine_Sweeper()
    m.create_map()

    assert len(m.map) == 10


@xfail
def test_bubble_fail():
    temp_list = [9, 2, 6, 1, 8, 10, 4, 5, 3, 7]
    # s = sorting.sorting.sorting()
    # assert s.bubble(temp_list) == [1, 2, 3, 4, 5, 6, 7, 8, 9]