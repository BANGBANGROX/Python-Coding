from typing import List
import heapq


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        maxBricks = []
        completed = 1
        i = 0

        for i in range(0, n - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                completed += 1
                continue
            bricks -= diff
            heapq.heappush(maxBricks, -1 * diff)
            if bricks < 0:
                bricks += -1 * heapq.heappop(maxBricks)
                ladders -= 1
            if ladders < 0:
                break
            completed += 1

        return completed - 1
