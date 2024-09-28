from collections import deque

class MyCircularDeque:
    def __init__(self, k: int):
        self.__max_size: int = k
        self.__deque: deque = deque()

    def insertFront(self, value: int) -> bool:
        if len(self.__deque) >= self.__max_size:
            return False
        
        self.__deque.appendleft(value)
        
        return True

    def insertLast(self, value: int) -> bool:
        if len(self.__deque) >= self.__max_size:
            return False
        
        self.__deque.append(value)
        
        return True

    def deleteFront(self) -> bool:
        if len(self.__deque) == 0:
            return False
        
        self.__deque.popleft()
        
        return True

    def deleteLast(self) -> bool:
        if len(self.__deque) == 0:
            return False
        
        self.__deque.pop()
        
        return True

    def getFront(self) -> int:
        if len(self.__deque) == 0:
            return -1
        
        return self.__deque[0]

    def getRear(self) -> int:
        if len(self.__deque) == 0:
            return -1
        
        return self.__deque[-1]

    def isEmpty(self) -> bool:
        return len(self.__deque) == 0

    def isFull(self) -> bool:
        return len(self.__deque) == self.__max_size
