class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list: list[str] = list(str(num))
        n: int = len(num_list)

        for i in range(n):
            max_idx: int = i
            for j in range(i + 1, n):
                if ord(num_list[j]) >= ord(num_list[max_idx]):
                    max_idx = j
            if max_idx != i and num_list[max_idx] != num_list[i]:
                temp: str = num_list[i]
                num_list[i] = num_list[max_idx]
                num_list[max_idx] = temp
                break

        return int("".join(num_list))


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        print(Solution().maximumSwap(num=int(input())))
