# User function Template for python3

class Solution:
    def findTime(self, s1, s2):
        # code here
        index = {}
        pointer = 0
        ans = 0

        for i in range(0, 26):
            index[s1[i]] = i

        for ch in s2:
            ans += abs(index[ch] - pointer)
            pointer = index[ch]

        return ans


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S1 = input()
        S2 = input()

        ob = Solution()
        print(ob.findTime(S1, S2))
# } Driver Code Ends
