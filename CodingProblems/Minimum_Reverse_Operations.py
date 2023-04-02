from typing import List


def minReverseOperations(n: int, p: int, banned: List[int], k: int) -> List[int]:
    moves = 0
    ans = [-1 for _ in range(n)]
    skip = [False for _ in range(n)]
    odd = set()
    even = set()
    queue = []

    for ban in banned:
        skip[ban] = True

    for i in range(n):
        if i == p or skip[i]:
            continue
        if i % 2 == 0:
            even.add(i)
        else:
            odd.add(i)

    queue.append(p)

    while len(queue) > 0:
        size = len(queue)
        for i in range(size):
            current = queue.pop()
            ans[current] = moves
            min_index = k - current - 1
            first_max_index = n - current - 1
            max_index = k - first_max_index - 1
            if min_index < 0:
                min_index = current - k + 1
            if max_index:
                max_index = first_max_index - k + 1
            max_index = n - max_index - 1
            current_set = even if min_index % 2 == 0 else odd
            key = current_set.ceiling(min_index)
            while key is not None and key <= max_index:
                queue.append(key)
                current_set.remove(key)
                key = current_set.ceiling(min_index)
        moves += 1

    return ans


class Solution:
    pass
