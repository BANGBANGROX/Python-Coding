
# Back-end complete function Template for Python 3

class Solution:
    def transform(self, s, t):
        # code here.
        count1 = {}
        count2 = {}
        m = len(s)
        n = len(t)

        if m != n:
            return -1

        for i in range(0, m):
            if (count1.get(s[i]) == None):
                count1[s[i]] = 0
            count1[s[i]] += 1

        for i in range(0, n):
            if (count2.get(t[i]) == None):
                count2[t[i]] = 0
            count2[t[i]] += 1

        for key in count1:
            if (count2.get(key) == None or count2[key] != count1[key]):
                return -1

        i = m - 1
        j = n - 1
        ans = 0

        while (i >= 0):
            if s[i] == t[j]:
                j -= 1
            else:
                ans += 1
            i -= 1

        return ans

        # {
        #  Driver Code Starts
        # Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        line = input().strip().split()
        A = line[0]
        B = line[1]
        ob = Solution()
        print(ob.transform(A, B))
# } Driver Code Ends
