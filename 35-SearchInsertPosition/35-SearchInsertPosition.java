// Last updated: 6/24/2025, 1:19:53 AM
class Solution {
    public int searchInsert(int[] nums, int target) {
        int start = 0;
        int end = nums.length - 1;

        while (start <= end) { 
            int middle = start + (end - start) / 2;

            if (target > nums[middle]) {
                start = middle + 1;
            } else if (target < nums[middle]) {
                end = middle - 1;
            } else {
                return middle; 
            }
        }

        // if not found, return the insert position
        return start;
    }
}
