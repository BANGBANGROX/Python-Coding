class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        taken = {}
        needed = (1 << k)
        n = len(s)

        for i in range(k, n + 1):
            code = s[i-k:i]
            if taken.get(code) == None:
                taken[code] = True
                needed -= 1
                if needed == 0:
                    return True

        return False
