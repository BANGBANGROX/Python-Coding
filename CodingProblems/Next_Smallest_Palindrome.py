# User function Template for python3
class Solution:
    def makePalindrome(self, num, n):
        ans = [0 for _ in range(n)]

        for i in range(0, (n - 1) // 2 + 1):
            ans[i] = num[i]
            ans[n - i - 1] = num[i]

        return ans

    def compare(self, a, b, n):
        for i in range(0, n):
            if a[i] > b[i]:
                return True
            if a[i] < b[i]:
                return False

        return False

    def all9(self, num, n):
        for i in range(0, n):
            if num[i] != 9:
                return False

        return True

    def generateNextPalindrome(self, num, n):
        # code here
        ans = []

        if self.all9(num, n):
            ans.append(1)
            for _ in range(1, n):
                ans.append(0)
            ans.append(1)
            return ans

        palindromeNum = self.makePalindrome(num, n)

        if self.compare(palindromeNum, num):
            return palindromeNum

        carry = 1

        for i in range((n - 1) // 2, -1, -1):
            value = palindromeNum[i] + carry
            palindromeNum[i] = value % 10
            carry = value // 10

        return self.makePalindrome(palindromeNum)
        # {
     # Driver Code Starts
        # Initial Template for Python 3


        # Driver code
if __name__ == "__main__":
    tc = int(input())
    while tc > 0:
        n = int(input())
        num = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.generateNextPalindrome(num, n)
        for x in ans:
            print(x, end=" ")
        print()
        tc = tc-1
# } Driver Code Ends
