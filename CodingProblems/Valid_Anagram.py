class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)

        if m != n:
            return False

        count = {}

        for i in range(0, n):
            if count.get(s[i]) == None:
                count[s[i]] = 0
            if count.get(t[i]) == None:
                count[t[i]] = 0
            count[s[i]] += 1
            count[t[i]] -= 1

        for key in count:
            if count[key] != 0:
                return False

        return True
