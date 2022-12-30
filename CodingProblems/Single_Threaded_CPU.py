from typing import List
import heapq


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        ans = [0 for _ in range(n)]
        pq = []
        sortedTasks = []

        for i in range(n):
            sortedTasks.append((tasks[i][0], tasks[i][1], i))

        sortedTasks.sort()
        heapq.heapify(pq)

        taskIndex = 0
        ansIndex = 0
        currentTime = 0

        while taskIndex < n or len(pq) > 0:
            if len(pq) == 0 and currentTime < sortedTasks[taskIndex][0]:
                currentTime = sortedTasks[taskIndex][0]
            while taskIndex < n and currentTime >= sortedTasks[taskIndex][0]:
                heapq.heappush(pq, (sortedTasks[taskIndex][1], sortedTasks[taskIndex][2]))
                taskIndex += 1
            tup = heapq.heappop(pq)
            processingTime = tup[0]
            index = tup[1]
            currentTime += processingTime
            ans[ansIndex] = index
            ansIndex += 1

        return ans


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        tasks = []
        for j in range(n):
            a = int(input())
            b = int(input())
            tasks.append([a, b])

        solution = Solution()
        print(solution.getOrder(tasks))
