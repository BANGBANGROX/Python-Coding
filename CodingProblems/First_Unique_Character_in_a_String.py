class Solution:
    def firstUniqChar(self, s: str) -> int:
        index = {}
        n = len(s)

        for i in range(0, n):
            if index.get(s[i]) == None:
                index[s[i]] = i
            else:
                index[s[i]] = -1

        for key in index:
            if index[key] != -1:
                return index[key]

        return -1
