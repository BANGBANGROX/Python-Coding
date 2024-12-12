#User function Template for python3


class Solution:
    def chooseandswap(self, s: str) -> str:
        # code here
        n: int = len(s)
        first_index: list[int] = [-1] * 26
        old_char: str = '#'
        new_char: str = '#'

        for i in range(n):
            idx = ord(s[i]) - ord('a')
            if first_index[idx] == -1:
                first_index[idx] = i

        for ch in s:
            flag: bool = False
            for idx in range(ord('a'), ord(ch)):
                if first_index[idx - ord('a')] > first_index[ord(ch) - ord('a')]:
                    old_char = ch
                    new_char = chr(idx)
                    flag = True
                    break
            if flag:
                break

        if old_char == '#':
            return s

        s_list: list[str] = list(s)

        for i in range(n):
            if s_list[i] == old_char:
                s_list[i] = new_char
            elif s_list[i] == new_char:
                s_list[i] = old_char

        return "".join(s_list)



#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        A = input()
        ans = ob.chooseandswap(A)
        print(ans)
        print("~")

# } Driver Code Ends