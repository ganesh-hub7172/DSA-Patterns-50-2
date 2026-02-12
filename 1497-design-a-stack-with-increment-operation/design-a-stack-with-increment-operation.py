class CustomStack:

    def __init__(self, maxSize):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x):
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self):
        if not self.stack:
            return -1
        return self.stack.pop()

    def increment(self, k, val):
        limit = min(k, len(self.stack))
        for i in range(limit):
            self.stack[i] += val
