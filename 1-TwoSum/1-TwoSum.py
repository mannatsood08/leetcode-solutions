class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        for i,v in enumerate (nums):
            diff=target-v
            if diff in h:
                return [h[diff],i]
            h[v]=i

