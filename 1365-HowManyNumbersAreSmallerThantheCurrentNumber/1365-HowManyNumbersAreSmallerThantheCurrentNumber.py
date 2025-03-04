from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a = []  # Initialize empty list
        for i in range(len(nums)):  # Iterate through each element
            count = 0  # Reset count for each element
            for j in range(len(nums)):  # Compare with all elements
                if nums[i] > nums[j]:  
                    count += 1  # Increase count if smaller number found
            a.append(count)  # Append count to result list
        return a  # Return final list
