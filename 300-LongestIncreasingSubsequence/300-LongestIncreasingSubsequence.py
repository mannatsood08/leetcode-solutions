"""
Complexity Analysis:
    - Time Complexity: O(nlogn)
    - Space Complexity: O(n)
"""

class BinarySearch:
    def find_smallest_index(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low

    def find_length_of_LIS(self, nums):
        LIS = []
        for num in nums:
            idx = self.find_smallest_index(LIS, num)
            if idx == len(LIS):
                LIS.append(num)
            else:
                LIS[idx] = num
        return len(LIS)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return BinarySearch().find_length_of_LIS(nums)