class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_len = 1e9
        left = 0
        n = len(s)
        total_unique = 0
        current_unique = 0
        t_count = [0] * 256
        s_count = [0] * 256
        final_left = -1
        final_right = -1

        for ch in t:
            t_count[ord(ch)] += 1
            if t_count[ord(ch)] == 1:
                total_unique += 1

        for right in range(n):
            idx = ord(s[right])
            s_count[idx] += 1
            if s_count[idx] == t_count[idx]:
                current_unique += 1
            if current_unique == total_unique:
                while True:
                    idx = ord(s[left])
                    if s_count[idx] == t_count[idx]:
                        break
                    s_count[idx] -= 1
                    left += 1
                if min_len > (right - left + 1):
                    final_left = left
                    final_right = right
                    min_len = right - left + 1

        return s[final_left:final_right + 1] if final_left != -1 else ""
