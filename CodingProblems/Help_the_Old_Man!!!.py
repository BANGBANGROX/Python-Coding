# User function Template for python3

class Solution:
    def shiftPileUtil(self, N, state, start, end, aux):
        if N == 1:
            state[0] -= 1
            if state[0] == 0:
                self.ans.append(start)
                self.ans.append(end)
            return

        self.shiftPileUtil(N - 1, state, start, aux, end)

        state[0] -= 1

        if state[0] == 0:
            self.ans.append(start)
            self.ans.append(end)

        self.shiftPileUtil(N - 1, aux, end, start)

    def shiftPile(self, N, n):
        # code here
        self.ans = []
        state = [n]

        self.shiftPileUtil(N, state, 1, 3, 2)

        return self.ans

# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, n = [int(x) for x in input().split()]

        ob = Solution()
        ans = ob.shiftPile(N, n)
        print(str(ans[0])+" "+str(ans[1]))
# } Driver Code Ends
