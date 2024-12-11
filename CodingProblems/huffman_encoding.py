#User function Template for python3
import heapq

class Node:
    def __init__(self, val: int, left: 'Node' | None, right: 'Node' | None) -> None:
        self.val: int = val
        self.left: Node = left
        self.right: Node = right

    def __lt__(self, other: 'Node') -> bool:
        return self.val < other.val


class Solution:
    def __int__(self) -> None:
        self.__answer = None

    def __traverse(self, node, current) -> None:
        if node.left is None:
            self.__answer.append(current)
        else:
            self.__traverse(node.left, current + '0')
            self.__traverse(node.right, current + '1')

    def huffmanCodes(self,S, f, N) -> list[str]:
        # Code here
        pq = []

        for val in f:
            heapq.heappush(pq, Node(val, None, None))

        while len(pq) > 1:
            n1 = heapq.heappop(pq)
            n2 = heapq.heappop(pq)
            heapq.heappush(pq, Node(n1.val + n2.val, n1, n2))

        self.__answer = []
        self.__traverse(heapq.heappop(pq), '')

        return self.__answer

#{
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t: int =int(input())
	for i in range(t):
		S: str = input()
		N: int = len(S)
		f: list[int] = [int(x) for x in input().split()]
		ob: Solution = Solution()
		ans: list[str] = ob.huffmanCodes(S,f,N)
		for i in ans:
		    print(i, end = " ")
		print()
# } Driver Code Ends