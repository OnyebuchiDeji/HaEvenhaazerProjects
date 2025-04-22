from time import time

"""
    To test the efficiency of these operations:
        self.app.grid[self.y][self.x] = (value + 1) % 2
        self.app.grid[self.y][self.x] = not value
        self.app.grid[self.y][self.x] = value ^ 2   ##  Bitwise XOR, addition by modular 2

    In the video, the test gave the score that the logical NOT was the fastest
    The %2 and XOR took almost the same time, with ~0.003 difference, but the
    logical NOT by 0.5 whole seconds
"""

n = 10000000

value, start = 0, time()
for i in range(n):
    value = (value + 1) % 2
print(f'%2 time taken: {time() - start}')

value, start = 0, time()
for i in range(n):
    value = value ^ 1
print(f'bitwise XOR time taken: {time() - start}')

value, start = 0, time()
for i in range(n):
    value = not value
print(f'logical NOT, time taken: {time() - start}')