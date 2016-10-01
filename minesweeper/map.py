
class map:
    x = 0
    y = 0
    map = []

    def __init__(self, x=10, y=10):
        self.x = x
        self.y = y

        for i in range(x):
            temp_array = []
            for j in range(y):
                temp_array.append(0)
            self.map.append(temp_array)

    def view_map(self):
        for i in range(1, self.x):
            print(self.map[i][1:self.y])
