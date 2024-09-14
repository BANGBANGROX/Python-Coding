class Solution:
    def __init__(self) -> None:
        self.__k: int = 0
        self.__required_length: int = 0
        self.__answer: int = 0
        self.__is_odd_length: bool = False
        self.__factorial: list[int] = None
        self.__visited: set[str] = None

    def __compute_factorial(self, n: int) -> None:
        self.__factorial = [0] * (n + 1)

        self.__factorial[0] = self.__factorial[1] = 1

        for i in range(2, n + 1):
            self.__factorial[i] = self.__factorial[i - 1] * i

    def __is_divisible_by_k(self, num: str) -> bool:
        result: int = 0

        for ch in num:
            result = (result * 10 + ord(ch) - ord("0")) % self.__k

        return result == 0

    def __get_permutations_without_leading_zeroes(self, num: str) -> int:
        n: int = len(num)
        total_permutations: int = self.__factorial[n]
        count: list[int] = [0] * 10

        for ch in num:
            count[ord(ch) - ord("0")] += 1

        for i in range(10):
            if count[i] > 0:
                total_permutations //= self.__factorial[count[i]]

        if count[0] == 0:
            return total_permutations

        permutations_with_leading_zeroes: int = self.__factorial[n - 1]
        permutations_with_leading_zeroes //= self.__factorial[count[0] - 1]

        for i in range(1, 10):
            if count[i] > 0:
                permutations_with_leading_zeroes //= self.__factorial[count[i]]

        return total_permutations - permutations_with_leading_zeroes

    def __generate_palindromes(self, pos: int, current_number: int) -> None:
        if pos >= self.__required_length:
            num_str: str = str(current_number)
            end: int = (
                self.__required_length - 1
                if self.__is_odd_length
                else self.__required_length
            )
            second_half_list: list = list(num_str[:end])
            second_half_list.reverse()
            num_str += "".join(second_half_list)

            if self.__is_divisible_by_k(num=num_str):
                sorted_num_str: str = "".join(sorted(num_str))
                if sorted_num_str not in self.__visited:
                    self.__answer += self.__get_permutations_without_leading_zeroes(
                        num=num_str
                    )
                    self.__visited.add(sorted_num_str)

            return

        for dig in range(0 if pos > 0 else 1, 10):
            self.__generate_palindromes(
                pos=pos + 1, current_number=current_number * 10 + dig
            )

    def countGoodIntegers(self, n: int, k: int) -> int:
        self.__k = k
        self.__required_length = (n + 1) // 2
        self.__answer = 0
        self.__is_odd_length = (n & 1) > 0
        self.__visited = set()

        self.__compute_factorial(n=n)
        self.__generate_palindromes(pos=0, current_number=0)

        return self.__answer


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        print(Solution().countGoodIntegers(n=int(input()), k=int(input())))
