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


if __name__ == "__main__":
    my_circular_deque: MyCircularDeque = MyCircularDeque(k=2)
    print(my_circular_deque.insertFront(value=1))
    print(my_circular_deque.insertLast(value=2))
    print(my_circular_deque.insertFront(value=3))
    print(my_circular_deque.insertLast(value=4))
    print(my_circular_deque.getFront())
    print(my_circular_deque.getRear())
    print(my_circular_deque.isEmpty())
    print(my_circular_deque.isFull())
    print(my_circular_deque.deleteFront())
    print(my_circular_deque.deleteLast())
    print(my_circular_deque.deleteFront())
    print(my_circular_deque.deleteLast())
    print(my_circular_deque.isEmpty())
    print(my_circular_deque.isFull())
