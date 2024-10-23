# User function Template for python3


class Solution:
    def __init__(self) -> None:
        self.answer: list[int] = None

    def _multiply(self, num: int, size: int) -> int:
        carry: int = 0

        for i in range(size):
            val: int = self.answer[i] * num + carry
            self.answer[i] = val % 10
            carry = val // 10

        while carry > 0:
            self.answer[size] = carry % 10
            carry //= 10
            size += 1

        return size

    def factorial(self, n: int) -> list[int]:
        # code here
        MAX_SIZE: int = 10**6 + 5
        self.answer = [0] * MAX_SIZE
        final_answer: list[int] = []
        curr_size: int = 1

        self.answer[0] = 1

        for i in range(2, n + 1):
            curr_size = self._multiply(i, curr_size)

        for i in range(curr_size - 1, -1, -1):
            final_answer.append(self.answer[i])

        return final_answer


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t: int = int(input())
    for _ in range(t):
        N: int = int(input())
        ob: Solution = Solution()
        ans: list[int] = ob.factorial(N)
        for i in ans:
            print(i, end="")
        print()

# } Driver Code Ends
