class CountInversionsService:
    def __init__(self, array: list) -> None:
        self.array = array

    def _merge(self, left: int, mid: int, right: int) -> int:
        result = 0
        i = left
        j = mid + 1
        k = 0
        auxiliary_array = [0] * (right - left + 1)

        while i <= mid and j <= right:
            if self.array[i] <= self.array[j]:
                auxiliary_array[k] = self.array[i]
                i += 1
            else:
                auxiliary_array[k] = self.array[j]
                j += 1
                result += (mid - i + 1)
            k += 1

        while i <= mid:
            auxiliary_array[k] = self.array[i]
            i += 1
            k += 1

        while j <= right:
            auxiliary_array[k] = self.array[j]
            j += 1
            k += 1

        k = 0
        i = left

        while i <= right:
            self.array[i] = auxiliary_array[k]
            i += 1
            k += 1

        return result

    def count_inversions(self, left: int, right: int) -> int:
        result = 0

        if left < right:
            mid = (left + right) // 2
            result += self.count_inversions(left, mid)
            result += self.count_inversions(mid + 1, right)
            result += self._merge(left, mid, right)

        return result


class Solution:
    def great_count(self, n: int, s: str) -> int:
        prefix_array = [0] * n
        answer = 0

        prefix_array[0] = 1 if s[0] == '1' else -1

        if prefix_array[0] > 0:
            answer += 1

        for i in range(1, n):
            prefix_array[i] = prefix_array[i - 1] + (1 if s[i] == '1' else -1)
            if prefix_array[i] > 0:
                answer += 1

        prefix_array.reverse()

        answer += CountInversionsService(prefix_array).count_inversions(0, n - 1)

        return answer


# code here


# {
# Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N = int(input())

        S = (input())

        obj = Solution()
        res = obj.great_count(N, S)

        print(res)

# } Driver Code Ends
