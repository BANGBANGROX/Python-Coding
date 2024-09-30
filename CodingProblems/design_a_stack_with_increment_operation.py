class CustomStack:
    def __init__(self, max_size: int):
        self.__stack: list[int] = []
        self.__max_size: int = max_size

    def push(self, x: int) -> None:
        if len(self.__stack) == self.__max_size:
            return

        self.__stack.append(x)

    def pop(self) -> int:
        if len(self.__stack) == 0:
            return -1

        return self.__stack.pop()

    def increment(self, k: int, val: int) -> None:
        curr_size: int = len(self.__stack)

        for i in range(min(curr_size, k)):
            self.__stack[i] += val


if __name__ == "__main__":
    custom_stack: CustomStack = CustomStack(max_size=2)

    custom_stack.push(x=1)
    custom_stack.push(x=2)
    print(custom_stack.pop())
    custom_stack.increment(k=1, val=1)
    print(custom_stack.pop())
    print(custom_stack.pop())
