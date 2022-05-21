# User function Template for python3

class Solution:
    def findAndReplace(self, s, q, index, sources, targets):
        # code here
        ans = s
        shift = 0

        for i in range(0, q):
            ind = index[i]
            source = sources[i]
            target = targets[i]
            if s[ind:len(source) + ind] == source:
                ind += shift
                ans = ans[:ind] + target + ans[ind + len(source):]
                shift += len(target) - len(source)

        return ans
        # {
        #  Driver Code Starts
        # Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()
        Q = int(input())
        index = list(map(int, input().split()))
        sources = list(map(str, input().split()))
        targets = list(map(str, input().split()))

        ob = Solution()
        print(ob.findAndReplace(S, Q, index, sources, targets))
# } Driver Code Ends
