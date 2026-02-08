class Solution:
    def finalPositionOfSnake(self, n, commands):
        row = 0
        col = 0

        for cmd in commands:
            if cmd == "UP":
                row -= 1
            elif cmd == "DOWN":
                row += 1
            elif cmd == "LEFT":
                col -= 1
            else:  # RIGHT
                col += 1

        return row * n + col
