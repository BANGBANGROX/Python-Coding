class Solution:
    def __init__(self) -> None:
        self.__answer: list[int] = None
        self.__max_length: int = 0
        self.__max_number: int = 0

    def __generate_numbers(self, pos: int, current_number: int) -> None:
        if current_number <= self.__max_number and current_number > 0:
            self.__answer.append(current_number)

        if pos >= self.__max_length:
            return

        for dig in range(1 if pos == 0 else 0, 10):
            self.__generate_numbers(
                pos=pos + 1, current_number=current_number * 10 + dig
            )

    def lexicalOrder(self, n: int) -> list[int]:
        self.__answer = []
        self.__max_length = len(str(n))
        self.__max_number = n

        self.__generate_numbers(pos=0, current_number=0)

        return self.__answer


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        print(Solution().lexicalOrder(n=int(input())))
