from ast import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = {};
        count2 = {};
        ans = [];

        for num in nums1 :
           if count1.get(num) == None :
               count1[num] = 0;
           count1[num] += 1;

        for num in nums2 :
            if count2.get(num) == None : 
                count2[num] = 0;
            count2[num] += 1;

        for num in count1 :
           if count2.get(num) == None :
               continue;
           cnt = min(count1[num], count2[num]);    
           while cnt > 0 :
               ans.append(num);
               cnt -= 1;
                
        return ans;                       