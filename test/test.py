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


def test_check_view_square():
    map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 'X', 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 'X', 0, 0, 0],
            [0, 0, 0, 0, 'X', 0, 0, 0, 0, 0, 'X', 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 'X', 0, 0, 0, 0, 0, 'X', 0, 0, 0, 0],
            [0, 'X', 0, 0, 0, 0, 0, 'X', 0, 'X', 0, 0],
            [0, 0, 0, 0, 0, 'X', 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    test_mine.mine.map = map
    assert test_mine.view_square(2, 8) == [[0, 'X', 0], [0, 0, 0], [0, 'X', 0]]


def test_check_find_mine():
    test_mine.find_mine()
    assert test_mine.view_square(2, 8) == [[1, 'X', 1], [2, 2, 2], [1, 'X', 2]]


@xfail
def test_bubble_fail():
    temp_list = [9, 2, 6, 1, 8, 10, 4, 5, 3, 7]
