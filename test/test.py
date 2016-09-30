from ..minesweeper.sweeper import sweeper
import pytest
xfail = pytest.mark.xfail


test_mine = sweeper()


def test_check_create_map():
    test_mine.create_map()
    assert len(test_mine.mine.map) == 12
    assert len(test_mine.mine.map[0]) == 12


def test_check_mine_count():
    test_mine.create_mine()
    count = 0
    for i in range(test_mine.mine.x+2):
        for j in range(test_mine.mine.y+2):
            if test_mine.mine.map[i][j] == "X":
                count += 1
    assert count == 10


def test_check_mine_square():
    map = [['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
           ['O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
           ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'O'],
           ['O', 'O', 'O', 'X', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O'],
           ['O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
           ['O', 'O', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
           ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O'],
           ['O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
           ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
           ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
           ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'O'],
           ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]

    test_mine.mine.map = map
    assert test_mine.view_square(2, 3) == [['O', 'X', 'O'], ['O', 'O', 'O'], ['O', 'X', 'O']]

    count = test_mine.check_square(2, 3)
    assert count == 2


@xfail
def test_bubble_fail():
    temp_list = [9, 2, 6, 1, 8, 10, 4, 5, 3, 7]
