from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a = [] 
        for i in range(len(nums)): 
            count = 0  
            for j in range(len(nums)): 
                if nums[i] > nums[j]:  
                    count += 1 
            a.append(count)  
        return a  
