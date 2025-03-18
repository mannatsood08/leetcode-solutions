class Solution(object):
    def minSubArrayLen(self, target, nums):
        m = float('inf')
        c_sum = i = 0
        for j in range(len(nums)):
            c_sum+= nums[j]
            if c_sum >=target:
                while c_sum-nums[i]>=target:
                    c_sum-=nums[i]
                    i+=1
                m = min(m, j-i+1)
        return m if m != float('inf') else 0