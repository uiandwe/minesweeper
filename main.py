from minesweeper.sweeper import sweeper


if __name__ == '__main__':

    mine_sweeper = sweeper()
    mine_sweeper.create_map()
    mine_sweeper.create_mine()
    mine_sweeper.view_map()
    mine_sweeper.find_mine()
    mine_sweeper.view_map()


