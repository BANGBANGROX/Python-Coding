class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        count: list[int] = [0] * k

        for num in arr:
            count[num % k] += 1

        if count[0] % 2 != 0:
            return False

        for first_rem in range(1, k):
            second_rem: int = (k - first_rem) % k
            if count[first_rem] != count[second_rem]:
                return False

        return True


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        n: int = int(input())
        arr: list[int] = [0] * n
        for i in range(n):
            arr[i] = int(input())
        k: int = int(input())

        print(Solution().canArrange(arr=arr, k=k))
