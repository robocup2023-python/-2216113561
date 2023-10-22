import random
import time

class Universe:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.current_generation = [[' ' for _ in range(width)] for _ in range(height)]
        self.next_generation = [[' ' for _ in range(width)] for _ in range(height)]

    def seed(self):
        for y in range(self.height):
            for x in range(self.width):
                if random.random() < 0.25:
                    self.current_generation[y][x] = '*'

    def alive(self, x, y):
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            return False
        return self.current_generation[y][x] == '*'

    def neighbors(self, x, y):
        count = 0
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                if self.alive(x + dx, y + dy):
                    count += 1
        return count

    def next(self):
        for y in range(self.height):
            for x in range(self.width):
                count = self.neighbors(x, y)
                if self.current_generation[y][x] == '*':
                    if count < 2 or count > 3:
                        self.next_generation[y][x] = ' '
                    else:
                        self.next_generation[y][x] = '*'
                else:
                    if count == 3:
                        self.next_generation[y][x] = '*'
                    else:
                        self.next_generation[y][x] = ' '
        self.current_generation, self.next_generation = self.next_generation, self.current_generation

    def show(self):
        print('\033[H')  # 清空屏幕
        for row in self.current_generation:
            print(''.join(row))
        time.sleep(0.2)  # 控制迭代速度

def main():
    width = 80
    height = 15
    universe = Universe(width, height)
    universe.seed()

    while True:
        universe.show()
        universe.next()

if __name__ == "__main__":
    main()
