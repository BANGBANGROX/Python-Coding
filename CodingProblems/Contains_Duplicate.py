from ast import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums);
        visited = {};

        for num in nums :
            if visited.get(num) == True :
                return True;
            visited[num] = True;
        
        return False;

