from collections import deque


class MyQueue:

    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()

    def push(self, x: int) -> None:
        if len(self.s1) == 0:
            self.s1.append(x)
            return

        while len(self.s1) > 0:
            self.s2.append(self.s1.pop())

        self.s2.append(x)

        while len(self.s2) > 0:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[len(self.s1) - 1]

    def empty(self) -> bool:
        return len(self.s1) == 0
