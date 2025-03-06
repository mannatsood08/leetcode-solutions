class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1 = 0
        prev2 = 0
        for num in nums:
            temp = prev1
            prev1 = max(prev2 + num,prev1)
            prev2 = temp
        return prev1