class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxx=max(nums)
        for i in range(maxx+2):
            if i in nums:
                continue
            else:
                return i