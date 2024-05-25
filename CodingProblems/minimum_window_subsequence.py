# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends
# User function Template for python3

class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        m = len(s1)
        n = len(s2)
        min_len = 1e9
        s1_itr = 0
        s2_itr = 0
        final_left = -1
        final_right = -1

        while s1_itr < m:
            if s1[s1_itr] == s2[s2_itr]:
                # Full match
                if s2_itr == n - 1:
                    right = s1_itr
                    while s2_itr >= 0:
                        if s1[s1_itr] == s2[s2_itr]:
                            s2_itr -= 1
                        s1_itr -= 1
                    left = s1_itr + 1
                    s2_itr = 0
                    s1_itr = s1_itr + 1
                    if min_len > (right - left + 1):
                        min_len = right - left + 1
                        final_left = left
                        final_right = right
                else:
                    s2_itr += 1
            s1_itr += 1

        return s1[final_left:final_right + 1] if final_left != -1 else ""


# Code here

# {
# Driver Code Starts.
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        str1 = input()
        str2 = input()
        ob = Solution()
        res = ob.minWindow(str1, str2)
        print(res)
# } Driver Code Ends
