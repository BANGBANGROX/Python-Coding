# User function Template for python3
'''
class Job:

    # Job class which stores profit and deadline.

    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0
'''

class Job:

    def __init__(self, id: int, deadline: int, profit: int):
        self.id = id
        self.deadline = deadline
        self.profit = profit


class Solution:

    # Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self, jobs: list[Job], n: int) -> list[int]:
        visited = [False] * (n + 1)
        total_jobs = 0
        total_profit = 0

        jobs.sort(key=lambda x: -1 * x.profit)

        for i in range(n):
            while jobs[i].deadline > 0 and visited[jobs[i].deadline]:
                jobs[i].deadline -= 1
            if jobs[i].deadline > 0:
                visited[jobs[i].deadline] = True
                total_jobs += 1
                total_profit += jobs[i].profit

        return [total_jobs, total_profit]


# code here


# {
# Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys



if __name__ == "__main__":
    t: int = int(input())
    for _ in range(t):
        job_ids: list[int] = list(map(int, input().split()))
        deadlines: list[int] = list(map(int, input().split()))
        profits: list[int] = list(map(int, input().split()))

        n: int = len(job_ids)
        jobs: list[Job] = [Job(job_ids[i], deadlines[i], profits[i]) for i in range(n)]

        obj: Solution = Solution()
        ans: list[int] = obj.JobScheduling(jobs, n)
        print(ans[0], ans[1])
        print("~")

# } Driver Code Ends